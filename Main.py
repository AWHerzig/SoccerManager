from Clubs import *

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

class handler:
    def __init__(self):
        # 50 Leagues, 7 Cup, 21 EURO
        self.league = 0
        self.cup = 128
        self.euro = 0
        self.slates  = ['Cup' if ((i+1) % 11) == 0 else 'Euro' if ((i+1) % 3) == 0 and not 45 < i < 55 else 'League' for i in range(78)]
        self.overall = 0
    
    def __str__(self):
        return f'LEAGUE: {self.league}, CUP: {self.cup}, EURO: {self.euro}'
glob = handler()

def playNext():
    if glob.overall == len(self.slates):
        print('No games left')
        return
    if glob.slates[glob.overall] == 'League':
        glob.league += 1
        for assoc in ALL:
            for level in range(len(assoc.leagues)):
                league = assoc.leagues[level]
                if (glob.league / 50) > (league.slate / (len(league.schedule) + (ExtraGames.loc[assoc.last, 'GAMES'] if level > 0 else 0))):
                    league.playNext(1)
    elif glob.slates[glob.overall] == 'Cup':
        glob.cup == glob.cup // 2
        for assoc in ALL:
            assoc.cup.playNext(glob.cup)
    else:
        if ENGLAND.leagues[0].year == 1:  # SOmething with europes
            pass
    glob.overall += 1
    if glob.overall == len(self.slates):
        print('SEASON OVER')

def yearReset():
    EURO.setup(TIERA, TIERB, TIERC)
    for assoc in ALL:
        assoc.endOfYear()
    DIRECTORY.to_csv('Output/Directory.csv', index=False)
    WINNERS.to_csv('Output/Winners.csv', index=False)



