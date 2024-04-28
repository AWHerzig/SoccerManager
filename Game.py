from Objects import *


def game(home, away, show=False, ET = False, agg = [0, 0], neutral = False):
    home.rolesSet(opp = away.basetactic)
    away.rolesSet(opp = home.basetactic)
    #print(home.basetactic, home.tactic, home.qual, home.roles)
    #print(away.basetactic, away.tactic, away.qual, away.roles)
    home.score = agg[0]  # Almost always 0-0
    away.score = agg[1]
    matchup = TMdf.loc[home.tactic, away.tactic]
    # Chance ---- 
    oddsOfChance = .45 + (.05 if matchup[1] == 'sharp' else -.05 if matchup[1] == 'draw' else 0)
    homeposs = sum(home.qual[1:4]) + home.qual[2] + \
        (home.qual[0] if home.roles[0] == 'EleventhMan' else 0) + (home.qual[1] if home.roles[1] == 'Possession' else 0) + \
        (home.qual[2] if home.roles[2] == 'Control' else 0) + (home.qual[3] if home.roles[3] == 'False 9' else 0) + \
        matchup[0]
    awayposs = sum(away.qual[1:4]) + away.qual[2] + \
        (away.qual[0] if away.roles[0] == 'EleventhMan' else 0) + (away.qual[1] if away.roles[1] == 'Possession' else 0) + \
        (away.qual[2] if away.roles[2] == 'Control' else 0) + (away.qual[3] if away.roles[3] == 'False 9' else 0) - \
        matchup[0]
    diff = homeposs - awayposs
    oddsOfHomePoss = clamp((.5 if neutral else .55) + (math.sqrt(diff) if diff >= 0 else -1*math.sqrt(abs(diff))) / 400, \
                            .1, .9)
    homeSharp = sharpness(home, away)
    awaySharp = sharpness(away, home)
    homeFinish = shot(home, away)
    awayFinish = shot(away, home)
    homeGPM = oddsOfChance * oddsOfHomePoss * homeSharp * homeFinish
    awayGPM = oddsOfChance * (1 - oddsOfHomePoss) * awaySharp * awayFinish
    stoppage = random.randint(2, 10)
    note = 'Neutral Site ' if neutral else ''
    if not show:
        home.score += round(numpy.random.binomial(90 + stoppage, homeGPM))
        away.score += round(numpy.random.binomial(90 + stoppage, awayGPM))
        if home.score == away.score and ET:
            note = note + 'a.e.t.'
            home.score += round(numpy.random.binomial(30, homeGPM))
            away.score += round(numpy.random.binomial(30, awayGPM))
            if home.score == away.score:
                note = note + 'Penalties'
                if odds(.5): # Figure it out later
                    home.score += 1
                else:
                    away.score += 1
    else:
        for minute in range(1, 91 + stoppage): # 91 not included
            if odds(oddsOfChance):
                if odds(oddsOfHomePoss):
                    if odds(homeSharp):
                        if odds(homeFinish):
                            home.score += 1
                else:
                    if odds(awaySharp):
                        if odds(awayFinish):
                            away.score += 1
        if home.score == away.score and ET:
            note = note + 'a.e.t.'
            for minute in range(1, 31): # 31 not included
                if odds(oddsOfChance):
                    if odds(oddsOfHomePoss):
                        if odds(homeSharp):
                            if odds(homeFinish):
                                home.score += 1
                    else:
                        if odds(awaySharp):
                            if odds(awayFinish):
                                away.score += 1
            if home.score == away.score:
                note = note + 'Penalties'
                if odds(.5): # Figure it out later
                    home.score += 1
                else:
                    away.score += 1
    return [home, home.score, away.score, away, note]


def sharpness(offense, defense):
    OffenseScore = offense.qual[3] + \
        .33*(offense.qual[1] if offense.roles[1] in ['Overload', 'Long Ball'] else 0) + \
        (offense.qual[2] if offense.roles[2] in ['Quick', 'Crossing'] else 0) + \
        (offense.qual[3] if offense.roles[3] in ['Route 1', 'In Behind'] else 0) + \
        (.5*(offense.qual[2]+offense.qual[3]) if (offense.roles[2] == 'Quick' and offense.roles[3] == 'In Behind') or \
            (offense.roles[2] == 'Crossing' and offense.roles[3] == 'Route 1') else 0)
    DefenseScore = defense.qual[1] + \
        (defense.qual[0] if defense.roles[0] == 'Sweeper Keeper' else 0) + \
        (defense.qual[1] if defense.roles[1] == 'Low Block' else 0) + \
        (defense.qual[2] if defense.roles[2] == 'Holding' else 0) + \
        .5*(defense.qual[3] if defense.roles[3] == 'Holdup' else 0) 
    diff = OffenseScore - DefenseScore
    return clamp(.2 + (math.sqrt(diff) if diff >= 0 else -1*math.sqrt(abs(diff))) / 300, .05, .35)

def shot(offense, defense):
    OffenseScore = offense.qual[3] 
    DefenseScore = 3*(defense.qual[0] + .5*(defense.qual[0] if defense.roles[0] == 'Shot Stopper' else 0))
    diff = OffenseScore - DefenseScore
    return clamp(.33 + (math.sqrt(diff) if diff >= 0 else -1*math.sqrt(abs(diff))) / 100, .15, .5)

        
"""           
results = pandas.DataFrame(columns = ['hqual', 'htac', 'hscore', 'hGPM', 'aqual', 'atac', 'ascore', 'aGPM'])

for hqual in list(range(100)) * 4:
    if hqual % 10 == 0:
        print(hqual)
    #print()
    for aqual in list(range(100)) * 4:
        HOMETEAM = CLUB('TEAMA', 'AAA', hqual)
        AWAYTEAM = CLUB('TEAMB', 'BBB', aqual)
        HOMETEAM.rolesSet(seasonStart=True)
        AWAYTEAM.rolesSet(seasonStart=True)
        res = game(HOMETEAM, AWAYTEAM)
        results.loc[len(results)] = [hqual, HOMETEAM.tactic, res[1], res[4], aqual, AWAYTEAM.tactic, res[3], res[5]]
"""