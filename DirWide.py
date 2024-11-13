import pygame
import numpy
import pandas
import random
import math
import names
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import os
import shutil
import dill
import statistics as stats
import inspect
def patch_asscalar(a):
    return a.item()
setattr(numpy, "asscalar", patch_asscalar)  # I have no damn idea, I stole this from internet since colormath is broken with new numpy.

global leaguePick 

screen = (1200, 700)
space, underscore = ' ', '_'
playerRadius = 20
legRadius = 10
ballRadius = 10
grav = .2

split = 10
floorHeight = 50
goalHeight = 200
floorToCeil = 500

bodyPower = 2
legPower = 6
bothPower = 10
speedMult = 2
jumpV = 5


WhiteC = (250, 250, 250)
BlackC = (0, 0, 0)
RedC = (148, 10, 13)
BlueC = (12, 15, 153)
GreenC = (5, 51, 4)
PurpleC = (41, 8, 51)
OrangeC = (148, 43, 4)
YellowC = (191, 173, 10)

seriesLoc = [
    None,
    [0],
    None,
    [0, 1, 0],
    None,
    [0, 0, 1, 1, 0],
    None,
    [0, 0, 1, 1, 0, 1, 0]
]

endmatch = {
    '1': 'st',
    '2': 'nd',
    '3': 'rd',
    '4': 'th',
    '5': 'th',
    '6': 'th',
    '7': 'th',
    '8': 'th',
    '9': 'th',
    '0': 'th',
}

ExtraGames = pandas.DataFrame({'TYPE':['ENG', 'ESP', 'GER', 'na'], 'GAMES':[3, 4, 2, 0]}).set_index('TYPE')

def text(string, pos, size, surface, color=WhiteC, spot = 'center'):
    font = pygame.font.Font('freesansbold.ttf', size)
    obj = font.render(str(string), True, color)
    textRect = obj.get_rect()
    if spot == 'center':
        textRect.center = pos
    elif spot == 'midleft':
        textRect.midleft = pos
    surface.blit(obj, textRect)

def image(path, out, tl, size):
    pic = pygame.transform.scale(pygame.image.load(path), size)
    picrect = pic.get_rect().move(tl)
    out.blit(pic, picrect)

def checkpoint(str, pos=(600, 300), size=40, out=None, color=WhiteC, filter=None):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(BlackC)
        text('Click to continue', (600, 50), 16, out, WhiteC)
        text(str, pos, size, out, color)
        pygame.display.update()

def pythag(a, b):  # A lot of this file is gonna be "just nice to have"
    return math.sqrt(a ** 2 + b ** 2)

def closeEnough(a, b):
    return abs(a-b) <= .001


def odds(chance):  # inputs are 0 to 1, default of uniform()
    X = numpy.random.uniform()
    if X < chance:
        return True
    else:
        return False


def quad(var, a, b, c):  # "just nice to have"
    return (a * (var ** 2)) + (var * b) + c

class Spot:
    def __init__(self, obj, obj2=None):
        if obj2 is None:
            self.x = obj[0]
            self.y = obj[1]
        else:
            self.x = obj
            self.y = obj2
    
    def __str__(self):
        return f'({round(self.x)}, {round(self.y)})'


def distanceFormula(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

def quadraticFormula(a, b, c):
    core = b**2 - (4*a*c)
    # print(a, b, c, core)
    if core < 0:
        return tuple() # tuple of 0
    elif core == 0:
        return (-b/(2*a),) # tuple of 1
    plus  = (-b + math.sqrt(core)) / (2*a)
    minus = (-b - math.sqrt(core)) / (2*a)
    return min([plus, minus]), max([plus, minus])


def clamp(val, low=0, high=1):  # nice2have, really surprised it isn't built-in Python
    if val < low:
        val = low
    elif val > high:
        val = high
    return val

def dfSpotChecker(df, row, col, val):
    try:
        return df.iloc[row, col] == val
    except IndexError:
        return False


def listsub(x, y):
    return [x[0]-y[0], x[1]- y[1]]

def listmult(x, scalar):
    return [scalar * x[0], scalar * x[1]]
    
def rgbTOlab(color):
    rgb = sRGBColor(rgb_r = color[0], rgb_g =color[1], rgb_b = color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor)
    return lab


def fancycolor(color):
    return sRGBColor(rgb_r = color[0], rgb_g =color[1], rgb_b = color[2], is_upscaled=True)

def colorscore(colors):
    return delta_e_cie2000(rgbTOlab(colors[0]), rgbTOlab(colors[1]))


def colorchecker(homecols, awaycols, req = 0):
    order = [
        [homecols[0], awaycols[0]],
        [homecols[0], awaycols[1]],
        [homecols[1], awaycols[1]],
        [homecols[1], awaycols[0]]
    ]
    for pair in order:
        if colorscore(pair) > req:
            return pair
    return [BlueC, RedC]


def bracket(teams, surf, topL = (0, 25), botR = (1000, 700), page = True, leng = None, score = False):  # This shit is dope, teams should be seeded. More than 32 really get squeezed.
    surf.fill(color=WhiteC)
    minX, minY = topL
    maxX, maxY = botR
    n = len(teams)
    R = math.ceil(math.log(n, 2)) + 1
    xpr = (maxX - minX) / R
    bracketRecursive((maxX, .5*(minY+maxY)), 1, R, xpr, minY, maxY, surf, teams, 1, score)
    topFirst = (botR[0] - topL[0]) / (2*R)
    topSplit = (botR[0] - topL[0]) / (R)
    if leng:
        for i in range(len(leng)):
            text(f'Best of {leng[i]}', (topFirst + i*topSplit, 15), 12, surf)
    pygame.display.update()
    while page:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                page = False
            if event.type == pygame.QUIT:
                pygame.quit()


def bracketRecursive(front, r, maxr, xpr, ceil, floor, surf, teams, seed, score):  # ceil in minY, floor is maxY
    back = front[0] - xpr, front[1]
    up = back[0], .5*(back[1] + ceil)
    down = back[0], .5*(floor + back[1])
    pygame.draw.line(surf, BlackC, front, back)
    if r == maxr or 2**r + 1 - seed > len(teams) or allNone(teams[2**r - seed]):
        text(f'{teams[seed-1]}' + (f' ({teams[seed-1].pwins})' if score else ''), (.5*(front[0]+back[0]), front[1]-10), 16, surf)
        return
    if r < maxr:
        pygame.draw.line(surf, BlackC, back, up)
        pygame.draw.line(surf, BlackC, back, down)
        bracketRecursive(up, r + 1, maxr, xpr, ceil, front[1], surf, teams, seed, score)
        bracketRecursive(down, r + 1, maxr, xpr, front[1], floor, surf, teams, 2**r + 1 - seed, score)

def allNone(x):
    if x is None:
        return True
    elif isinstance(x, tuple):
        return allNone(x[0]) and allNone(x[1])
    else:
        return False


def resultsDisplayer(out, games, addedText = ''): # Takes up to 12
    if len(games) > 12:
        print(len(games), 'is bigger than 12')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click to continue', (500, 50), 16, out, BlackC)
        text(addedText, (250, 50), 24, out, BlackC)
        text(addedText, (750, 50), 24, out, BlackC)
        for sheet in range(len(games)):
            games[sheet].board.output(out, 200 + 300*(sheet%3), 100 + 150*(sheet//3))
        pygame.display.update()

def standingsDisplayer(out, tables, addedText = ''): # Takes up to 4
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(BlackC)
        text('Click to continue', (500, 50), 16, out, WhiteC)
        text(addedText, (250, 50), 24, out, WhiteC)
        text(addedText, (750, 50), 24, out, WhiteC)
        for j in tables:
            curx = 200
            cury = 200
            for i in range(min(len(j), 16)):
                cury += 30
                text(strViaList(j.iloc[i], i+1), (curx, cury), 16, out)
            cury = 200
            curx = 1000 - 200
            for i in range(16, len(j)):
                cury += 30
                text(strViaList(j.iloc[i], i+1), (curx, cury), 16, out)
        pygame.display.update()


def strup(x, leng):  # String up... but im calling it strup from now on
    y = str(x)
    return y + max(0, int(1.6*(leng-len(y))))*' '

def dataframe_to_aligned_strings_with_headers(df):
    # Determine maximum width for each column based on column headers and data
    col_widths = {
        col: max(df[col].astype(str).map(len).max(), len(col))
        for col in df.columns
    }
    
    # Prepare the header row
    header_row = ' | '.join(
        f"{col:<{col_widths[col]}}"
        for col in df.columns
    )
    
    # Prepare the data rows
    data_rows = []
    for index, row in df.iterrows():
        row_str = ' | '.join(
            f"{str(row[col]):>{col_widths[col]}}"  # Right-align each column
            for col in df.columns
        )
        data_rows.append('|'+row_str+'|')
    
    # Combine header and data rows
    aligned_strings = ['|'+header_row+'|'] + data_rows
    
    return aligned_strings


"""
RegionT = [ # This is here for future
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()])
]
League = [
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB(),
    CLUB()
]
"""


def seeder_full(matchups):
    x = [None]*100
    recD = seeder_rec(matchups, 0, 1)
    high = max(list(recD.values()))
    for team in list(recD.keys()):
        x[recD[team]] = team
    return x[:high+1]

    #recD.update

def seeder_rec(split, high, turn):
    if isinstance(split, tuple) or isinstance(split, list):
        smallD = {}
        smallD.update(seeder_rec(split[0], high = high, turn = turn + 1))
        smallD.update(seeder_rec(split[1], high = 2**turn - 1 - high, turn = turn + 1))
        return smallD
    else:
        return {split: high}
            

def findMatchups(teams, depth, path):
    #print(teams, depth, path)
    #print(path.append(0))
    if isinstance(teams, tuple) or isinstance(teams, list):
        if depth == 1:
            return {teams: path}
        else:
            smallD = {}
            smallD.update(findMatchups(teams[0], depth = depth-1, path = path + [0]))
            smallD.update(findMatchups(teams[1], depth = depth-1, path = path + [1]))
            return smallD
    else:
        return {}


def path_replacer(big, path, rep):
    if len(path) == 0:
        return rep
    else:
        if path[0] == 0: # Either 0 or 1
            return path_replacer(big[0], path[1:], rep), big[1]
        else:
            return big[0], path_replacer(big[1], path[1:], rep)

def unseeder(teams):
    if len(teams) == 2:
        return teams	
    elif len(teams) == 1:
        return teams[0]
    #R = math.ceil(log(len(x), 2)) + 1
    group1 = []
    group2 = []
    cur = 0
    group1.append(teams[cur])
    cur += 1
    while cur < len(teams):
        group2.append(teams[cur])
        cur += 1
        if cur < len(teams):
            group2.append(teams[cur])
            cur += 1
            if cur < len(teams):
                group1.append(teams[cur])
                cur += 1
                if cur < len(teams):
                    group1.append(teams[cur])
                    cur += 1
    return unseeder(tuple(group1)), unseeder(tuple(group2))

def noneRemover(teams):
    if not isinstance(teams, tuple):
        return teams
    if len(teams) == 1:
        return teams[0]
    if allNone(teams[0]):
        return noneRemover(teams[1])
    if allNone(teams[1]):
        return noneRemover(teams[0])
    return noneRemover(teams[0]), noneRemover(teams[1])

def playoffDecider(x, y, length):
    if (x.pwins == length-1 or y.pwins == length-1) and (abs(x.pwins-y.pwins) < 2):
        return 'highlight'

def RoundRobin(teams, double = True):
    t = teams.copy()
    if len(t) % 2:
        teams.append('_')
    n = len(t)
    fixtures = []
    return_fixtures = []
    for fixture in range(1, n):
        matchs = []
        return_matchs = []
        for i in range(n//2):
            if odds(.5):
                matchs.append((t[i], t[n - 1 - i]))
                return_matchs.append((t[n - 1 - i], t[i]))
            else:
                return_matchs.append((t[i], t[n - 1 - i]))
                matchs.append((t[n - 1 - i], t[i]))
        t.insert(1, t.pop())
        fixtures.append(matchs)
        return_fixtures.append(return_matchs)
    random.shuffle(fixtures)
    random.shuffle(return_fixtures)
    if double:
        return fixtures + return_fixtures
    else:
        return fixtures

def listMergr(x):
    out = []
    for i in x:
        out = out + i
    return out

def findInCup(fixtures, club, flip = False, neutralFinal = True, round = False):
    mini = fixtures[(fixtures['Home'] == club) | (fixtures['Away'] == club)]
    if len(mini) == 0:
        return False
    if round:
        if 4*len(fixtures) <= round:
            return ['NONE', None]
        if len(fixtures) >= round:
            return ['TBD', None]
    if len(mini) > 0:
        m = mini.iloc[0,].to_list()
        if m[0] == club:
            return ['NEUTRAL' if neutralFinal and len(fixtures) == 1 else 'HOME' if not flip else 'AWAY', m[1].name if m[1] is not None else 'NA']
        else:
            return ['NEUTRAL' if neutralFinal and len(fixtures) == 1 else 'AWAY' if not flip else 'HOME', m[0].name if m[1] is not None else 'NA']

def scheduleLister(club, glo, EURO):
    out = pandas.DataFrame(columns = ['GameNum', 'Competition', 'Stage', 'Location', 'Opponent'])
    l, c, e, s, starte = glo.league, 'Alive', glo.euro, club.league.slate, glo.euro
    level = club.league.assoc.leagues.index(club.league)
    hold = None
    holdlevel = None
    holdknock = None
    flipList = [None, None, [None, None, True, False], [None, True, False, False], [True, False, True, False]]
    neutList = [None, None, False, True, False]
    roundList = [None, None, [None, None, 2, 2], [None, 4, 4, 2], [4, 4, 2, 2]]
    counter = glo.overall
    for i in glo.slates[glo.overall:]:
        counter += 1
        #print(out.dtypes)
        #print(out)
        if i == 'League':
            l += 1
            exgames = ExtraGames.loc[club.league.assoc.last, 'GAMES']
            if (l / 50) > (s / (len(club.league.schedule) + (exgames if level > 0 else 0))):
                if s >= len(club.league.schedule):
                    if 50 - l >= exgames:
                        out.loc[len(out)] = [counter, club.league.abr, 'OFF', 'NA', 'NA']
                    else:
                        if club.league.slate >= len(club.league.schedule): # Have the tournament
                            message = findInCup(club.league.playoffs.fixtures, club,
                                               flip = flipList[exgames][l-47],
                                               neutralFinal = neutList[exgames],
                                               round = roundList[exgames][l-47])
                            if not message:
                                out.loc[len(out)] = [counter, club.league.abr, 'PROM PLAYOFF', 'NA', 'NA']
                            else:
                                out.loc[len(out)] = [counter, club.league.abr, 'PROM PLAYOFF'] + message
                        else: # Dont
                            out.loc[len(out)] = [counter, club.league.abr, 'PROM PLAYOFF', 'TBD', 'TBD']
                else:
                    df = pandas.DataFrame(club.league.schedule[s])
                    m = df[(df[0] == club) | (df[1] == club)].iloc[0,].to_list()
                    if m[0] == club:
                        out.loc[len(out)] = [counter, club.league.abr, str(s+1), 'HOME', m[1].name if m[1] is not None else 'NA']
                    else:
                        out.loc[len(out)] = [counter, club.league.abr, str(s+1), 'AWAY', m[0].name if m[0] is not None else 'NA']
                    s += 1
            else:
                out.loc[len(out)] = [counter, club.league.abr, 'OFF', 'NA', 'NA']
        elif i == 'Cup':
            if c == 'Alive':
                message = findInCup(club.league.assoc.cup.fixtures, club)
                if not message:
                    c = 'Eliminated'
                    out.loc[len(out)] = [counter, club.league.assoc.cup.abr, 'CUP', 'Eliminated', 'NA']
                else:
                    c = 'TBD'
                    out.loc[len(out)] = [counter, club.league.assoc.cup.abr, 'CUP'] + message
            else:
                out.loc[len(out)] = [counter, club.league.assoc.cup.abr, 'CUP', 'TBD', 'NA']
        else:
            e += 1
            if e <= 4:
                # Champions League
                if club in listMergr(EURO.CLteams):
                    out.loc[len(out)] = [counter, 'CL', 'PLAY-IN', 'Advanced', 'NA']
                elif club in listMergr(EURO.ELteams):
                    out.loc[len(out)] = [counter, 'EL', 'PLAY-IN', 'Advanced', 'NA']
                elif club in listMergr(EURO.ECteams):
                    out.loc[len(out)] = [counter, 'EC', 'PLAY-IN', 'Advanced', 'NA']
                else:
                    clpi = findInCup(pandas.concat([cup.fixtures for cup in EURO.CLplayin.cups], ignore_index=True), 
                                 club, flip = e % 2 == 1, neutralFinal = False, round = 16 * (.5 ** ((e-1)//2)))
                    elpi = findInCup(pandas.concat([cup.fixtures for cup in EURO.ELplayin.cups], ignore_index=True), 
                                 club, flip = e % 2 == 1, neutralFinal = False, round = 48 * (.5 ** ((e-1)//2)))
                    ecpi = findInCup(pandas.concat([cup.fixtures for cup in EURO.ECplayin.cups], ignore_index=True), 
                                 club, flip = e % 2 == 1, neutralFinal = False, round = 80 * (.5 ** ((e-1)//2)))
                    if clpi:
                        out.loc[len(out)] = [counter, 'CL', 'PLAY-IN'] + clpi
                    elif elpi:
                        out.loc[len(out)] = [counter, 'EL', 'PLAY-IN'] + elpi
                    elif ecpi:
                        out.loc[len(out)] = [counter, 'EC', 'PLAY-IN'] + ecpi
                    else:
                        out.loc[len(out)] = [counter, 'EURO', 'PLAY-IN', 'NA', 'NA']
            elif e <= 10:
                if starte < 4:
                    out.loc[len(out)] = [counter, 'EURO', 'GROUPS', 'NA', 'NA']
                    continue
                if holdlevel is None:
                    if club in listMergr([i.teams for i in EURO.CLteams]):
                        holdlevel = 'CL'
                    elif club in listMergr([i.teams for i in EURO.ELteams]):
                        holdlevel = 'EL'
                    elif club in listMergr([i.teams for i in EURO.ECteams]):
                        holdlevel = 'EC'
                    else:
                        holdlevel = 'na'
                elevel = holdlevel
                map = {'CL':EURO.CLteams, 'EL':EURO.ELteams, 'EC':EURO.ECteams}
                if elevel == 'na':
                    out.loc[len(out)] = [counter, 'EURO', 'GROUPS', 'NA', 'NA']
                else:
                    split = map[elevel]
                    if hold is None:
                        hold = listMergr([i.teams for i in split]).index(club) // 4
                    g = hold
                    df = pandas.DataFrame(split[g].schedule[e-5])
                    m = df[(df[0] == club) | (df[1] == club)].iloc[0,].to_list()
                    if m[0] == club:
                        out.loc[len(out)] = [counter, elevel, 'GROUPS', 'HOME', m[1].name if m[1] is not None else 'NA']
                    else:
                        out.loc[len(out)] = [counter, elevel, 'GROUPS', 'AWAY', m[0].name if m[0] is not None else 'NA']
            else:
                if starte < 10:
                    out.loc[len(out)] = [counter, 'EURO', 'KNOCKOUT', 'NA', 'NA']
                    continue
                if holdknock is None:
                    if findInCup(EURO.CLteams.fixtures, club):
                        holdknock = 'CL'
                    elif findInCup(EURO.ELteams.fixtures, club):
                        holdknock = 'EL'
                    elif findInCup(EURO.ECteams.fixtures, club):
                        holdknock = 'EC'
                    else:
                        holdknock = 'na'
                if holdknock == 'na':
                    out.loc[len(out)] = [counter, 'EURO', 'KNOCKOUT', 'NA', 'NA']
                else:
                    eknock = holdknock
                    map = {'CL':EURO.CLteams, 'EL':EURO.ELteams, 'EC':EURO.ECteams}
                    realknock = map[eknock]
                    message = findInCup(realknock.fixtures, club, flip = e % 2 == 1, round = 2**(1 + (20 - e)//2))
                    out.loc[len(out)] = [counter, holdknock, 'KNOCKOUT'] + message
    return out

def getNextSchedule(glob, EURO, spec = None):
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
            #assoc.cup.playNext(glob.cup)
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

def nameShorten(x):
    if x is None:
        return None
    else:
        return x.name if len(x.name) < 10 else x.ABR


"""
x = (1, 2, 3, 4, 5, 6, None, None, None, None, 7, 8, 9)
print(unseeder(x))
print(seeder_full(unseeder(x)))
print(noneRemover(unseeder(x)))
print(seeder_full(noneRemover(unseeder(x))))

pygame.init()

out = pygame.display.set_mode(screen)
pygame.display.set_caption('CURLING')
kill = False

bracket(seeder_full(unseeder(x)), out)
bracket(seeder_full(noneRemover(unseeder(x))), out)
"""