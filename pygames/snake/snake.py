import math
import random
import pygame
#import OpenGL
import tkinter as tk
from tkinter import messagebox
import sys
from os import path
print(path.abspath(path.dirname(__file__)))
sys.path.append(path.abspath(path.dirname(__file__))) #APPEND Path for looking for modules
from assets.gameobjects import snake as snake 
from assets.gameobjects import cube as cube 
#pygame.init()
#print("USING PYGAME VERSION: {}".format(pygame.ver))

print(sys.version)


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, WHITE, (x,0), (x,w), 1)
        pygame.draw.line(surface, WHITE, (0,y), (w,y), 1)

def redrawWindow(surface):  
    surface.fill(BLACK)

    myfont = pygame.font.Font(pygame.font.get_default_font(), 36) 
    textsurface = myfont.render('SNAKE', True, BLUE)
    surface.blit(textsurface,(windowWidth // 2 - 70, 0))
    
        
    s.draw(surface)
    snack.draw(surface)
    drawGrid(windowWidth, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
       
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():  
    global rows, windowWidth, s, snack
    windowWidth = 500
    windowHeight = 500
    rows = 20
    pygame.init()
    win = pygame.display.set_mode(size=(windowWidth, windowHeight))
    s = snake(RED, (10,10))
    snack = cube(randomSnack(rows, s), color=GREEN)
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(100)
        clock.tick(10)
        s.move()

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=GREEN)
 
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score: ", len(s.body))
                message_box("You Lost!", "Play again?")
                s.reset((10,10))
                break
 
           
        redrawWindow(win)

#start main()    
main()
