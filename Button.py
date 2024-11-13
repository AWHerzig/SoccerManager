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
        if isinstance(self.show, list):
            #print(self.show, list)
            for txt in self.show:
                text(txt[0], txt[1], txt[2], out)
        else:
            text(self.show, (stats.mean(self.loc[:2]), stats.mean(self.loc[2:])), 20, out, col)

    def hover(self, col = WhiteC):
        widthadd = .1 * (self.loc[1] - self.loc[0])
        heightadd = .1 * (self.loc[3] - self.loc[2])
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[2] - heightadd), (self.loc[0] - widthadd, self.loc[3] + heightadd))
        pygame.draw.line(out, col, (self.loc[1] + widthadd, self.loc[2] - heightadd), (self.loc[1] + widthadd, self.loc[3] + heightadd))
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[2] - heightadd), (self.loc[1] + widthadd, self.loc[2] - heightadd))
        pygame.draw.line(out, col, (self.loc[0] - widthadd, self.loc[3] + heightadd), (self.loc[1] + widthadd, self.loc[3] + heightadd))
        if isinstance(self.show, list):
            for txt in self.show:
                text(txt[0], txt[1], txt[2], out)
        else:
            text(self.show, (stats.mean(self.loc[:2]), stats.mean(self.loc[2:])), 20, out, col)

    def click(self):
        if inspect.isfunction(self.be) or inspect.ismethod(self.be):
            return self.be()
        else:
            return self.be

    def inme(self, point):
        if self.loc[0] <= point[0] <= self.loc[1] and self.loc[2] <= point[1] <= self.loc[3]:
            return True
        else:
            return False

"""

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
"""
#pygame.init()

#out = pygame.display.set_mode(screen)
#pygame.display.set_caption('HERZIG SOCCER')
kill = False
#checkpoint('HERZIG SOCCER 2025 v0.1', out = out)

def renderDF(df, viewport_y):
    SCREEN_HEIGHT = 700
    font = pygame.font.Font('freesansbold.ttf', 24)
    LINE_HEIGHT = font.get_linesize()
    # Calculate column widths based on content and headers
    total_height = (len(df) + 1) * LINE_HEIGHT  # +1 for header
    
    # Create a surface to render the visible portion of the DataFrame
    surface = pygame.Surface((1000, SCREEN_HEIGHT))
    surface.fill(BlackC)  # Fill with white background
    
    # Render headers
    for i, col in enumerate(df.columns):
        text_surface = font.render(f"{col}", True, WhiteC)
        surface.blit(text_surface, (i * 150, 0))  # Adjust position as needed
    
    # Render data rows within the viewport
    start_index = max(0, viewport_y)
    end_index = min(len(df), start_index + (SCREEN_HEIGHT // LINE_HEIGHT) + 1)
    
    for index in range(start_index, end_index):
        row = df.iloc[index]
        for i, col in enumerate(df.columns):
            text_surface = font.render(f"{str(row[col])}", True, WhiteC)
            surface.blit(text_surface, (i * 150, (index - start_index + 1) * LINE_HEIGHT))  # Adjust position as needed
    
    return surface


class Screen:
    def __init__(self, boxes, texts, surfaces = [], fillcol = BlackC, textcol = WhiteC, spot = 'center'):
        self.boxes = boxes
        self.texts = texts
        self.surfaces = surfaces
        self.fillcol = fillcol
        self.textcol = textcol
        self.spot = spot

    def goto(self):
        run = True
        viewport_y = 0
        SCROLL_SPEED = 1
        while run:
            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        viewport_y -= SCROLL_SPEED
                    elif event.key == pygame.K_DOWN:
                        viewport_y += SCROLL_SPEED
            out.fill(self.fillcol)
            for txt in self.texts:
                text(txt[0], txt[1], txt[2], out, self.textcol, self.spot)
            for surf in self.surfaces:
                out.blit(renderDF(surf[0], viewport_y), (surf[1], surf[2]))
            mousepoint = pygame.mouse.get_pos()
            for box in self.boxes:
                if click and box.inme(mousepoint):
                    return box.click()
                if box.inme(mousepoint):
                    box.hover()
                else:
                    box.draw()
            pygame.display.update()

    def kill(self):
        return 'done'




# TURN OF FOR TESTING
#"""

#modescreen = Screen([Box('Manager Mode', [100, 500, 200, 600]), Box('Simulator Mode', [700, 1100, 200, 600])], [('SELECT GAME MODE', (600, 100), 40)])
#mode = modescreen.goto()
##

