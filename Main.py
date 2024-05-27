from UserPlay import *

ExtraGames = pandas.DataFrame({'TYPE':['ENG', 'ESP', 'GER', 'na'], 'GAMES':[3, 4, 2, 0]}).set_index('TYPE')

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

slot = input('INPUT NAME OF SAVE FILE (BLANK TO START NEW)')
if slot:
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



# TESTS
#for i in range(8):
#    for country in ALL:
#        country.playNext('C')
#EURO.setup(TIERA, TIERB, TIERC)
#EURO.playNext()
#EURO.playNext()

