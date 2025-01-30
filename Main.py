from UserPlay import *


if DLeague:
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)
else:
    TIERA = [ENGLAND, SPAIN, GERMANY, ITALY]
    TIERB = [FRANCE, PORTUGAL]
    TIERC = [NETHERLANDS, SCOTLAND, GREECE, TURKIYE, BELGIUM, 
        DENMARK, SWITZERLAND, AUSTRIA, CROATIA, CZECHIA]
    ALL = TIERA + TIERB + TIERC
    if not fromSave:
        EURO = EUROPE()
        EURO.pastCL = ESP1[0]
        EURO.pastEL = ITA1[1]
        EURO.setup(TIERA, TIERB, TIERC)
        glob = handler()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)





# LOAD SAVE
"""
x = pandas.DataFrame(os.listdir())
saves = [None]*16
real = x[x[0].str.contains('.dill')][0].to_list()
saves[:len(real)] = real
bList = [Box(saves[i][5:-5] if saves[i] is not None else '<NEW GAME>', [50 + 300*(i//4), 250 + 300*(i//4), 125 + 150*(i%4), 225 + 150*(i%4)]) for i in range(16)]
slotscreen = Screen(bList, [('SELECT GAME MODE', (600, 100), 40)])
slot = slotscreen.goto()
MyClub = None
#slot = input('INPUT NAME OF SAVE FILE (BLANK TO START NEW)')
if slot != '<NEW GAME>':
    print(slot)
    with open(f'SAVE_{slot}.dill', 'rb') as f:
        ENGLAND, SPAIN, GERMANY, ITALY, \
            FRANCE, PORTUGAL, NETHERLANDS, SCOTLAND, \
            GREECE, TURKIYE, BELGIUM, DENMARK, \
            SWITZERLAND, AUSTRIA, CROATIA, CZECHIA, \
            EURO, glob, RESULTS, DIRECTORY, WINNERS = dill.load(f)
    #print(EURO)
    TIERA = [ENGLAND, SPAIN, GERMANY, ITALY]
    TIERB = [FRANCE, PORTUGAL]
    TIERC = [NETHERLANDS, SCOTLAND, GREECE, TURKIYE, BELGIUM, 
        DENMARK, SWITZERLAND, AUSTRIA, CROATIA, CZECHIA]
    ALL = TIERA + TIERB + TIERC
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)
    RESULTS.to_csv('Output/Results.csv', index=False)
    for ass in ALL:
        ass.cup.out(RESULTS)
        for lea in ass.leagues:
            lea.out(RESULTS)
    outs = pandas.DataFrame(os.listdir('Output'))
    outs = outs[outs[0].str.startswith(('ECP', 'ELP', 'CLP'))][0].tolist()
    outs
    #print(outs)
    #print(EURO)
    for i in outs:
        os.remove(f'Output/{i}')
    #print(EURO)
    EURO.out(RESULTS)
#standingsDisplayer(out, [ENGLAND.leagues[0].standings])
elif mode == 'Manager Mode':
    bList =  [Box(ALL[i].name, [50 + 300*(i//4), 250 + 300*(i//4), 125 + 150*(i%4), 225 + 150*(i%4)], ALL[i]) for i in range(16)]
    leaguescreen = Screen(bList, [('SELECT ASSOCIATION TO PLAY IN', (600, 100), 40)])
    LeaguePick = leaguescreen.goto()
    if len(LeaguePick.leagues) == 1:
        DivPick = LeaguePick.leagues[0]
    else:
        bList =  [Box(LeaguePick.leagues[i].name, [50 + 600*(i//2), 550 + 600*(i//2), 125 + 275*(i%2), 350 + 275*(i%2)], LeaguePick.leagues[i]) for i in range(len(LeaguePick.leagues))]
        DivPick = Screen(bList, [('SELECT LEAGUE TO PLAY IN', (600, 100), 40)]).goto()
    bList =  [Box(f"{DivPick.teams[i].name} {round(DivPick.teams[i].baserating / 11)}", [50 + 300*(i//4), 250 + 300*(i//4), 125 + 120*(i%4), 265 + 120*(i%4)], DivPick.teams[i]) for i in range(len(DivPick.teams))]
    MyClub = Screen(bList, [('SELECT YOUR CLUB', (600, 100), 40)]).goto()
    TakeControl(MyClub)
"""
def getNextSchedule(ALL, glob, EURO, spec = None):
    if glob.overall == len(glob.slates):
        print('No games left')
        return
    print('SLATE TYPE:', glob.slates[glob.overall])
    if glob.slates[glob.overall] == 'League':
        for assoc in ALL:
            for level in range(len(assoc.leagues)):
                league = assoc.leagues[level]
                if (glob.league+1 / 50) > (league.slate / (len(league.schedule) + (ExtraGames.loc[assoc.last, 'GAMES'] if level > 0 else 0))):
                    if spec is not None:
                        if league != spec:
                            continue
                    print(league.name)
                    if league.slate < len(league.schedule):
                        for i in league.schedule[league.slate]:
                            a = f'{i[0]} ({league.standings.loc[i[0]].Points} pts, #{list(league.standings.index).index(i[0]) + 1} in {league.abr})'
                            b = f'{i[1]} ({league.standings.loc[i[1]].Points} pts, #{list(league.standings.index).index(i[1]) + 1} in {league.abr})'
                            print(a, '  vs.  ', b)
                    else:
                        c = league.playoffs
                        if c is None:
                            continue
                        matches = zip(c.fixtures.Home, c.fixtures.Away)
                        for i in matches:
                            if len(c.aggholder) == 0 or i[0] is None or i[1] is None:
                                a = f'{i[0]}'
                                b = f'{i[1]}'
                                print(a, '  vs.  ', b)
                            else: 
                                a = f'{i[0]} ({c.aggholder.loc[i[0]].Score})'
                                b = f'{i[1]} ({c.aggholder.loc[i[1]].Score})'
                                print(b, '  vs.  ', a)
    elif glob.slates[glob.overall] == 'Cup':
        #print('here')
        for assoc in ALL:
            c = assoc.cup
            if spec is not None:
                if c != spec:
                    continue
            if len(c.fixtures) < glob.cup // 2: # Get the finals lined up
                continue
            print(c.name)
            matches = zip(c.fixtures.Home, c.fixtures.Away)
            for i in matches:
                a = f'{i[0]}'
                b = f'{i[1]}'
                print(a, '  vs.  ', b)
    else:
        if glob.euro < 4:
            all = EURO.CLplayin.cups + EURO.ELplayin.cups + EURO.ECplayin.cups if glob.euro in [2, 3] else \
                EURO.CLplayin.cups + EURO.ELplayin.cups
            for c in all:
                if spec is not None:
                    if c not in spec:
                        continue
                print(c.name)
                matches = zip(c.fixtures.Home, c.fixtures.Away)
                for i in matches:
                    if len(c.aggholder) == 0 or i[0] is None or i[1] is None:
                        a = f'{i[0]}'
                        b = f'{i[1]}'
                        print(a, '  vs.  ', b)
                    else: 
                        a = f'{i[0]} ({c.aggholder.loc[i[0]].Score})'
                        b = f'{i[1]} ({c.aggholder.loc[i[1]].Score})'
                        print(b, '  vs.  ', a)
        elif glob.euro < 10:
            all = EURO.CLteams + EURO.ELteams + EURO.ECteams
            for league in all:
                if spec is not None:
                    if league not in spec:
                        continue
                print(league.name)
                for i in league.schedule[league.slate]:
                    a = f'{i[0]} ({league.standings.loc[i[0]].Points} pts, #{list(league.standings.index).index(i[0]) + 1} in {league.abr})'
                    b = f'{i[1]} ({league.standings.loc[i[1]].Points} pts, #{list(league.standings.index).index(i[1]) + 1} in {league.abr})'
                    print(a, '  vs.  ', b)
        else:
            all = [EURO.ELteams, EURO.ECteams] if glob.euro in [10, 11] else \
                [EURO.CLteams, EURO.ELteams, EURO.ECteams]
            for c in all:
                if spec is not None:
                    if c not in spec:
                        continue
                print(c.name)
                matches = zip(c.fixtures.Home, c.fixtures.Away)
                for i in matches:
                    if len(c.aggholder) == 0 or i[0] is None or i[1] is None:
                        a = f'{i[0]}'
                        b = f'{i[1]}'
                        print(a, '  vs.  ', b)
                    else: 
                        a = f'{i[0]} ({c.aggholder.loc[i[0]].Score})'
                        b = f'{i[1]} ({c.aggholder.loc[i[1]].Score})'
                        print(b, '  vs.  ', a)

def playNextAll(ALL, glob, EURO, RESULTS, times = 1):
    for i in range(times):
        if glob.overall == len(glob.slates):
            print('No games left')
            return
        if glob.slates[glob.overall] == 'League':
            glob.league += 1
            for assoc in ALL:
                for level in range(len(assoc.leagues)):
                    league = assoc.leagues[level]
                    if (glob.league / 50) > (league.slate / (len(league.schedule) + (ExtraGames.loc[assoc.last, 'GAMES'] if level > 0 or assoc.last == 'GER' else 0))):
                        league.playNext(RESULTS)
        elif glob.slates[glob.overall] == 'Cup':
            #print('here')
            glob.cup = glob.cup // 2
            for assoc in ALL:
                assoc.cup.playNext(RESULTS, glob.cup)
        else:
            glob.euro += 1
            EURO.playNext(RESULTS)
        glob.overall += 1
        RESULTS.to_csv('Output/Results.csv')
        if glob.overall == len(glob.slates):
            print('SEASON OVER')

def yearReset(ALL, glob, EURO, DIRECTORY):
    EURO.setup(TIERA, TIERB, TIERC)
    for assoc in ALL:
        assoc.endOfYear(DIRECTORY)
    glob.reset()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)

def playNextUser():
    playNextAll(RESULTS)
    restartMenu()

def buildMainMenu():
    mm = Screen([], [])
    mm.boxes.append(Box('Quit', [100, 200, 50, 100], pygame.display.quit))
    mm.boxes.append(Box('My ROSTER', [650, 1100, 150, 300], RosterScreenBuilder(MyClub, mm).goto))
    mm.boxes.append(Box('ADVANCE SEASON', [100, 550, 150, 300], playNextUser)) # Add to this
    if MyClub is not None:
        ind = list(MyClub.league.standings.index).index(MyClub)
        minitable = MyClub.league.standings.iloc[max(ind-2, 0):min(ind+3, len(MyClub.league.standings))][['Played', 'Points', 'GoalDifference']].reset_index().\
                rename(columns = {'index': 'Teams', 'Played': 'P', 'Points': 'PTS', 'GoalDifference':'GD'})
        mm.boxes.append(Box(dfout(minitable, 925, 450), [650, 1100, 400, 650], standingsShower(MyClub.league, mm, ALL, EURO).goto))
    else:
        mm.boxes.append(Box('STANDINGS', [650, 1100, 400, 650], standingsShower(None, mm, ALL, EURO).goto))
    if MyClub is not None:
        x = scheduleLister(MyClub, glob, EURO)
        minitable = x[x.Location.isin(['AWAY', 'HOME', 'NEUTRAL'])].iloc[:5][['Competition', 'Location', 'Opponent']]
        mm.boxes.append(Box(dfout(minitable, 350, 450), [100, 550, 400, 650], scheduleShower(MyClub, mm, ALL, glob, EURO).goto))
    else:
        mm.boxes.append(Box('SCHEDULE', [100, 550, 400, 650], scheduleShower(None, mm, ALL, glob, EURO).goto))
    return mm

#MainMenu = buildMainMenu()

def restartMenu():
    pygame.init()
    out = pygame.display.set_mode(screen)
    pygame.display.set_caption('HERZIG SOCCER')
    buildMainMenu().goto()

#MainMenu.goto() # Removing this whole thing
# TESTS
#for i in range(8):
#    for country in ALL:
#        country.playNext('C')
#EURO.setup(TIERA, TIERB, TIERC)
#EURO.playNext()
#EURO.playNext()
