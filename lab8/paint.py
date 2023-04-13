import pygame
import random
pygame.init()
clock=pygame.time.Clock()
scrx,scry=600,600
screen=pygame.display.set_mode((scrx, scry))
bg="White"
screen.fill(bg)
window=True

random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#varibles for my pen type and color
color="Red"
mode="Pen"

#tuple and list to store position of the mouse when its clicked and points[] to store where the pen draw
pos=()
points=[]

#for rectangle
rect_w=0
rect_h=0

#2 functions for eraser and pen
def eraser(pos):
    pygame.draw.circle(screen,bg,pos,15)
def pen(pos, color):
    pygame.draw.circle(screen,color,pos,10)


while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                color=((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            elif event.key == pygame.K_w:
                color="Green"
            elif event.key == pygame.K_e:
                color="Blue"

            if event.key == pygame.K_1:
                mode = "Circle"
            elif event.key == pygame.K_2:
                mode = "Pen"
            elif event.key == pygame.K_3:
                mode = "Rect"
            elif event.key == pygame.K_4:
                mode = "Eraser"

        if event.type==pygame.MOUSEBUTTONDOWN and mode=="Circle":
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen, color, pos, 30)
        elif event.type == pygame.MOUSEBUTTONDOWN and mode == "Rect":
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, color, (pos[0], pos[1], 80, 60))

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
            pos = pygame.mouse.get_pos()
            if mode == "Pen":
                pen(pos, color)
            if mode == "Eraser":
                eraser(pos)
    # clock.tick(500)
    pygame.display.flip()