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

def standingsShower(table, main, ALL, EURO):
    bs = [Box('MENU', [20, 100, 600, 680], main.goto)]
    texts = []
    surfaces = []
    if isinstance(table, str): # EURO
        bs.append(Box('OTHER LEAGUES', [20, 100, 500, 580], lambda: standingsShower(None, main, ALL, EURO).goto()))
        if EURO.slate <= 4: # Playin
            clp = [cup.fixtures.copy(deep=True) for cup in EURO.CLplayin.cups]
            elp = [cup.fixtures.copy(deep=True) for cup in EURO.ELplayin.cups]
            ecp = [cup.fixtures.copy(deep=True) for cup in EURO.ECplayin.cups]
            for i in range(len(clp)):
                clp[i]['Competition'] = ['CL' for j in clp[i].Home]
                clp[i]['Path'] = [i + 1 for j in clp[i].Home]
            for i in range(len(elp)):
                elp[i]['Competition'] = ['EL' for j in elp[i].Home]
                elp[i]['Path'] = [i + 1 for j in elp[i].Home]
            for i in range(len(ecp)):
                ecp[i]['Competition'] = ['EC' for j in ecp[i].Home]
                ecp[i]['Path'] = [i + 1 for j in ecp[i].Home]
            tot = pandas.concat([cup for cup in clp + elp + ecp])[['Competition', 'Path', 'Home', 'Away']]
            tot.Home = tot.Home.apply(nameShorten)
            tot.Away = tot.Away.apply(nameShorten)
            cla = pandas.DataFrame({'Competition': ['CL']*32, 'Path': ['Advanced']*32, 'Home': listMergr(EURO.CLteams), 'Away': ['']*32})
            ela = pandas.DataFrame({'Competition': ['EL']*32, 'Path': ['Advanced']*32, 'Home': listMergr(EURO.ELteams), 'Away': ['']*32})
            eca = pandas.DataFrame({'Competition': ['EC']*32, 'Path': ['Advanced']*32, 'Home': listMergr(EURO.ECteams), 'Away': ['']*32})
            adv = pandas.concat([cla, ela, eca])
            out = pandas.concat([tot, adv[adv.Home.apply(lambda x: x is not None)]])
            surfaces.append([out, 200, 0])
        elif EURO.slate <= 10: # Groups
            clp = [group.standings.copy(deep=True) for group in EURO.CLteams]
            elp = [group.standings.copy(deep=True) for group in EURO.ELteams]
            ecp = [group.standings.copy(deep=True) for group in EURO.ECteams]
            for i in range(len(clp)):
                clp[i]['Competition'] = ['CL' for j in clp[i].index]
                clp[i]['Path'] = [i + 1 for j in clp[i].index]
            for i in range(len(elp)):
                elp[i]['Competition'] = ['EL' for j in elp[i].index]
                elp[i]['Path'] = [i + 1 for j in elp[i].index]
            for i in range(len(ecp)):
                ecp[i]['Competition'] = ['EC' for j in ecp[i].index]
                ecp[i]['Path'] = [i + 1 for j in ecp[i].index]
            tot = pandas.concat([cup for cup in clp + elp + ecp]).reset_index()\
                [['Competition', 'Path', 'Teams', 'Played', 'Points', 'GoalDifference']]
            tot.Teams = tot.Teams.apply(nameShorten)
            surfaces.append([tot, 200, 0])
        else: # Knockout
            clp =  EURO.CLteams.fixtures.copy(deep=True)
            elp = EURO.ELteams.fixtures.copy(deep=True)
            ecp = EURO.ECteams.fixtures.copy(deep=True)
            clp['Competition'] = ['CL' for j in clp.Home]
            elp['Competition'] = ['EL' for j in elp.Home]
            ecp['Competition'] = ['EC' for j in ecp.Home]
            tot = pandas.concat([clp, elp, ecp]).reset_index()\
                [['Competition', 'Home', 'Away']]
            tot.Home = tot.Home.apply(nameShorten)
            tot.Away = tot.Away.apply(nameShorten)
            surfaces.append([tot, 200, 0])
    elif isinstance(table, CUP): # DOMESTIC CUP
        tot = table.fixtures.copy(deep = True)
        tot.Home = tot.Home.apply(nameShorten)
        tot.Away = tot.Away.apply(nameShorten)
        surfaces.append([tot, 200, 0])
        bs.append(Box('OTHER LEAGUES', [20, 100, 500, 580], lambda: standingsShower(None, main, ALL, EURO).goto()))
    elif table is not None: # LEAGUE
        df = table.standings[['Played', 'Points', 'GoalDifference', 'Wins', 'Draws', 'Losses']].reset_index().\
            rename(columns = {'indexx': 'Teams', 'Played': 'P', 'Points': 'PTS', 'GoalDifference':'GD', 'Wins':'W', 'Draws':'D', 'Losses':'L'})
        df.Teams = df.Teams.apply(nameShorten)
        bs.append(Box('OTHER LEAGUES', [20, 100, 500, 580], lambda: standingsShower(None, main, ALL, EURO).goto()))
        surfaces.append([df, 200, 0])
    else: # STANDINGS MENU
        bList =  [Box(ALL[i].name, [50 + 300*(i//4), 250 + 300*(i//4), 125 + 150*(i%4), 225 + 150*(i%4)], ALL[i]) for i in range(16)]
        bList.append(Box('EURO', [25, 125, 50, 100]))
        leaguescreen = Screen(bList, [('SELECT ASSOCIATION TO VIEW', (600, 100), 40)])
        LeaguePick = leaguescreen.goto()
        if isinstance(LeaguePick, str):
            standingsShower('EURO', main, ALL, EURO).goto()
        else:
            bList =  [Box(LeaguePick.leagues[i].name, [50 + 600*(i//2), 550 + 600*(i//2), 125 + 275*(i%2), 350 + 275*(i%2)], LeaguePick.leagues[i]) for i in range(len(LeaguePick.leagues))]
            bList.append(Box('CUP', [25, 125, 50, 100], LeaguePick.cup)) 
            DivPick = Screen(bList, [('SELECT LEAGUE TO VIEW', (600, 100), 40)]).goto()
            standingsShower(DivPick, main, ALL, EURO).goto()
    return Screen(bs, texts, surfaces, spot = 'midleft')

def scheduleShower(team, main, ALL, glob, EURO):
    bs = [Box('MENU', [20, 100, 600, 680], main.goto)]
    texts = [] 
    surfaces = []
    if team is not None:
        bs.append(Box('OTHER LEAGUES', [20, 100, 500, 580], lambda: scheduleShower(None, main, ALL, glob, EURO).goto()))
        surfaces.append([scheduleLister(team, glob, EURO), 200, 0])
    else:
        bList =  [Box(ALL[i].name, [50 + 300*(i//4), 250 + 300*(i//4), 125 + 150*(i%4), 225 + 150*(i%4)], ALL[i]) for i in range(16)]
        leaguescreen = Screen(bList, [('SELECT ASSOCIATION TO VIEW', (600, 100), 40)])
        LeaguePick = leaguescreen.goto()
        if len(LeaguePick.leagues) == 1:
            DivPick = LeaguePick.leagues[0]
        else:
            bList =  [Box(LeaguePick.leagues[i].name, [50 + 600*(i//2), 550 + 600*(i//2), 125 + 275*(i%2), 350 + 275*(i%2)], LeaguePick.leagues[i]) for i in range(len(LeaguePick.leagues))]
            DivPick = Screen(bList, [('SELECT LEAGUE TO VIEW', (600, 100), 40)]).goto()
        bList = [Box(f"{DivPick.teams[i].name} {round(DivPick.teams[i].baserating / 11)}", [50 + 300*(i//4), 250 + 300*(i//4), 125 + 120*(i%4), 265 + 120*(i%4)], DivPick.teams[i]) for i in range(len(DivPick.teams))]
        TeamPick = Screen(bList, [('SELECT TEAM TO VIEW', (600, 100), 40)]).goto()
        scheduleShower(TeamPick, main, ALL, glob, EURO).goto()
    return Screen(bs, texts, surfaces, spot = 'midleft')



def dfout(df, x, y):
    texts = []   
    #print(df) 
    strings = dataframe_to_aligned_strings_with_headers(df)
    for i in range(len(strings)):
        texts.append((strings[i], (x, y + 20*i), 20))
    return texts


