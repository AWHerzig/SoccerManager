from Matchup import *

qualitySpread = 0

class GK:
    def __init__(self):
        self.name = 'NAME'
        self.POS = 'GK'
        self.shotstopper = 5
        self.sweeperkeeper = 5
        self.eleventhman = 5

class DEF:
    def __init__(self):
        self.name = 'NAME'
        self.POS = 'DEF'
        self.lowblock = 5
        self.possession = 5
        self.overload = 5
        self.longball = 5

class MID:
    def __init__(self):
        self.name = 'NAME'
        self.POS = 'MID'
        self.quick = 5
        self.holding = 5
        self.control = 5
        self.crossing = 5

class ATT:
    def __init__(self):
        self.name = 'NAME'
        self.POS = 'ATT'
        self.routeone = 5
        self.false9 = 5
        self.inbehind = 5
        self.holdup = 5

class CLUB:
    def __init__(self, name, abr, qual = 70):
        self.name = name
        self.ABR = abr
        # GAME
        self.score = 0
        # For controlled ----
        self.user = False
        self.squadGK  = []
        self.squadDEF = []
        self.squadMID = []
        self.squadATT = []
        # For all ----
        self.coach = sum(numpy.random.normal(qual, qualitySpread, 1))
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
        return self.name

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
        if not self.user:
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
    
