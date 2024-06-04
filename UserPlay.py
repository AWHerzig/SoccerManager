from Clubs import *


def TakeControl(club):
    club.user = True
    base = club.baserating / 11
    club.squadGK  = [GK(base), GK(base-10), GK(base - 20)]
    club.squadDEF = [DEF(base) for i in range(5)] + [DEF(base - 10) for i in range(5)]
    club.squadMID = [MID(base) for i in range(5)] + [MID(base - 10) for i in range(5)]
    club.squadATT = [ATT(base) for i in range(4)] + [ATT(base - 10) for i in range(4)]

def overwrite():
    return True

def SaveGame_Standard(slot, glob, EURO):
    savepath = f'SAVE_{slot}.dill'
    if os.path.exists(savepath):
        if overwrite():
            os.remove(savepath)
    with open(f'SAVE_{slot}.dill', 'wb') as f:
        dill.dump((ENGLAND, SPAIN, GERMANY, ITALY, \
            FRANCE, PORTUGAL, NETHERLANDS, SCOTLAND, \
            GREECE, TURKIYE, BELGIUM, DENMARK, \
            SWITZERLAND, AUSTRIA, CROATIA, CZECHIA, \
            EURO, glob, RESULTS, DIRECTORY, WINNERS), f)


def RosterScreenBuilder(club, main):
    back = Box('MENU', [20, 100, 600, 680], main.goto)
    buy = Box('BUY', [150, 230, 600, 680], 'na')
    sell = Box('SELL', [250, 330, 600, 680], 'na')
    texts = []
    texts.append(('GOALKEEPERS', (300, 25), 40))
    for gkind in range(len(club.squadGK)):
        gk = club.squadGK[gkind]
        texts.append((gk.name, (175 + 285*(gkind%2), 50 + 70*(gkind//2)), 15))
        texts.append((gk.stats(), (175 + 285*(gkind%2), 70 + 70*(gkind//2)), 15))
        texts.append((gk.info(), (175 + 285*(gkind%2), 90 + 70*(gkind//2)), 15))
    texts.append(('DEFENDERS', (900, 25), 40))
    for dfind in range(len(club.squadDEF)):
        df = club.squadDEF[gkind]
        texts.append((df.name, (780 + 260*(dfind%2), 50 + 70*(dfind//2)), 15))
        texts.append((df.stats(), (780 + 260*(dfind%2), 70 + 70*(dfind//2)), 15))
        texts.append((df.info(), (780 + 260*(dfind%2), 90 + 70*(dfind//2)), 15))
    texts.append(('MIDFIELDERS', (300, 200), 40))
    for mdind in range(len(club.squadMID)):
        md = club.squadMID[mdind]
        texts.append((md.name, (175 + 285*(mdind%2), 225 + 70*(mdind//2)), 15))
        texts.append((md.stats(), (175 + 285*(mdind%2), 245 + 70*(mdind//2)), 15))
        texts.append((md.info(), (175 + 285*(mdind%2), 265 + 70*(mdind//2)), 15))
    texts.append(('ATTACKERS', (900, 405), 40))
    for atind in range(len(club.squadATT)):
        at = club.squadATT[atind]
        texts.append((at.name, (780 + 260*(atind%2), 430 + 70*(atind//2)), 15))
        texts.append((at.stats(), (780 + 260*(atind%2), 450 + 70*(atind//2)), 15))
        texts.append((at.info(), (780 + 260*(atind%2), 470 + 70*(atind//2)), 15))
    return Screen([back, buy, sell], texts)

def standingsShower(table, main, ALL):
    bs = [Box('MENU', [20, 100, 600, 680], main.goto)]
    texts = []
    if table is not None:
        bs.append(Box('OTHER LEAGUES', [20, 100, 500, 580], lambda: standingsShower(None, main, ALL).goto()))
        texts = texts + dfout(table, 600, 100)
    else:
        bList =  [Box(ALL[i].name, [50 + 300*(i//4), 250 + 300*(i//4), 125 + 150*(i%4), 225 + 150*(i%4)], ALL[i]) for i in range(16)]
        leaguescreen = Screen(bList, [('SELECT ASSOCIATION TO VIEW', (600, 100), 40)])
        LeaguePick = leaguescreen.goto()
        if len(LeaguePick.leagues) == 1:
            DivPick = LeaguePick.leagues[0]
        else:
            bList =  [Box(LeaguePick.leagues[i].name, [50 + 600*(i//2), 550 + 600*(i//2), 125 + 275*(i%2), 350 + 275*(i%2)], LeaguePick.leagues[i]) for i in range(len(LeaguePick.leagues))]
            DivPick = Screen(bList, [('SELECT LEAGUE TO VIEW', (600, 100), 40)]).goto()
        standingsShower(DivPick.standings, main, ALL).goto()
    return Screen(bs, texts)



def dfout(table, x, y, size = 'big'):
    texts = []
    #texts.append((f'PLAYED: table.iloc[0, 0]', (x, y), 40))
    #y += 25
    if size == 'big':
        df = table[['Played', 'Points', 'GoalDifference', 'Wins', 'Draws', 'Losses']].reset_index().\
            rename(columns = {'indexx': 'Teams', 'Played': 'P', 'Points': 'PTS', 'GoalDifference':'GD', 'Wins':'W', 'Draws':'D', 'Losses':'L'})
    else:
        df = table[['Played', 'Points', 'GoalDifference']].reset_index().\
            rename(columns = {'index': 'Teams', 'Played': 'P', 'Points': 'PTS', 'GoalDifference':'GD'})
    texts.append((strViaList(list(df.columns), '#'), (x, y), 20))   
    #print(df) 
    for i in range(len(df)):
        texts.append((strViaList(df.iloc[i].to_list(), df.loc[i, 'Teams'].league.standings.index.to_list().index(df.loc[i, 'Teams'])+1), (x, y + 20*(i+1)), 20))
    return texts
    


