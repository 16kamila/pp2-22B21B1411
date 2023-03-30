import pygame
pygame.init()
pygame.display.set_caption("ball")

scr_x=650
scr_y=450
scr=pygame.display.set_mode((scr_x,scr_y))

window=True
clock=pygame.time.Clock()
scr.fill((22, 51, 17))

r=50
x=scr_x/2
y=scr_y/2

while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window=False

    press=pygame.key.get_pressed()
    if press[pygame.K_UP]:y-=10
    if press[pygame.K_DOWN]:y+=10
    if press[pygame.K_RIGHT]:x+=10
    if press[pygame.K_LEFT]:x-=10
    scr.fill((22, 51, 17))

    if x<r:x=r
    if y<r:y=r
    if x>scr.get_width()-r:x=scr.get_width()-r
    if y>scr.get_height()-r:y=scr.get_height()-r

    pygame.draw.circle(scr,(81,150,69),(x,y),r)
    pygame.display.flip()
    clock.tick(100)