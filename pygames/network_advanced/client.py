import pygame
import time
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Client")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pressedKeys = {}
pressedMouseButtons = {}



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
            player.move(mx, my, pressedKeys)

            

def main():
    run = True
    n = Network()    
    p1 = n.getP()
    clock = pygame.time.Clock()
   

    while run:  
        clock.tick(60)
        p2 = n.send(p1)           
        captureEvents(win, p1)
        p1.move(pressedKeys = pressedKeys)
        redrawWindow(win, p1, p2) 
        
        


main()
