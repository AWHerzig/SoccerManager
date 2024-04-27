from Game import *

year = 1
RESULTS = pandas.DataFrame(columns = ['Year', 'Competition', 'Round', 'Home', 'HomeScore', 'AwayScore', 'Away', 'Notes'])

class ASSOCIATION:
    def __init__(self, name, abr, leagues, relSpots, lastSpot, euroSpots):
        self.name = name
        self.abr = abr
        self.leagues = [LEAGUE(f'{self.name} League {div+1}', f'{self.abr}-{div+1}', leagues[div], self) for div in range(len(leagues))]
        self.relSpots = relSpots
        self.last = lastSpot  # 0 for straight up, 1 for "England" Playoff, 2 for "Germany" Playoff 
        allteams = []
        for i in self.leagues:
            allteams += i.teams
        self.cup = CUP(f'{self.name} Cup', f'{self.abr}-C', allteams)
        self.euroSpots = euroSpots
        self.euroTeams = []

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
        if self.leagues[0].slate != len(self.leagues[0].schedule):
            raise ValueError('League isnt finished')
        # Start Europe
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
        """  
        self.euroTeams = [
            cands[:CLspots],  # Champions League
            cands[CLspots:sum(self.euroSpots[0:2])],  # Europa League
            cands[sum(self.euroSpots[0:2]):totalspots],  # Conference League
            cands[totalspots:(totalspots+3)]  # Extra In case
        ]
        """
        self.euroTeams = cands[:10]  # all in one list for backups
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
                if self.last > 0:
                    promoted = downTeams[:(self.relSpots[div]-1)] + [self.leagues[div+1].playoffs.fixtures.Champion[0]]
                else:
                    promoted = downTeams[:self.relSpots[div]]
                stayDown = [team for team in downTeams if team not in promoted]
                self.leagues[div].seasonStart(survive + promoted)
                self.leagues[div+1].seasonStart(relegated + stayDown)
        # END RELEGATION
        allteams = []
        for i in self.leagues:
            allteams += i.teams
        self.cup.seasonStart(allteams)
    


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
        self.slate = 0
        self.playoffs = None
        self.out()

    def resultHandler(self, result):
        RESULTS.loc[len(RESULTS)] = [year, self.abr, self.slate+1]+result
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
        if self.slate < len(self.schedule):
            for match in self.schedule[self.slate]:
                self.resultHandler(game(match[0], match[1]))
            self.standings.sort_values(['Points', 'GoalDifference', 'GoalsFor', 'Wins'], ascending = False, inplace = True)
            self.slate += 1
            self.out()
        else:
            mydiv = self.assoc.leagues.index(self)
            if self.playoffs is None and self.assoc.last > 0 and mydiv > 0:
                autospots = self.assoc.relSpots[mydiv - 1] - 1
                if self.assoc.last == 1:
                    self.playoffs = CUP(self.name + ' prom. playoffs', self.abr + 'P', \
                        teams = list(self.standings.index)[autospots:(autospots+4)], agg = True, finalagg = False)
                else:
                    topTeam = self.assoc.leagues[mydiv-1].standings.index[len(self.assoc.leagues[mydiv-1].standings) - (autospots+1)]
                    self.playoffs = CUP(self.name + ' prom. playoffs', self.abr + 'P', \
                        teams = [self.standings.index[autospots], topTeam], \
                        agg = True, finalagg = True)
                self.playoffs.playNext()
            elif self.assoc.last > 0 and mydiv > 0:
                self.playoffs.playNext()
            else:
                pass

    def seasonStart(self, teams = None):
        if teams is not None:
            self.teams = teams
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
        self.slate = 0

    def out(self):
        RESULTS.to_csv(f'Output/Results.csv', index = False)
        self.standings.reset_index().to_csv(f'Output/{self.abr}Standings.csv', index = False)


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
        self.out()

    def resultHandler(self, result, advance = True):
        RESULTS.loc[len(RESULTS)] = [year, self.abr, f'{len(self.fixtures)*2}-{self.leg}']+result
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
            raise ValueError('Cup already over')
        self.winners = []
        matches = zip(self.fixtures.Home, self.fixtures.Away)
        if ((not self.agg) and len(self.fixtures) > 1) or ((not self.finalagg) and len(self.fixtures) == 1): # No Agg
            matches = zip(self.fixtures.Home, self.fixtures.Away)
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


    def out(self):
        RESULTS.to_csv(f'Output/Results.csv', index=False)
        self.fixtures.to_csv(f'Output/{self.abr}Fixtures.csv', index=False)
        



           

        


        