
from Objects import *

class vWall:
    def __init__(self, x, y1, y2, direct, flag=1):
        self.x = x
        self.top = y1
        self.bot = y2
        self.dir = direct
        self.topSpot = Spot(x, y1)
        self.botSpot = Spot(x, y2)
        self.start = (x, y1)
        self.end = (x, y2)
        self.mid = (x, .5 * (y1 + y2))
        self.flag = flag
        self.dpoint = (x + (20+(30*flag))*direct, .5 * (y1 + y2))

    def withinY(self, thing):
        if self.top <= thing.y <= self.bot:
            return True
        elif distanceFormula(thing, self.topSpot) <= thing.rad:
            return True
        elif distanceFormula(thing, self.botSpot) <= thing.rad:
            return True
        else:
            return False

    def isTouching(self, thing):
        if self.dir == 1:
            if self.x - 5 - (20*self.flag) <= thing.x - thing.rad <= self.x and self.withinY(thing):
                thing.xV = abs(thing.xV)
        else:
            if self.x + 5 + (20*self.flag) >= thing.x + thing.rad >= self.x and self.withinY(thing):
                thing.xV = -abs(thing.xV)


class hWall:
    def __init__(self, y, x1, x2, direct, flag=1):
        self.y = y
        self.left = x1
        self.right = x2
        self.dir = direct  # 1 or -1
        self.leftSpot = Spot(x1, y)
        self.rightSpot = Spot(x2, y)
        self.start = (x1, y)
        self.end = (x2, y)
        self.mid = (.5*(x1+x2), y)
        self.flag = flag
        self.dpoint = (.5*(x1+x2), y + (20+(30*flag))*direct)

    def withinX(self, thing):
        if self.left <= thing.x <= self.right:
            return True
        elif distanceFormula(thing, self.leftSpot) <= thing.rad:
            return True
        elif distanceFormula(thing, self.rightSpot) <= thing.rad:
            return True
        else:
            return False

    def isTouching(self, thing):
        if self.dir == 1:
            if self.y - 5 - (20*self.flag) <= thing.y - thing.rad <= self.y and self.withinX(thing):
                thing.yV = abs(thing.yV)
        else:
            if self.y + 5 + (20*self.flag) >= thing.y + thing.rad >= self.y and self.withinX(thing):
                thing.yV = -abs(thing.yV)

split = 25  # Milliseconds
gameTime = 90000  # splits
#gameTime *= 1000  # Milliseconds
kickoffDelay = 1000
accel = .1
decel = .02

goalTop = screen[1]*.5 - 80
goalBot = screen[1]*.5 + 80
goalBack = -50
goalFront = 30
walls = [vWall(30, 0, goalTop, 1), vWall(screen[0]-30, 0, goalTop, -1), 
         vWall(30, goalBot, screen[1], 1), vWall(screen[0]-30, goalBot, screen[1], -1), 
         hWall(0, 0, screen[0], 1), hWall(screen[1], 0, screen[0], -1)
         #hWall(goalTop, goalBack, goalFront, -1), hWall(goalBot, goalBack, goalFront, 1)
         #hWall(goalTop, goalBack, goalFront, 1, flag=0), hWall(goalBot, goalBack, goalFront, -1, flag=0),
         #vWall(goalBack, goalTop, goalBot, -1), vWall(goalBack + 30, goalTop, goalBot, 1, flag=0),
         #hWall(goalTop, screen[0]-goalFront, screen[0]-goalBack, -1), hWall(goalBot, screen[0]-goalFront, screen[0]-goalBack, 1),
         #hWall(goalTop, screen[0]-goalFront, screen[0]-goalBack, 1, flag=0), hWall(goalBot, screen[0]-goalFront, screen[0]-goalBack, -1, flag=0),
         #vWall(screen[0]-goalBack, goalTop, goalBot, 1), vWall(screen[0]-goalBack - 30, goalTop, goalBot, -1, flag=0)
         ]

class Disc:
    def __init__(self, qual, abr='N/A', pos=1, cont=False):
        self.name = names.get_full_name()
        while len(self.name) != 15:
            if len(self.name) > 15:
                self.name = names.get_full_name()
            else:
                self.name = self.name + ' '
        self.team = abr
        self.side = 0
        self.x = 0
        self.y = 0
        self.startX = 0
        self.startY = 0
        self.color = (0, 0, 0)
        self.rad = 25
        self.pow = round(.8*math.sqrt(qual), 1)
        self.speed = round(.8*math.sqrt(qual), 1)
        #self.smart = 10
        self.xV = 0
        self.yV = 0
        self.timeSinceHit = 0
        self.controlled = cont
        self.pos = pos
        # STATS
        self.goals = 0
        self.ownGoals = 0

    def inRangeOf(self, thing):
        if distanceFormula(self, thing) <= self.rad+thing.rad:  # hit
            return True
        else:
            return False

    def canCover(self, spot, splits):
        xDiff = spot.x - self.x
        yDiff = spot.y - self.y
        angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
        angle += math.pi / 4 if xDiff < 0 else 0
        mag = pythag(xDiff, yDiff) - 45
        if mag/self.speed <= splits:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def statline(self):
        return f'{self.team} {self.name} {self.goals} {self.ownGoals}'


class Ball:
    def __init__(self, x=screen[0]*.5, y=screen[1]*.5, color=WhiteC):
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        self.xV = 0
        self.yV = 0
        self.dir = 0
        self.color = color
        self.rad = 5
        self.controlled = False



def BallVec(T, velo, pos, axis=0):
    p = velo*T + pos
    while numpy.any(p < 0) or numpy.any(p > screen[axis]):
        p = numpy.where(p < 0, -p, p)
        p = numpy.where(p > screen[axis], screen[axis] - (p - screen[axis]), p)
    return p

def movementDec(discs, ball, surface):
    for disc in discs:
        if disc.controlled:
            continue # gets set later
        Time = range(1001)
        xGoal = goalFront if disc.side == 1 else screen[0]-goalFront
        yGoal = (goalTop+goalBot)/2
        xDef = goalFront+20 if disc.side ==  -1 else screen[0]-goalFront-20
        yDef = (goalTop+goalBot)/2
        # Ball Vector
        df = pandas.DataFrame({'Time': Time})
        df['x'] = BallVec(df.Time, ball.xV, ball.x, 0)
        df['y'] = BallVec(df.Time, ball.yV, ball.y, 1)
        # Back Wall Timing
        data = pandas.DataFrame({'Time': Time})
        data['x'] = ball.xV * data['Time'] + ball.x
        WhenBackWall = data.loc[(data['x'] < 0) | (data['x'] > 2*screen[0]), 'Time'].min()
        if WhenBackWall is numpy.nan:
            WhenBackWall = 10000
        # mutate df
        ballToGoalX = xGoal - df.x
        ballToGoalY = yGoal - df.y
        ballToGoal = numpy.sqrt(ballToGoalX**2 + ballToGoalY**2)
        scale = disc.rad / (ballToGoal + 0.00001)
        tarX = df.x - (ballToGoalX * scale)
        tarY = df.y - (ballToGoalY * scale)
        spotToTar = numpy.sqrt((tarX - disc.x)**2 + (tarY - disc.y)**2)
        timeToTar = spotToTar / disc.speed
        # Make choice
        choice = pandas.DataFrame({'Time': Time, 'x': round(tarX), 'y': round(tarY), 'Time.Tar': round(timeToTar)})
        choice['Possible'] = (choice['Time.Tar'] < choice['Time']) & \
            (choice['x'] > 0) & (choice['x'] < screen[0]) & \
            (choice['y'] > 0) & (choice['y'] < screen[1])
        
        choice = choice[choice['Possible']].sort_values(by='Time')
        #texts = dataframe_to_aligned_strings_with_headers(choice.iloc[:20, :])
        #for i in range(len(texts)):
        #    text(texts[i], (800, 300 + 40*i), 12, surface)
        if not choice.empty: # Select the first row (if exists)
            choice = choice.iloc[[0]]
        else:
            choice = pandas.DataFrame(columns=['Time', 'x', 'y', 'Time.Tar'])
        tChoice = choice['Time'].values[0] if not choice.empty else 10000
        if tChoice < WhenBackWall:
            xChoice = choice['x'].values[0] if not choice.empty else xDef
            yChoice = choice['y'].values[0] if not choice.empty else yDef
        else:
            xChoice = xDef
            yChoice = yDef
        
        yDist = yChoice - disc.y
        xDist = xChoice - disc.x
        aDist = numpy.sqrt(yDist**2 + xDist**2)
        # Calculate speed 
        if tChoice < WhenBackWall:
            speed = aDist / tChoice
        else:
            speed = disc.speed
        angle = numpy.arctan2(yDist, xDist)  # Using arctan2 for correct quadrant
        disc.xV = speed * numpy.cos(angle)
        disc.yV = speed * numpy.sin(angle)
        pygame.draw.line(surface, WhiteC, (disc.x, disc.y), (xChoice, yChoice), 2)
        


def reset(things, spot=0):
    for i in things:
        i.x = i.startX
        i.y = i.startY
        i.xV = 0
        i.yV = 0
        if isinstance(i, Ball):
            side = spot if spot != 0 else random.choice([1, -1])
            i.x = numpy.random.normal(screen[0] * .5 + (side * screen[0] * .15), screen[0] * .05)
            i.y = numpy.random.normal(.5 * screen[1], .1 * screen[1])
    


def usrgame(left, right, ET=False):
    elapsed = 0
    leftDisc = Disc(left.baserating/11, abr = left.ABR, cont = left.user)
    rightDisc = Disc(right.baserating/11, abr = right.ABR, cont = right.user)
    dud = input(f'{left.ABR} v {right.ABR} starting now')
    pygame.init()
    out = pygame.display.set_mode((screen[0], screen[1]))
    pygame.display.set_caption(f'{left.ABR} v {right.ABR}; ')
    ball = Ball()
    leftDisc.color = GreenC
    leftDisc.side = -1
    (leftDisc.startX, leftDisc.startY) = (.2, .5)
    leftDisc.startX *= screen[0]
    leftDisc.startY *= screen[1]
    rightDisc.color = OrangeC
    rightDisc.side = 1
    (rightDisc.startX, rightDisc.startY) = (.2, .5)
    rightDisc.startX = (1 - rightDisc.startX) * screen[0]
    rightDisc.startY = (1 - rightDisc.startY) * screen[1]
    discs = [leftDisc, rightDisc]
    things = discs + [ball]
    time = 0
    note = ''
    kill = False
    reset(things)
    barrierCrosses = 0
    while (time < gameTime or (left.score == right.score and ET)) and not kill:
        hits = False
        flag = False
        #pygame.time.delay(split)
        if time == 0:
            reset(things)
            barrierCrosses = 0
        time += split
        elapsed += split / 1000
        outTime = int(time / 1000) if time >= 0 else 'OT'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill = True
        out.fill(BlackC)
        out.fill((85, 194, 194), (goalBack+40, goalTop + 5, goalFront-goalBack-45, goalBot-goalTop-10))
        out.fill((85, 194, 194), (screen[0] - goalFront + 5, goalTop + 5, goalFront - goalBack - 45, goalBot - goalTop - 10))
        for thing in things:
            pygame.draw.circle(out, thing.color, [thing.x, thing.y], thing.rad)
            if thing.controlled:
                text(f'YOU', (thing.x, thing.y), 12, out)
            elif isinstance(thing, Disc):
                text(f'OPP', (thing.x, thing.y), 12, out)
        text(f'{left.score}    {outTime}    {right.score}', (screen[0] // 2, 50), 32, out)
        text(f'{left}', (screen[0] * .2, 50), 32, out)
        l1, l2, l3 = left.league.standings.loc[left].Points, list(left.league.standings.index).index(left) + 1, left.league.abr
        text(f'{l1} pts, #{l2} in {l3}', (screen[0] * .2, 100), 24, out)
        text(f'{leftDisc.pow} {leftDisc.speed}', (screen[0] * .2, 75), 16, out)
        text(f'{right}', (screen[0] * .8, 50), 32, out)
        r1, r2, r3 = right.league.standings.loc[right].Points, list(right.league.standings.index).index(right) + 1, right.league.abr
        text(f'{r1} pts, #{r2} in {r3}', (screen[0] * .8, 100), 24, out)
        text(f'{rightDisc.pow} {rightDisc.speed}', (screen[0] * .8, 75), 16, out)
        for wall in walls:
            pygame.draw.line(out, WhiteC, wall.start, wall.end)
        for item in discs:
            if item.inRangeOf(ball) and not hits and item.timeSinceHit == 0:  # Does it hit the ball
                flag = True
                item.timeSinceHit = 3
                for item2 in discs:
                    if item != item2 and item2.inRangeOf(ball): # 2 hit the ball at same time
                        item2.timeSinceHit = 3
                        hits = True
                        xDiff = (ball.x - item.x) + (ball.x - item2.x)
                        yDiff = (ball.y - item.y) + (ball.y - item2.y)
                        angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
                        angle = angle + (math.pi if xDiff < 0 else 0)
                        veloMag = pythag(item.xV + item2.xV, item.yV + item2.yV)  # No idea if this'll work
                        veloDir = math.atan(item.yV + item2.yV / item.xV + item2.xV) if item.xV != 0 else math.pi / 4
                        veloDir = veloDir + (math.pi if item.xV + item2.xV < 0 else 0)
                        ballVelo = abs(veloMag * math.cos(veloDir - angle)) + (item.pow + item2.pow)
                        ball.xV = ballVelo * math.cos(angle)
                        ball.yV = ballVelo * math.sin(angle)
                if not hits: # just one hits ball
                    xDiff = ball.x - item.x
                    yDiff = ball.y - item.y
                    angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
                    angle = angle + (math.pi if xDiff < 0 else 0) # atan adjust
                    veloMag = math.sqrt(item.xV ** 2 + item.yV ** 2) # how fast is the disc going
                    veloDir = math.atan(item.yV / item.xV) if item.xV != 0 else math.pi / 4 # what dir is the disc going
                    veloDir = veloDir + (math.pi if item.xV < 0 else 0) # atan adjust
                    ballVelo = abs(.1*item.pow * (1+veloMag) * math.cos(veloDir - angle)) + abs(veloMag) # cos for a power adjustment based on lining up disc angle
                    if ball.rad >= ball.x or ball.x + ball.rad >= screen[0] or ball.rad >= ball.y or ball.y + ball.rad >= screen[1]: # PINCH
                        ballVelo += 6 # make it go real fast
                        if ball.rad >= ball.x: # Adjust angle... i dont really get this
                            angle += math.pi / 2 if item.yV < 0 else -math.pi / 2
                        elif ball.x + ball.rad >= screen[0]:
                            angle += math.pi / 2 if item.yV > 0 else -math.pi / 2
                        elif ball.rad >= ball.y:
                            angle += math.pi / 2 if item.xV > 0 else -math.pi / 2
                        else:
                            angle += math.pi / 2 if item.xV < 0 else -math.pi / 2
                    ball.xV = ballVelo * math.cos(angle)
                    ball.yV = ballVelo * math.sin(angle)
            for target in discs:  # Does it hit another disc, problem with no acceleration?
                continue # skip for now
                if item != target and item.inRangeOf(target):
                    velo = item.pow / 2
                    xDiff = target.x - item.x
                    yDiff = target.y - item.y
                    if xDiff != 0:
                        angle = math.atan(yDiff / xDiff)
                        target.xV = velo * math.cos(angle)
                        target.yV = velo * math.sin(angle)
                    else:
                        target.xV = 0
                        target.yV = velo * (1 if yDiff > 0 else -1)
                    if xDiff < 0:
                        target.xV *= -1
                        target.yV *= -1
        # Now move the things
        movementDec(discs, ball, out)
        keys = pygame.key.get_pressed()
        for thing in discs:
            thing.timeSinceHit = max(thing.timeSinceHit-1, 0)
            if thing.controlled: # overwrite for usercontrolled
                thing.xV, thing.yV = 0, 0
                dirs = keys[pygame.K_LEFT] + keys[pygame.K_RIGHT] + keys[pygame.K_UP] + keys[pygame.K_DOWN]
                mul = 1 / math.sqrt(2) if dirs == 2 else 1
                curspeed = thing.speed * mul
                if keys[pygame.K_LEFT]:
                    thing.xV = -curspeed
                if keys[pygame.K_RIGHT]:
                    thing.xV = curspeed
                if keys[pygame.K_UP]:
                    thing.yV = -curspeed
                if keys[pygame.K_DOWN]:
                    thing.yV = curspeed
        for thing in things:  # Move the stuff
            thing.x += thing.xV
            thing.y += thing.yV
            for wall in walls:
                wall.isTouching(thing)
            if thing.x < 0 or thing.x > screen[0] or thing.y < 0 or thing.y > screen[1]:  # Something is stuck
                barrierCrosses += 1
            if barrierCrosses > 300:
                reset(things)
                barrierCrosses = 0
        text(f'{barrierCrosses}', (300, 300), 32, out)
        if goalFront - 5 >= ball.x >= goalBack+40 and goalTop+5 <= ball.y <= goalBot-5:  # Goal
            right.score += 1
            reset(things, spot=-1)
            barrierCrosses = 0
        elif screen[0]-goalFront+5 <= ball.x <= screen[0]-goalBack-40 and goalTop+5 <= ball.y <= goalBot-5:
            left.score += 1
            reset(things, spot=1)
            barrierCrosses = 0
        pygame.display.update()
    pygame.quit()
    if time > gameTime:
        note = 'a.e.t.'
    return [left, left.score, right.score, right, note]


def distanceFormula(thing1, thing2):
    return math.sqrt((thing1.x-thing2.x)**2 + (thing1.y-thing2.y)**2)


class Spot:  # So you can put it in the distance formula
    def __init__(self, x, y, rad=0):
        self.x = x
        self.y = y
        self.rad = rad





