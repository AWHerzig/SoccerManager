from Matchup import *

qualitySpread = 0
pqualSpread = 7
adjustSpread = 5

class GK:
    def __init__(self, qual):
        self.name = names.get_full_name(gender = 'male')
        self.POS = 'GK'
        self.shotstopper = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.sweeperkeeper = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.eleventhman = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        # Stats
        self.age = 25
        self.contract = 3
        self.gamesplayed = 0
        self.wins = 0

    def stats(self):
        return f'STOP: {self.shotstopper}. SWEEP: {self.sweeperkeeper}. 11MAN: {self.eleventhman}.'

    def info(self):
        return f'Age: {self.age}. Yrs: {self.contract}. P: {self.gamesplayed}. W: {self.wins}'

class DEF:
    def __init__(self, qual):
        self.name = names.get_full_name(gender = 'male')
        self.POS = 'DEF'
        self.lowblock = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.possession = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.overload = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.longball = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        # Stats
        self.age = 25
        self.contract = 3
        self.gamesplayed = 0
        self.wins = 0

    def stats(self):
        return f'BL: {self.lowblock}. PO: {self.possession}. OL: {self.overload}. LB: {self.longball}.'

    def info(self):
        return f'Age: {self.age}. Yrs: {self.contract}. P: {self.gamesplayed}. W: {self.wins}'

class MID:
    def __init__(self, qual):
        self.name = names.get_full_name(gender = 'male')
        self.POS = 'MID'
        self.quick = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.holding = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.control = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.crossing = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        # Stats
        self.age = 25
        self.contract = 3
        self.gamesplayed = 0
        self.wins = 0

    def stats(self):
        return f'QU: {self.quick}. HL: {self.holding}. CN: {self.control}. CR: {self.crossing}.'

    def info(self):
        return f'Age: {self.age}. Yrs: {self.contract}. P: {self.gamesplayed}. W: {self.wins}'

class ATT:
    def __init__(self, qual):
        self.name = names.get_full_name(gender = 'male')
        self.POS = 'ATT'
        self.routeone = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.false9 = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.inbehind = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        self.holdup = round(clamp(numpy.random.normal(qual, pqualSpread), 0, 100))
        # Stats
        self.age = 25
        self.contract = 3
        self.gamesplayed = 0
        self.wins = 0

    def stats(self):
        return f'R1: {self.routeone}. F9: {self.false9}. IB: {self.inbehind}. HU: {self.holdup}.'

    def info(self):
        return f'Age: {self.age}. Yrs: {self.contract}. P: {self.gamesplayed}. W: {self.wins}'

class CLUB:
    def __init__(self, name, abr, qual = 40):
        self.name = name
        self.ABR = abr
        self.league = None
        self.ogqual = qual
        # GAME
        self.score = 0
        # For controlled ----
        self.user = False
        self.goal = 0
        self.ratingAdjustMean = 0
        self.squadGK  = []
        self.squadDEF = []
        self.squadMID = []
        self.squadATT = []
        # For all ----
        self.coach = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 1)])
        # GK
        self.shotstopper = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 1)])
        self.sweeperkeeper = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 1)])
        self.eleventhman = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 1)])
        # DEF
        self.lowblock = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 4)])
        self.possession = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 4)])
        self.overload = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 4)])
        self.longball = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 4)])
        # MID
        self.quick = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.holding = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.control = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.crossing = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        # ATT
        self.routeone = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.false9 = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.inbehind = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        self.holdup = sum([clamp(i, 0, 100) for i in numpy.random.normal(qual, qualitySpread, 3)])
        # FULL
        self.qual = None, None, None, None
        self.roles = None, None, None, None
        self.basetactic = None
        self.baserating = 0
        self.tactic = None
        self.rolesSet(seasonStart=True)

    def __str__(self):
        return f'{self.name} [{round(self.baserating/11)}]'

    def rolesSet(self, opp='No Tactic', seasonStart = False):
        # ['Park The Bus', 'Counter Attack', 'Width', 'Strangle', 'No Tactic']
        bg = max(self.shotstopper, self.sweeperkeeper, self.eleventhman)
        bd = max(self.lowblock, self.possession, self.overload, self.longball)
        bm = max(self.quick, self.holding, self.control, self.crossing)
        ba = max(self.routeone, self.false9, self.inbehind, self.holdup)
        if odds(self.coach / 100) or seasonStart:
            tacAdd = {'No Tactic': TMdf.loc['No Tactic', opp][0], 'Park The Bus': TMdf.loc['Park The Bus', opp][0],
                'Counter Attack': TMdf.loc['Counter Attack', opp][0], 'Width': TMdf.loc['Width', opp][0], 
                'Strangle': TMdf.loc['Strangle', opp][0]}
        else:
            tacAdd = {'No Tactic': 0, 'Park The Bus': 0, 'Counter Attack': 0, 'Width': 0, 'Strangle': 0}
        if self.user or not self.user :
            maxi = bg + bd + bm + ba + tacAdd['No Tactic']
            PTB = self.shotstopper + self.lowblock + self.holding + self.holdup + tacAdd['Park The Bus']
            CA = self.shotstopper + self.longball + self.quick + self.inbehind + tacAdd['Counter Attack']
            WID = self.sweeperkeeper + self.overload + self.crossing + self.routeone + tacAdd['Width']
            STR = self.eleventhman + self.possession + self.control + self.false9 + tacAdd['Strangle']
            best = max(maxi, PTB, CA, WID, STR)
            #print('ere0')
            if closeEnough(best, STR):
                self.roles = 'Eleventh Man', 'Possession', 'Control', 'False 9'
                self.qual = self.eleventhman, self.possession, self.control, self.false9
                self.tactic = 'Strangle'
                if seasonStart:
                    self.basetactic = 'Strangle'
                    self.baserating = sum(self.qual)
            elif closeEnough(best, CA):
                self.roles = 'Shot Stopper', 'Long Ball', 'Quick', 'In Behind'
                self.qual = self.shotstopper, self.longball, self.quick, self.inbehind
                self.tactic = 'Counter Attack'
                if seasonStart:
                    self.basetactic = 'Counter Attack'
                    self.baserating = sum(self.qual)
            elif closeEnough(best, WID):
                self.roles = 'Sweeper Keeper', 'Overload', 'Crossing', 'Route 1'
                self.qual = self.sweeperkeeper, self.overload, self.crossing, self.routeone
                self.tactic = 'Width'
                if seasonStart:
                    self.basetactic = 'Width'
                    self.baserating = sum(self.qual)
            elif closeEnough(best, PTB):
                self.roles = 'Shot Stopper', 'Low Block', 'Holding', 'Holdup'
                self.qual = self.shotstopper, self.lowblock, self.holding, self.holdup
                self.tactic = 'Park The Bus'
                if seasonStart:
                    self.basetactic = 'Park The Bus'
                    self.baserating = sum(self.qual)
            else:
                #print('ere')
                self.roles = (
                    'Shot Stopper' if closeEnough(bg, self.shotstopper) else \
                        'Sweeper Keeper' if closeEnough(bg, self.sweeperkeeper) else \
                        'Eleventh Man',
                    'Low Block' if closeEnough(bd, self.lowblock) else \
                        'Possession' if closeEnough(bd, self.possession) else \
                        'Overload' if closeEnough(bd, self.overload) else \
                        'Long Ball',
                    'Quick' if closeEnough(bm, self.quick) else \
                        'Holding' if closeEnough(bm, self.holding) else \
                        'Control' if closeEnough(bm, self.control) else \
                        'Crossing',
                    'Route 1' if closeEnough(ba, self.routeone) else \
                        'False 9' if closeEnough(ba, self.false9) else \
                        'In Behind' if closeEnough(ba, self.inbehind) else \
                        'Holdup'
                )
                self.qual = self.shotstopper if closeEnough(bg, self.shotstopper) else \
                        self.sweeperkeeper if closeEnough(bg, self.sweeperkeeper) else \
                        self.eleventhman, \
                    self.lowblock if closeEnough(bd, self.lowblock) else \
                        self.possession if closeEnough(bd, self.possession) else \
                        self.overload if closeEnough(bd, self.overload) else \
                        self.longball, \
                    self.quick if closeEnough(bm, self.quick) else \
                        self.holding if closeEnough(bm, self.holding) else \
                        self.control if closeEnough(bm, self.control) else \
                        self.crossing, \
                    self.routeone if closeEnough(ba, self.routeone) else \
                        self.false9 if closeEnough(ba, self.false9) else \
                        self.inbehind if closeEnough(ba, self.inbehind) else \
                        self.holdup
                self.tactic = 'No Tactic'
                if seasonStart:
                    self.basetactic = 'No Tactic'
                    self.baserating = sum(self.qual)
        else:
            pass

    def ratingAdjust(self):

        # For all ----
        self.coach = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.coach/1 + self.ratingAdjustMean, adjustSpread, 1)])
        # GK
        self.shotstopper = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.shotstopper/1 + self.ratingAdjustMean, adjustSpread, 1)])
        self.sweeperkeeper = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.sweeperkeeper/1 + self.ratingAdjustMean, adjustSpread, 1)])
        self.eleventhman = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.eleventhman/1 + self.ratingAdjustMean, adjustSpread, 1)])
        # DEF
        self.lowblock = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.lowblock/4 + self.ratingAdjustMean, adjustSpread, 4)])
        self.possession = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.possession/4 + self.ratingAdjustMean, adjustSpread, 4)])
        self.overload = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.overload/4 + self.ratingAdjustMean, adjustSpread, 4)])
        self.longball = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.longball/4 + self.ratingAdjustMean, adjustSpread, 4)])
        # MID
        self.quick = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.quick/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.holding = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.holding/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.control = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.control/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.crossing = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.crossing/3 + self.ratingAdjustMean, adjustSpread, 3)])
        # ATT
        self.routeone = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.routeone/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.false9 = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.false9/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.inbehind = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.inbehind/3 + self.ratingAdjustMean, adjustSpread, 3)])
        self.holdup = sum([clamp(i, 0, 100) for i in numpy.random.normal(self.holdup/3 + self.ratingAdjustMean, adjustSpread, 3)])
        # FULL
        self.qual = None, None, None, None
        self.roles = None, None, None, None
        self.basetactic = None
        self.baserating = 0
        self.tactic = None
        self.rolesSet(seasonStart=True)

    def tacticSet(self):
        G, D, M, A = self.roles
        if G == 'Shot Stopper':
            if D == 'Low Block':
                if M == 'Holding':
                    if A == 'Holdup':
                        self.tactic = 'Park The Bus'
                    else:
                        self.tactic = 'No Tactic'
                else:
                    self.tactic = 'No Tactic'
            elif D == 'Long Ball':
                if M == 'Quick':
                    if A == 'In Behind':
                        self.tactic = 'Counter Attack'
                    else:
                        self.tactic = 'No Tactic'
                else:
                    self.tactic = 'No Tactic'
            else:
                self.tactic = 'No Tactic'
        elif G == 'Sweeper Keeper':
            if D == 'Overload':
                if M == 'Crossing':
                    if A == 'Route 1':
                        self.tactic = 'Width'
                    else:
                        self.tactic = 'No Tactic'
                else:
                    self.tactic = 'No Tactic'
            else:
                self.tactic = 'No Tactic'
        elif G == 'Eleventh Man':
            if D == 'Possession':
                if M == 'Control':
                    if A == 'False 9':
                        self.tactic = 'Strangle'
                    else:
                        self.tactic = 'No Tactic'
                else:
                    self.tactic = 'No Tactic'
            else:
                self.tactic = 'No Tactic'
        else:
            self.tactic = 'No Tactic'

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
    
