from UserPlay import *


TIERA = [ENGLAND, SPAIN, GERMANY, ITALY]
TIERB = [FRANCE, PORTUGAL]
TIERC = [NETHERLANDS, SCOTLAND, GREECE, TURKIYE, BELGIUM, 
    DENMARK, SWITZERLAND, AUSTRIA, CROATIA, CZECHIA]
ALL = TIERA + TIERB + TIERC
EURO = EUROPE()
EURO.pastCL = ENG1[0]
EURO.pastEL = ESP1[12]
DIRECTORY.to_csv('Output/Directory.csv', index=False)
WINNERS.to_csv('Output/Winners.csv', index=False)
EURO.setup(TIERA, TIERB, TIERC)

class handler:
    def __init__(self):
        # 50 Leagues, 7 Cup, 21 EURO
        self.league = 0
        self.cup = 128
        self.euro = 0
        #self.slates  = ['Cup' if ((i+1) % 11) == 0 else 'Euro' if ((i+1) % 3) == 0 and not 45 < i < 55 else 'League' for i in range(78)]
        self.slates = ['Cup' if ((i+3) % 11) == 0 else 'Euro' if ((i-0) % 3) == 0 and not 31 < i < 46 else 'League' for i in range(76)]
        self.overall = 0
    
    def __str__(self):
        return f'LEAGUE: {self.league}, CUP: {self.cup}, EURO: {self.euro}'

    def reset(self):
        self.league = 0
        self.cup = 128
        self.euro = 0
        self.overall = 0
glob = handler()

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
        ass.cup.out()
        for lea in ass.leagues:
            lea.out()
    outs = pandas.DataFrame(os.listdir('Output'))
    outs = outs[outs[0].str.startswith(('ECP', 'ELP', 'CLP'))][0].tolist()
    outs
    #print(outs)
    #print(EURO)
    for i in outs:
        os.remove(f'Output/{i}')
    #print(EURO)
    EURO.out()
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
def playNextAll():
    if glob.overall == len(glob.slates):
        print('No games left')
        return
    if glob.slates[glob.overall] == 'League':
        glob.league += 1
        for assoc in ALL:
            for level in range(len(assoc.leagues)):
                league = assoc.leagues[level]
                if (glob.league / 50) > (league.slate / (len(league.schedule) + (ExtraGames.loc[assoc.last, 'GAMES'] if level > 0 else 0))):
                    league.playNext()
    elif glob.slates[glob.overall] == 'Cup':
        #print('here')
        glob.cup = glob.cup // 2
        for assoc in ALL:
            assoc.cup.playNext(glob.cup)
    else:
        glob.euro += 1
        EURO.playNext()
    glob.overall += 1
    if glob.overall == len(glob.slates):
        print('SEASON OVER')

def yearReset():
    EURO.setup(TIERA, TIERB, TIERC)
    for assoc in ALL:
        assoc.endOfYear()
    glob.reset()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)

def playNextUser():
    playNextAll()
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
