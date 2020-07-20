import pygame

width = 500
height = 500


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height) 
        self.vel = 3
        self.pos = (x, y)
        self.selected = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.selected:
            new_rect = pygame.Rect(self.x, self.y, self.width -1 , self.height -1) 
            pygame.draw.rect(win, WHITE, new_rect, 2)

    def move(self, relX = 0, relY = 0, pressedKeys = {}):      
        if relX != 0:
            self.x += relX
        if relY != 0:
            self.y += relY

        if pressedKeys.get(pygame.K_LEFT):
            self.x -= self.vel                                   
        if pressedKeys.get(pygame.K_RIGHT):
            self.x += self.vel 
        if pressedKeys.get(pygame.K_UP):
            self.y -= self.vel 
        if pressedKeys.get(pygame.K_DOWN):
            self.y += self.vel  
        if pressedKeys.get(pygame.K_ESCAPE):
            self.selected = False     

        #print("x: {} y: {}".format(self.x, self.y))
        #Just Force to not get out of bounds
        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > width - self.width: self.x = (width - self.width)
        if self.y > (height - self.height): self.y = (height - self.height)
        
        self.update()

    #redraw
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width , self.height)
        self.pos = (self.x, self.y)