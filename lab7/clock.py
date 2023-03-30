import pygame
import sys
from datetime import datetime
import math
pygame.init()
scr_x=600
scr_y=600
scr=pygame.display.set_mode((scr_x,scr_y))
clock = pygame.time.Clock()
window=True
# now=datetime.now()


while window:
    now=datetime.now()
    now_sec=now.second
    now_min=now.minute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window=False
    clock_image=pygame.transform.scale(pygame.image.load('images/clock.png'), (scr_x, scr_y))
    scr.blit(clock_image, (0, 0))

    sec=pygame.image.load('images/hand_1.png')
    sec=pygame.transform.scale(sec,(350,100))
    sec2 = sec.get_rect(center=(scr_x / 2 - 20, scr_y / 2))
    min=pygame.image.load('images/hand_2.png')
    min=pygame.transform.scale(min,(350, 80))
    min2=min.get_rect(center=(scr_x / 2 + 20, scr_y / 2))

    secpos = pygame.transform.rotate(sec, -1 *(6*now_sec)+90)
    secpos2 = secpos.get_rect()
    secpos2.center = sec2.center
    scr.blit(secpos, secpos2)
    minpos=pygame.transform.rotate(min, -1*(6 *now_min)-160)
    minpos2=minpos.get_rect()
    minpos2.center=min2.center
    scr.blit(minpos,minpos2)

    pygame.display.flip()
    clock.tick(100)


