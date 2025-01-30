from Game import *



RESULTS = pandas.DataFrame(columns = ['Year', 'Competition', 'Round', 'Home', 'HomeScore', 'AwayScore', 'Away', 'Notes'])
DIRECTORY = pandas.DataFrame(columns = ['Year', 'League', 'Team', 'BaseRating'])
WINNERS = pandas.DataFrame(columns = ['Year', 'Competition', 'Team'])


def quicknest(l, seed = False):
    if seed:
        return [(l[i], l[len(l)-1-i]) for i in range(0,len(l)//2)] 
    else:
        return [(l[i], l[i+1]) for i in range(0,len(l),2)]
RoundName = ['Final', 'Semi', 'Quarter']
RoundAbr = ['F', 'SF', 'QF']

class DL_ASSOCIATION:
    def __init__(self, name, abr, leagues, DIRECTORY):
        self.name = name
        self.abr = abr
        self.year = 1
        self.leagues = [DL_LEAGUE(f'Division {div+1}', f'DIV{div+1}', leagues[div], self) for div in range(len(leagues))]
        for i in self.leagues:
            i.mydiv = self.leagues.index(i)+1
        self.directoryUpdate(DIRECTORY)
        self.setLeagues()
        allteams = []
        for i in self.leagues:
            allteams += i.teams
        self.cup = CUP(f'SUPER CUP', f'CUP', allteams, assoc = self)
        self.slate = 1
        self.setGoals()

    def playNext(self, RESULTS, WINNERS):
        if self.alldone():
            print('NO MORE GAMES')
            return
        if self.slate in [5, 9, 14, 18, 23, 27, 32, 36]:
            self.cup.playNext(RESULTS, WINNERS)
        else:
            for i in self.leagues:
                i.playNext(RESULTS, WINNERS)
        WINNERS.to_csv(f'Output/Winners.csv', index=False)
        self.slate += 1

    def alldone(self):
        return numpy.mean([i.done for i in self.leagues]) == 1

    def setGoals(self):
        for i in self.leagues:
            for j in i.teams:
                j.goal = list(i.standings.index).index(j)
                j.ratingAdjustMean = 0

    def getRAM(self): # ratingAdjustMean, only call once
        for i in self.leagues:
            for j in i.teams:
                final = list(i.standings.index).index(j)
                j.ratingAdjustMean += (j.goal - final)/2

    def ratingAdjust(self):
        for i in self.leagues:
            for j in i.teams:
                j.ratingAdjust()

    def directoryUpdate(self, DIRECTORY):
        for i in self.leagues:
            for j in i.teams:
                DIRECTORY.loc[len(DIRECTORY)] = [self.year, i.name, j.name, j.baserating]
        DIRECTORY.to_csv(f'Output/Directory.csv', index=False)

    def setLeagues(self):
        for i in self.leagues:
            for j in i.teams:
                j.league = i

    def setTeams(self):
        for ind in range(len(self.leagues)):
            comingDown = self.leagues[ind-1].forRelegation if ind > 0 else []
            comingUp = self.leagues[ind+1].forPromotion if ind < 15 else []
            remainingTeams = [x for x in list(self.leagues[ind].standings.index) \
                              if x not in self.leagues[ind].forPromotion + self.leagues[ind].forRelegation]
            self.leagues[ind].teams = comingDown + remainingTeams + comingUp
            
    def leagueResets(self):
        for i in self.leagues:
            i.seasonStart()

    def yearReset(self, DIRECTORY):
        self.getRAM()
        self.ratingAdjust()
        self.setTeams()
        self.year += 1
        self.slate = 1
        self.setLeagues()
        self.directoryUpdate(DIRECTORY)
        self.leagueResets()
        #allteams = []
        #for i in self.leagues:
        #    allteams += i.teams
        #self.seasonStart(allteams)
        

class CUP:
    def __init__(self, name, abr, teams, assoc, agg = False, finalagg = False):
        self.name = name
        self.abr = abr
        self.teams = teams
        self.fixtures = None
        self.winners = None
        self.finalists = []
        self.agg = agg
        self.finalagg = finalagg
        self.assoc = assoc
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
        self.out(RESULTS)

    def resultHandler(self, result, RESULTS, advance = True):
        if self.leg == 2 and result[3] != 'BYE':
            spit = result.copy()
            spit[1] -= self.aggholder.loc[spit[0], 'Score']
            spit[2] -= self.aggholder.loc[spit[3], 'Score']
            RESULTS.loc[len(RESULTS)] = [self.assoc.year, self.abr, f'{len(self.fixtures)*2}-{self.leg}']+spit
        else:
            RESULTS.loc[len(RESULTS)] = [self.assoc.year, self.abr, f'{len(self.fixtures)*2}-{self.leg}']+result
        if advance:
            if result[2] == 'NA': # Home Bye
                self.winners.append(result[0])
            elif result[1] > result[2]: # Home Win
                self.winners.append(result[0])
                result[0].ratingAdjustMean += (1 if numpy.log2(len(self.fixtures))*2 < result[0].league.mydiv else 0)
            else:  # Away win, no draws
                self.winners.append(result[3])
                result[3].ratingAdjustMean += (1 if numpy.log2(len(self.fixtures))*2 < result[3].league.mydiv else 0)
        else:
            if result[2] != 'NA':
                self.aggholder.loc[result[0]] = [result[1]]
                self.aggholder.loc[result[3]] = [result[2]]

    def playNext(self, RESULTS, WINNERS, Round = 0):
        if len(self.fixtures) < Round: # Get the finals lined up
            return
        if self.fixtures.shape[1] == 1:
            #print(f'{self.name} over')
            return
        elif len(self.fixtures) == 1:
            self.finalists = [self.fixtures.Home[0], self.fixtures.Away[0]]
        self.winners = []
        matches = zip(self.fixtures.Home, self.fixtures.Away)
        if ((not self.agg) and len(self.fixtures) > 1) or ((not self.finalagg) and len(self.fixtures) == 1): # No Agg
            matches = zip(self.fixtures.Home, self.fixtures.Away)
            if len(self.fixtures) == 1: # Final at neutral site
                self.resultHandler(game(self.fixtures.Home[0], self.fixtures.Away[0], ET=True, neutral = True), RESULTS)
            else:
                for match in matches:
                    if match[1] is None:
                        self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'], RESULTS)
                    else:
                        self.resultHandler(game(match[0], match[1], ET=True), RESULTS)
        elif self.leg == 1: # First leg
            self.aggholder = pandas.DataFrame(columns = ['Teams', 'Score']).set_index('Teams')
            for match in matches:
                if match[1] is None:
                    self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'], RESULTS, advance=False)
                else:
                    self.resultHandler(game(match[1], match[0]), RESULTS, advance=False) # Away hosts the first leg
            self.leg = 2
        else:  # Second Leg
            for match in matches:
                if match[1] is None:
                    self.resultHandler([match[0], 'NA', 'NA', 'BYE', 'No Game'], RESULTS, advance=True)
                else:
                    self.resultHandler(game(match[0], match[1], ET = True, 
                    agg = [self.aggholder.loc[match[0], 'Score'], self.aggholder.loc[match[1], 'Score']]), RESULTS, advance=True)
            self.aggholder = pandas.DataFrame(columns = ['Teams', 'Score']).set_index('Teams')
            self.leg = 1
        if len(self.winners) > 1:
            random.shuffle(self.winners)
            split = len(self.winners) // 2
            home = self.winners[:split]
            away = self.winners[split:]
            self.fixtures = pandas.DataFrame({'Home': home, 'Away': away})
        elif len(self.winners) == 1:
            self.fixtures = pandas.DataFrame({'Champion': [self.winners[0]]})
            WINNERS.loc[len(WINNERS)] = [self.assoc.year, self.abr, self.winners[0]]
        self.out(RESULTS)

    def seasonStart(self, teams):
        if teams is not None:
            self.teams = teams
        self.fixtures = None
        self.winners = None
        self.finalists = []
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
        self.out(RESULTS)

    def __str__(self):
        return self.name


    def out(self, RESULTS):
        RESULTS.to_csv(f'Output/Results.csv', index=False)
        self.fixtures.to_csv(f'Output/{self.abr}Fixtures.csv', index=False)

class DL_LEAGUE:
    def __init__(self, name, abr, teams, assoc = None):
        self.name = name
        self.abr = abr
        self.teams = teams
        self.assoc = assoc
        self.mydiv = 0
        n = len(teams)
        self.standings = pandas.DataFrame({
            'Teams': self.teams,
            'Points': [0]*n,
            'GoalDifference': [0]*n,
            'Wins': [0]*n,
            'Losses': [0]*n
        }).set_index('Teams')
        self.H2H = pandas.DataFrame(0, index=self.teams, columns=self.teams) # For Head 2 Head Results
        self.stage = 1
        self.forPromotion = []
        self.forRelegation = []
        self.cur = DL_STAGE(f'{self.name} Stage 1', f'{self.abr}-1', self)
        self.playoffs = None
        self.done = False
        self.out(RESULTS)

    def playNext(self, RESULTS, WINNERS):
        if self.done == True:
            #print('No more games in', self.name)
            return
        if self.stage < 5:
            self.cur.playNext(RESULTS)
            if self.stage in [1, 2, 3] and self.cur.round == 8:
                self.stage += 1
                self.cur = DL_STAGE(f'{self.name} Stage {self.stage}', f'{self.abr}-{self.stage}', self)
            elif self.stage == 4 and self.cur.round == 8:
                WINNERS.loc[len(WINNERS)] = [self.assoc.year, f'{self.abr}-S', list(self.standings.index)[0]]
                self.stage = 5
                if self.mydiv == 1:
                    self.playoffs = {
                        'Championship': DL_Bracket(f'{self.name} Championship', f'{self.abr}-C', self, 
                                                    list(self.standings.index)[:6], [2, 3, 4]),
                        'Relegation': DL_Bracket(f'{self.name} Relegation', f'{self.abr}-R', self, 
                                                  list(self.standings.index)[12:14], [2])}
                elif self.mydiv == 16:
                    self.playoffs = {
                        'Championship': DL_Bracket(f'{self.name} Championship', f'{self.abr}-C', self, 
                                                    list(self.standings.index)[:2], [3]),
                        'Promotion': DL_Bracket(f'{self.name} Promotion', f'{self.abr}-P', self, 
                                                  list(self.standings.index)[2:5], [1, 2])}
                else:
                    self.playoffs = {
                        'Championship': DL_Bracket(f'{self.name} Championship', f'{self.abr}-C', self, 
                                                    list(self.standings.index)[:2], [3]),
                        'Promotion': DL_Bracket(f'{self.name} Promotion', f'{self.abr}-P', self, 
                                                  list(self.standings.index)[2:5], [1, 2]),
                        'Relegation': DL_Bracket(f'{self.name} Relegation', f'{self.abr}-R', self, 
                                                  list(self.standings.index)[12:14], [2])}
        else:
            alldone = True
            for i in self.playoffs.keys():
                if isinstance(self.playoffs[i], DL_Bracket):
                    self.playoffs[i].playNext(RESULTS, WINNERS)
                    if self.playoffs[i].winner is not None:
                        pass
                    else:
                        alldone = False
            if alldone:
                self.done = True
                if self.mydiv > 1:
                    self.forPromotion = list(self.standings.index)[:2] + [self.playoffs['Promotion'].winner]
                if self.mydiv < 16:
                    self.forRelegation = list(self.standings.index)[14:] + [self.playoffs['Relegation'].second]
        self.out(RESULTS)

    def display(self):
        if self.stage < 5:
            #print(self.stage)
            return self.cur.display()
        else:
            return pandas.concat([i.display() for i in self.playoffs.values()])
        

    def seasonStart(self):
        n = len(self.teams)
        self.standings = pandas.DataFrame({
            'Teams': self.teams,
            'Points': [0]*n,
            'GoalDifference': [0]*n,
            'Wins': [0]*n,
            'Losses': [0]*n
        }).set_index('Teams')
        self.H2H = pandas.DataFrame(0, index=self.teams, columns=self.teams) # For Head 2 Head Results
        self.stage = 1
        self.forPromotion = []
        self.forRelegation = []
        self.cur = DL_STAGE(f'{self.name} Stage 1', f'{self.abr}-1', self)
        self.playoffs = None
        self.done = False
        self.out(RESULTS)

    def out(self, RESULTS):
        RESULTS.to_csv(f'Output/Results.csv', index = False)
        self.display().reset_index().to_csv(f'Output/{self.abr}Display.csv', index = False)
        self.standings.reset_index().to_csv(f'Output/{self.abr}Standings.csv', index = False)

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.teams)

class DL_STAGE:
    def __init__(self, name, abr, league):
        self.name = name
        self.abr = abr
        self.teams = league.standings.index
        self.league = league
        self.cur = (self.quicknest(self.teams, True),)
        self.round = 1

    def playNext(self, RESULTS):
        if self.round == 1:
            R1 = self.cur[0]
            R2 = []
            L1R1 = []
            for i in R1:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                R2.append(res[0])
                L1R1.append(res[1])
            self.cur = (quicknest(R2, True), quicknest(L1R1, True))
        elif self.round == 2:
            R2, L1R1 = self.cur
            R3 = []
            L1R2 = []
            L2R1 = []
            for i in R2:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                R3.append(res[0])
                L2R1.append(res[1])
            for i in L1R1:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                L1R2.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 0
            self.cur = (quicknest(R3, True), quicknest(L1R2, True), quicknest(L2R1, True))
        elif self.round == 3:
            R3, L1R2, L2R1 = self.cur
            R4 = []
            L1R3 = []
            L2R2 = []
            L3R1 = []
            for i in R3:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                R4.append(res[0])
                L3R1.append(res[1])
            for i in L1R2:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                L1R3.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 1
            for i in L2R1:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                L2R2.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 1
            self.cur = (quicknest(R4), quicknest(L1R3), quicknest(L2R2), quicknest(L3R1))
        elif self.round == 4:
            R4, L1R3, L2R2, L3R1 = self.cur
            FINAL = []
            Lower4 = []
            for i in R4:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                FINAL.append(res[0])
                Lower4.append(res[1])
            for i in L1R3:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                Lower4.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 2
            for i in L2R2:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                Lower4.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 2
            for i in L3R1:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                Lower4.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 2
            self.cur = (FINAL, quicknest(Lower4))
        elif self.round == 5:
            FINAL, Lower4 = self.cur
            Lower2 = []
            for i in Lower4:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                Lower2.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 4
            self.cur = (FINAL, quicknest(Lower2))
        elif self.round == 6:
            FINAL, Lower2 = self.cur
            for i in Lower2:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                FINAL.append(res[0])
                self.league.standings.loc[res[1], 'Points'] += 8
            self.cur = (quicknest(FINAL),)
        elif self.round == 7:
            FINAL = self.cur[0]
            for i in FINAL:
                res = self.resultHandlerDLT(game(i[0], i[1], ET = True), RESULTS)
                self.league.standings.loc[res[1], 'Points'] += 16
                self.league.standings.loc[res[0], 'Points'] += 32
                self.cur = [(res[0],)]
        self.round += 1
        self.league.standings['H2H'] = [self.league.H2H.loc[cur, list(self.league.standings.loc[(self.league.standings.Points ==\
                                                                                         self.league.standings.loc[cur, 'Points']) & \
                                                                                        (self.league.standings.index != cur)].index)].sum() - \
                                self.league.H2H.loc[list(self.league.standings.loc[(self.league.standings.Points == \
                                                                                    self.league.standings.loc[cur, 'Points']) & \
                                                                                    (self.league.standings.index != cur)].index), cur].sum() \
                                for cur in self.league.standings.index]
        self.league.standings.sort_values(['Points', 'H2H', 'GoalDifference'], ascending = False, inplace = True)

    def resultHandlerDLT(self, result, RESULTS):
        RESULTS.loc[len(RESULTS)] = [self.league.assoc.year, self.abr, self.round]+result
        self.league.H2H.loc[result[0], result[3]] += result[1]
        self.league.H2H.loc[result[3], result[0]] += result[2]
        self.league.standings.loc[result[0], 'GoalDifference'] += result[1]-result[2]
        self.league.standings.loc[result[3], 'GoalDifference'] += result[2]-result[1]
        if result[1] > result[2]:  # Home Win
            self.league.standings.loc[result[0], 'Wins'] += 1
            self.league.standings.loc[result[3], 'Losses'] += 1
            return result[0], result[3]
        elif result[2] > result[1]:  # Away Win
            self.league.standings.loc[result[3], 'Wins'] += 1
            self.league.standings.loc[result[0], 'Losses'] += 1
            return result[3], result[0]

    def display(self, out = False):
        df = pandas.concat([pandas.DataFrame(i) for i in self.cur])
        if out:
            RESULTS.to_csv(f'Output/Results.csv', index=False)
            df.to_csv(f'Output/{self.abr}Fixtures.csv', index=False)
        return df
            
    def quicknest(self, l, seed = False):
        if seed:
            return [(l[i], l[len(l)-1-i]) for i in range(0,len(l)//2)] 
        else:
            return [(l[i], l[i+1]) for i in range(0,len(l),2)]

    def __str__(self):
        return self.name

    def __len__(self):
        return 16


class PlayoffSeries:
    def __init__(self, name, abr, league, high, low, length):
        self.name = name
        self.abr = abr
        self.league = league
        self.high = high
        self.low = low
        self.length = length
        self.gamenum = 1
        self.highwins, self.lowwins = 0, 0
        self.winner = None

    def playNext(self, RESULTS):
        if self.gamenum > ((2*self.length)-1): # Series already over
            return self.winner
        if (self.gamenum % 2 + 1) == 0:
            res = game(self.high, self.low, ET = True)
            if res[1] > res[2]:
                self.highwins += 1
            else:
                self.lowwins += 1
        else:
            res = game(self.low, self.high, ET = True)
            if res[1] > res[2]:
                self.lowwins += 1
            else:
                self.highwins += 1
        RESULTS.loc[len(RESULTS)] = [self.league.assoc.year, self.abr, self.gamenum]+res
        self.gamenum += 1
        if self.highwins == self.length:
            self.gamenum = 2*self.length
            self.winner = self.high
            return self.winner
        elif self.lowwins == self.length:
            self.gamenum = 2*self.length
            self.winner = self.low
            return self.winner

    def display(self):
        # Create a DataFrame with one row and the specific columns
        data = {
            'High Seed': [self.high],
            'High Seed Wins': [self.highwins],
            'Low Seed Wins': [self.lowwins],
            'Low Seed': [self.low]
        }
        # The index is self.abr
        df = pandas.DataFrame(data, index=[self.abr])
        return df

    def isDone(self):
        return self.gamenum > ((2*self.length)-1)
    
class DL_Bracket:
    def __init__(self, name, abr, league, teams, lengths):
        self.name = name
        self.abr = abr
        self.league = league
        self.teams = teams
        self.lengths = lengths
        n = len(self.teams)
        self.numRounds = math.ceil(math.log(n, 2))
        self.round = 1
        numbyes = 2**math.ceil(math.log(n, 2)) - n
        self.cur = quicknest(self.teams[numbyes:], True)
        for i in range(len(self.cur)):
            self.cur[i] = PlayoffSeries(f'{self.name} {RoundName[self.numRounds - self.round]}', 
                                        f'{self.abr}-{RoundAbr[self.numRounds - self.round]}', 
                                        self.league, self.cur[i][0], self.cur[i][1], self.lengths[self.round-1])
        self.next = self.teams[:numbyes]
        self.winner = None
        self.second = None
        
    def alldone(self):
        return numpy.mean([i.isDone() for i in self.cur]) == 1
        
    def getWinners(self):
        return [i.winner for i in self.cur]
        
    def playNext(self, RESULTS, WINNERS):
        if self.winner is not None:
            return self.winner
        for i in self.cur:
            i.playNext(RESULTS)
        if self.alldone():
            self.round += 1
            if len(self.cur)==1 and len(self.next) == 0:
                self.winner = self.cur[0].winner
                WINNERS.loc[len(WINNERS)] = [self.league.assoc.year, self.abr, self.winner]
                self.second = self.cur[0].low if self.cur[0].winner == self.cur[0].high else self.cur[0].high
            self.cur = quicknest(self.next + self.getWinners(), True)
            for i in range(len(self.cur)):
                self.cur[i] = PlayoffSeries(f'{self.name} {RoundName[self.numRounds - self.round]}', 
                                            f'{self.abr}-{RoundAbr[self.numRounds - self.round]}', 
                                            self.league, self.cur[i][0], self.cur[i][1], self.lengths[self.round-1])
            self.next = []

    def display(self):
        if self.winner is not None:
            return pandas.DataFrame({'High Seed': [self.winner], 
                                    'High Seed Wins': [0],
                                    'Low Seed Wins': [0],
                                    'Low Seed': [numpy.nan]}, 
                                    index=[f'{self.abr}-W'])
        return pandas.concat([i.display() for i in self.cur] + [pandas.DataFrame({'High Seed': self.next, 
                                                                                  'High Seed Wins': [0]*len(self.next),
                                                                                  'Low Seed Wins': [0]*len(self.next),
                                                                                  'Low Seed': [numpy.nan]*len(self.next)}, 
                                                                                 index=[f'{self.abr}-BYE']*len(self.next))])
        
        