from Game import *

RESULTS = pandas.DataFrame(columns = ['Year', 'Competition', 'Round', 'Home', 'HomeScore', 'AwayScore', 'Away', 'Notes'])
DIRECTORY = pandas.DataFrame(columns = ['Year', 'Association', 'League', 'Team', 'BaseRating'])
WINNERS = pandas.DataFrame(columns = ['Year', 'Competition', 'Team'])

class ASSOCIATION:
    def __init__(self, name, abr, leagues, relSpots, lastSpot):
        self.name = name
        self.abr = abr
        self.leagues = [LEAGUE(f'{self.name} League {div+1}', f'{self.abr}{div+1}', leagues[div], self) for div in range(len(leagues))]
        self.relSpots = relSpots
        self.last = lastSpot  # 'na' for straight up
        allteams = []
        for i in self.leagues:
            allteams += i.teams
        self.cup = CUP(f'{self.name} Cup', f'{self.abr}C', allteams)
        self.year = 1

    def playNext(self, comp, num=1): # num is round for cup and how many slates for league
        if comp in ['L', 'League', 'LEAGUE']:
            for i in range(num):
                for l in self.leagues:
                    try:
                        l.playNext()
                    except IndexError:
                        print(f'End of Season in {l.name}')
        else:
            self.cup.playNext(num)

    def endOfYear(self):
        if self.cup.fixtures.shape[1] != 1:
            raise ValueError('Cup isnt finished')
        if self.leagues[0].slate < len(self.leagues[0].schedule):
            raise ValueError('League isnt finished')
        # Start Europe
        """  
        totalspots = sum(self.euroSpots)
        cands = list(self.leagues[0].standings.index) # Top Flight Teams
        cup = self.cup.winners[0]
        CLspots = self.euroSpots[0]
        if cup not in cands[:CLspots]:
            try:
                cands.remove(cup)
            except ValueError:  # Cup winner not in top flight
                pass
            cands.insert(CLspots, cup)
        
        self.euroTeams = [
            cands[:CLspots],  # Champions League
            cands[CLspots:sum(self.euroSpots[0:2])],  # Europa League
            cands[sum(self.euroSpots[0:2]):totalspots],  # Conference League
            cands[totalspots:(totalspots+3)]  # Extra In case
        ]
        """
        #self.euroTeams = cands[:10]  # all in one list for backups
        # End Europe
        # RELEGATION
        if len(self.leagues) > 1: # i.e. relegation needs to happen
            for div in range(len(self.leagues)-1):
                upTeams = list(self.leagues[div].standings.index)
                relegated = upTeams[(len(upTeams)-self.relSpots[div]):]
                if self.last == 2:
                    try:
                        relegated.remove(self.leagues[div+1].playoffs.fixtures.Champion[0]) # 3rd last wins playoff
                    except ValueError:
                        pass
                survive = upTeams[:(len(upTeams)-self.relSpots[div])]
                downTeams = list(self.leagues[div+1].standings.index)
                if self.last != 'na':
                    promoted = downTeams[:(self.relSpots[div]-1)] + [self.leagues[div+1].playoffs.fixtures.Champion[0]]
                else:
                    promoted = downTeams[:self.relSpots[div]]
                stayDown = [team for team in downTeams if team not in promoted]
                self.leagues[div].seasonStart(survive + promoted)
                self.leagues[div+1].seasonStart(relegated + stayDown)
        else:
            self.leagues[0].seasonStart()
        # END RELEGATION
        self.year += 1
        allteams = []
        for i in self.leagues:
            allteams += i.teams
        for i in allteams:
            i.ratingAdjust()
            DIRECTORY.loc[len(DIRECTORY)] = [self.year, self.name, i.league.name, i.name, i.baserating]
        self.cup.seasonStart(allteams)

    def __str__(self):
        return self.name
    

class LEAGUE:
    def __init__(self, name, abr, teams, assoc = None):
        self.name = name
        self.abr = abr
        self.teams = teams
        self.assoc = assoc
        n = len(self.teams)
        self.standings = pandas.DataFrame({
            'Teams': self.teams,
            'Played': [0]*n,
            'Points': [0]*n,
            'Wins': [0]*n,
            'Draws': [0]*n,
            'Losses': [0]*n,
            'GoalDifference': [0]*n,
            'GoalsFor': [0]*n,
            'GoalsAgainst': [0]*n
        }).set_index('Teams')
        self.schedule = RoundRobin(list(self.standings.index), double=True)
        if len(self.teams) <= 12:
            self.schedule = self.schedule + RoundRobin(list(self.standings.index), double=True)
        self.slate = 0
        self.playoffs = None
        self.year = 1
        for i in self.teams:
            i.league = self
            DIRECTORY.loc[len(DIRECTORY)] = [self.year, self.assoc.name, self.name, i.name, i.baserating]
        self.out()

    def resultHandler(self, result):
        RESULTS.loc[len(RESULTS)] = [self.year, self.abr, self.slate+1]+result
        # Home
        self.standings.loc[result[0], 'Played'] += 1
        self.standings.loc[result[0], 'GoalDifference'] += result[1] - result[2]
        self.standings.loc[result[0], 'GoalsFor'] += result[1]
        self.standings.loc[result[0], 'GoalsAgainst'] += result[2]
        # Away
        self.standings.loc[result[3], 'Played'] += 1
        self.standings.loc[result[3], 'GoalDifference'] += result[2] - result[1]
        self.standings.loc[result[3], 'GoalsFor'] += result[2]
        self.standings.loc[result[3], 'GoalsAgainst'] += result[1]
        # Result
        if result[1] > result[2]:  # Home Win
            self.standings.loc[result[0], 'Wins'] += 1
            self.standings.loc[result[0], 'Points'] += 3
            self.standings.loc[result[3], 'Losses'] += 1
        elif result[2] > result[1]:  # Away Win
            self.standings.loc[result[3], 'Wins'] += 1
            self.standings.loc[result[3], 'Points'] += 3
            self.standings.loc[result[0], 'Losses'] += 1
        else:  # Draw
            self.standings.loc[result[0], 'Draws'] += 1
            self.standings.loc[result[0], 'Points'] += 1
            self.standings.loc[result[3], 'Draws'] += 1
            self.standings.loc[result[3], 'Points'] += 1

    def playNext(self):
        pause = False
        mydiv = self.assoc.leagues.index(self)
        if self.slate < len(self.schedule):
            for match in self.schedule[self.slate]:
                self.resultHandler(game(match[0], match[1]))
            self.standings.sort_values(['Points', 'GoalDifference', 'GoalsFor', 'Wins'], ascending = False, inplace = True)
            self.slate += 1
            self.out()
        if self.slate == len(self.schedule):
            WINNERS.loc[len(WINNERS)] = [self.year, self.abr, self.standings.index[0]]
        if self.slate == len(self.schedule) and self.assoc.last != 'na' and mydiv > 0:
            autospots = self.assoc.relSpots[mydiv - 1] - 1
            if self.assoc.last == 'ENG':
                self.playoffs = CUP(self.name + ' prom. playoffs', self.abr + 'P', \
                    teams = list(self.standings.index)[autospots:(autospots+4)], agg = True, finalagg = False)
            elif self.assoc.last == 'ESP':
                self.playoffs = CUP(self.name + ' prom. playoffs', self.abr + 'P', \
                    teams = list(self.standings.index)[autospots:(autospots+4)], agg = True, finalagg = True)
            elif self.assoc.last == 'GER':
                topTeam = self.assoc.leagues[mydiv-1].standings.index[len(self.assoc.leagues[mydiv-1].standings) - (autospots+1)]
                self.playoffs = CUP(self.name + ' prom. playoffs', self.abr + 'P', \
                    teams = [self.standings.index[autospots], topTeam], \
                    agg = True, finalagg = True)
            self.playoffs.year = self.year
            self.slate += 1
            pause = True
        elif self.slate == len(self.schedule):
            self.slate += 1
        if self.slate > len(self.schedule) and self.playoffs is not None and not pause:
            if self.assoc.last != 'na' and mydiv > 0:
                self.playoffs.playNext()
            else:
                pass

    def seasonStart(self, teams = None):
        if teams is not None:
            self.teams = teams
            for team in teams:
                team.league = self
        n = len(self.teams)
        self.standings = pandas.DataFrame({
            'Teams': self.teams,
            'Played': [0]*n,
            'Points': [0]*n,
            'Wins': [0]*n,
            'Draws': [0]*n,
            'Losses': [0]*n,
            'GoalDifference': [0]*n,
            'GoalsFor': [0]*n,
            'GoalsAgainst': [0]*n
        }).set_index('Teams')
        self.schedule = RoundRobin(list(self.standings.index), double=True)
        if len(self.teams) <= 12:
            self.schedule = self.schedule + RoundRobin(list(self.standings.index), double=True)
        self.playoffs = None
        if os.path.isfile(f'Output/{self.abr}PFixtures.csv'):
            os.remove(f'Output/{self.abr}PFixtures.csv')
        if self.slate > 0: # Basically, if it hasn't already been reset
            self.year += 1
        self.slate = 0
        self.out()

    def out(self):
        RESULTS.to_csv(f'Output/Results.csv', index = False)
        self.standings.reset_index().to_csv(f'Output/{self.abr}Standings.csv', index = False)

    def __str__(self):
        return self.name


class CUP:
    def __init__(self, name, abr, teams, agg = False, finalagg = False):
        self.name = name
        self.abr = abr
        self.teams = teams
        self.fixtures = None
        self.winners = None
        self.agg = agg
        self.finalagg = finalagg
        self.leg = 1
        self.aggholder = pandas.DataFrame(columns = ['Teams', 'Score']).set_index('Teams')
        getBye = 2*(2**math.floor(math.log(len(self.teams), 2))) - len(self.teams)
        if getBye == len(self.teams):
            draw = self.teams
            random.shuffle(draw)
            split = len(draw) // 2
            home = draw[:split]
            away = draw[split:]
            self.fixtures = pandas.DataFrame({'Home': home, 'Away': away})
        else:
            topdraw = self.teams[:getBye]
            bottomdraw = self.teams[getBye:]
            topfixtures = pandas.DataFrame({'Home': topdraw, 'Away': [None]*getBye})
            random.shuffle(bottomdraw)
            split = len(bottomdraw) // 2
            home = bottomdraw[:split]
            away = bottomdraw[split:]
            bottomfixtures = pandas.DataFrame({'Home': home, 'Away': away})
            self.fixtures = pandas.concat([topfixtures, bottomfixtures], ignore_index = True)
        self.year = 1
        self.out()

    def resultHandler(self, result, advance = True):
        if self.leg == 2:
            result[1] -= self.aggholder.loc[result[0]]
            result[2] -= self.aggholder.loc[result[3]]
            RESULTS.loc[len(RESULTS)] = [self.year, self.abr, f'{len(self.fixtures)*2}-{self.leg}']+result
        else:
            RESULTS.loc[len(RESULTS)] = [self.year, self.abr, f'{len(self.fixtures)*2}-{self.leg}']+result
        if advance:
            if result[2] == 'NA': # Home Bye
                self.winners.append(result[0])
            elif result[1] > result[2]: # Home Win
                self.winners.append(result[0])
            else:  # Away win, no draws
                self.winners.append(result[3])
        else:
            if result[2] != 'NA':
                self.aggholder.loc[result[0]] = [result[1]]
                self.aggholder.loc[result[3]] = [result[2]]

    def playNext(self, Round = 0):
        if len(self.fixtures) < Round: # Get the finals lined up
            return
        if self.fixtures.shape[1] == 1:
            print(f'{self.name} over')
            return
        self.winners = []
        matches = zip(self.fixtures.Home, self.fixtures.Away)
        if ((not self.agg) and len(self.fixtures) > 1) or ((not self.finalagg) and len(self.fixtures) == 1): # No Agg
            matches = zip(self.fixtures.Home, self.fixtures.Away)
            if len(self.fixtures) == 1: # Final at neutral site
                self.resultHandler(game(self.fixtures.Home[0], self.fixtures.Away[0], ET=True, neutral = True))
            else:
                for match in matches:
                    if match[1] is None:
                        self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'])
                    else:
                        self.resultHandler(game(match[0], match[1], ET=True))
        elif self.leg == 1: # First leg
            self.aggholder = pandas.DataFrame(columns = ['Teams', 'Score']).set_index('Teams')
            for match in matches:
                if match[1] is None:
                    self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'], advance=False)
                else:
                    self.resultHandler(game(match[1], match[0]), advance=False) # Away hosts the first leg
            self.leg = 2
        else:  # Second Leg
            for match in matches:
                if match[1] is None:
                    self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'], advance=True)
                else:
                    self.resultHandler(game(match[0], match[1], ET = True, 
                    agg = [self.aggholder.loc[match[0], 'Score'], self.aggholder.loc[match[1], 'Score']]), advance=True)
            self.leg = 1
        if len(self.winners) > 1:
            random.shuffle(self.winners)
            split = len(self.winners) // 2
            home = self.winners[:split]
            away = self.winners[split:]
            self.fixtures = pandas.DataFrame({'Home': home, 'Away': away})
        elif len(self.winners) == 1:
            self.fixtures = pandas.DataFrame({'Champion': [self.winners[0]]})
            WINNERS.loc[len(WINNERS)] = [self.year, self.abr, self.winners[0]]
        self.out()

    def seasonStart(self, teams):
        if teams is not None:
            self.teams = teams
        self.fixtures = None
        self.winners = None
        getBye = 2*(2**math.floor(math.log(len(self.teams), 2))) - len(self.teams)
        if getBye == len(self.teams):
            draw = self.teams
            random.shuffle(draw)
            split = len(draw) // 2
            home = draw[:split]
            away = draw[split:]
            self.fixtures = pandas.DataFrame({'Home': home, 'Away': away})
        else:
            topdraw = self.teams[:getBye]
            bottomdraw = self.teams[getBye:]
            topfixtures = pandas.DataFrame({'Home': topdraw, 'Away': [None]*getBye})
            random.shuffle(bottomdraw)
            split = len(bottomdraw) // 2
            home = bottomdraw[:split]
            away = bottomdraw[split:]
            bottomfixtures = pandas.DataFrame({'Home': home, 'Away': away})
            self.fixtures = pandas.concat([topfixtures, bottomfixtures], ignore_index = True)
        self.year += 1
        self.out()

    def __str__(self):
        return self.name


    def out(self):
        RESULTS.to_csv(f'Output/Results.csv', index=False)
        self.fixtures.to_csv(f'Output/{self.abr}Fixtures.csv', index=False)
        
class EUhelper:
    def __init__(self, assoc, teams, cup):
        self.teams = teams
        self.assoc = assoc
        self.cup = cup
        self.chosen = []

    def pop(self):
        team = self.teams[0]
        self.chosen.append(team)
        self.teams = self.teams[1:]
        return team

    def remove(self, team):
        if team in self.teams:
            self.teams.remove(team)
            self.chosen.append(team)

class EUROPE:
    def __init__(self):
        self.pastCL = None
        self.pastEL = None
        self.cupWinners = []
        self.CLteams = [[], [], [], []]
        self.ELteams = [[], [], [], []]
        self.ECteams = [[], [], [], []]
        self.CLplayin = []
        self.ELplayin = [[], []]
        self.ECplayin = [[], []]
        self.holder = []
        self.Ateams = {}
        self.Bteams = {}
        self.Cteams = {}

    def setup(self, As, Bs, Cs):
        A = [EUhelper(x, list(x.leagues[0].standings.index[:11]), x.cup.winners[0]) for x in As]
        B = [EUhelper(x, list(x.leagues[0].standings.index[:11]), x.cup.winners[0]) for x in Bs]
        C = [EUhelper(x, list(x.leagues[0].standings.index[:11]), x.cup.winners[0]) for x in Cs]
        for i in A + B + C:
            i.remove(self.pastCL)
            i.remove(self.pastEL)
        self.CLteams[0] = [self.pastCL, self.pastEL] + [x.pop() for x in A+B]
        C1s = sorted([x.pop() for x in C], key = lambda x: x.baserating, reverse = True)
        self.CLteams[1] = C1s[:2] + [x.pop() for x in A+B]
        self.CLteams[2] = C1s[2:]
        self.CLteams[3] = [x.pop() for x in A] + ([numpy.nan] * 4)
        CLP = sorted([x.pop() for x in A], key = lambda x: x.baserating, reverse = True) + \
            sorted([x.pop() for x in B], key = lambda x: x.baserating, reverse = True) + \
            sorted([x.pop() for x in C], key = lambda x: x.baserating, reverse = True)
        self.CLplayin = [[CLP[0], CLP[15], CLP[7], CLP[8]],
                        [CLP[1], CLP[14], CLP[6], CLP[9]],
                        [CLP[2], CLP[13], CLP[4], CLP[10]],
                        [CLP[3], CLP[12], CLP[4], CLP[11]]]






           

        


        