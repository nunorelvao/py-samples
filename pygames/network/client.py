import pygame
import time
from network import Network

width = 500
height = 500
win = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Client")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

clientNumber = 0
pressedKeys = {}
pressedMouseButtons = {}

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
            pygame.draw.rect(win, RED, new_rect, 2)

    def move(self, relX = 0, relY = 0):      
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
       
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1]) 

def redrawWindow(win, p1, p2):
    win.fill(BLACK)
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()


def captureEvents(win, player):    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()  
        if event.type == pygame.KEYUP:
            pressedKeys[event.key] = False
        if event.type == pygame.KEYDOWN:
            pressedKeys[event.key] = True
        if event.type == pygame.MOUSEBUTTONDOWN:           
            mouse_pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            #print("event at: {} , Palyer 1 at: {}".format(mouse_pos, player.pos))
            pressedMouseButtons["button1"] = pressed1
            pressedMouseButtons["button2"] = pressed2
            pressedMouseButtons["button3"] = pressed3
            #print("MOUSEBUTTONDOWN MB1: {}, MB2: {}, MB3: {}".format(pressedMouseButtons.get("button1"), pressedMouseButtons.get("button2"),pressedMouseButtons.get("button3")))

            if player.rect.collidepoint(mouse_pos):               
                if player.selected:
                    player.selected = False
                elif player.selected == False:
                    player.selected = True


        if event.type == pygame.MOUSEBUTTONUP:           
            mouse_pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            #print("event at: {} , Palyer 1 at: {}".format(mouse_pos, player.pos))
            pressedMouseButtons["button1"] = pressed1
            pressedMouseButtons["button2"] = pressed2
            pressedMouseButtons["button3"] = pressed3
            #print("MOUSEBUTTONUP MB1: {}, MB2: {}, MB3: {}".format(pressedMouseButtons.get("button1"), pressedMouseButtons.get("button2"),pressedMouseButtons.get("button3")))
        
        if event.type == pygame.MOUSEMOTION and player.selected:
            mx, my = (event.rel)            
            player.move(mx, my)

            

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p1 = Player(startPos[0], startPos[1], 100, 100, GREEN)
    p2 = Player(0, 0, 100, 100, RED)
    clock = pygame.time.Clock()
   

    while run:  
        clock.tick(60)
        
        p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        print("UPDATE  P2: ({},{})".format( p2.x, p2.y))
        p2.update()
        
        captureEvents(win, p1)

        p1.move()
        redrawWindow(win, p1, p2) 
        
        


main()
