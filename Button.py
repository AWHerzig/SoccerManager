from DirWide import *
# like DirWide2 btw but button specific cuz shit gets funky
# And the startup is here

class Box:
    def __init__(self, show, loc, be = None):
        self.show = show
        self.be = be if be is not None else show
        self.loc = loc  # [L, R, T, B]

    def draw(self, col = WhiteC):
        pygame.draw.line(out, col, (self.loc[0], self.loc[2]), (self.loc[0], self.loc[3]))
        pygame.draw.line(out, col, (self.loc[1], self.loc[2]), (self.loc[1], self.loc[3]))
        pygame.draw.line(out, col, (self.loc[0], self.loc[2]), (self.loc[1], self.loc[2]))
        pygame.draw.line(out, col, (self.loc[0], self.loc[3]), (self.loc[1], self.loc[3]))
        text(self.show, (stats.mean(self.loc[:2]), stats.mean(self.loc[2:])), 20, out, col)

    def hover(self, col = WhiteC):
        widthadd = .1 * (self.loc[1] - self.loc[0])
        heightadd = .1 * (self.loc[3] - self.loc[2])
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[2] - heightadd), (self.loc[0] - widthadd, self.loc[3] + heightadd))
        pygame.draw.line(out, col, (self.loc[1] + widthadd, self.loc[2] - heightadd), (self.loc[1] + widthadd, self.loc[3] + heightadd))
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[2] - heightadd), (self.loc[1] + widthadd, self.loc[2] - heightadd))
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[3] + heightadd), (self.loc[1] + widthadd, self.loc[3] + heightadd))
        text(self.show, (stats.mean(self.loc[:2]), stats.mean(self.loc[2:])), 24, out, col)

    def click(self):
        if inspect.isfunction(self.be):
            return self.be()
        else:
            return self.be

    def inme(self, point):
        if self.loc[0] <= point[0] <= self.loc[1] and self.loc[2] <= point[1] <= self.loc[3]:
            return True
        else:
            return False

def buttons(out, title, options, retop=True):
    if len(options) > 8:
        raise ValueError('Can only do 8 buttons at a time')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = pygame.mouse.get_pos()
                if 100 <= spot[0] <= 900 and 100 <= spot[1] <= 600:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click on option to make selection', (500, 25), 15, out)
        text(title, (500, 75), 32, out)
        #Start Lines
        # Core 4
        pygame.draw.line(out, BlackC, (100, 100), (100, 600))
        pygame.draw.line(out, BlackC, (100, 100), (900, 100))
        pygame.draw.line(out, BlackC, (900, 600), (100, 600))
        pygame.draw.line(out, BlackC, (900, 600), (900, 100))
        # Vertical Splits
        pygame.draw.line(out, BlackC, (300, 100), (300, 600))
        pygame.draw.line(out, BlackC, (500, 100), (500, 600))
        pygame.draw.line(out, BlackC, (700, 100), (700, 600))
        # Horizontal Split
        if len(options) > 4:
            pygame.draw.line(out, BlackC, (100, 350), (900, 350))
        #End Lines
        #Start Text
        for block in range(len(options)):
            text(options[block], (200 + 200*(block%4), 350 if len(options) <= 4 else 175 + 350*(block//4)), 32, out)
        pygame.display.update()
    grid = (spot[0]-100)//200, int(spot[1] > 350) if len(options) > 4 else 0
    ind = grid[0] + 4*grid[1]
    return options[ind] if retop else ind

def buttons2(boxes, txt = '', fillcol = BlackC, textcol = WhiteC):
    run = True
    while run:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(fillcol)
        text(txt, (screen[0]/2, 100), 40, out, WhiteC)
        mousepoint = pygame.mouse.get_pos()
        for box in boxes:
            if click and box.inme(mousepoint):
                return box.click()
            if box.inme(mousepoint):
                box.hover()
            else:
                box.draw()
        pygame.display.update()


# TURN OF FOR TESTING
#"""
pygame.init()

out = pygame.display.set_mode(screen)
pygame.display.set_caption('HERZIG SOCCER')
kill = False
checkpoint('HERZIG SOCCER 2025 v0.1', out = out)
mode = buttons2([Box('Manager Mode', [100, 500, 200, 600]), Box('Simulator Mode', [700, 1100, 200, 600])], 'SELECT GAME MODE')
##

