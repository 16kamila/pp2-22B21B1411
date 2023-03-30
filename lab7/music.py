import pygame
import sys
pygame.init()
window=True
pygame.display.set_caption("muzika")
scr_x,scr_y=650,400
scr=pygame.display.set_mode((scr_x,scr_y))
background=pygame.transform.scale(pygame.image.load("images/album.jpg"),(scr_x,scr_y))

music=["music/Die For You - The Weeknd.mp3","music/mirrorball - Taylor Swift.mp3","music/R U Mine  - Arctic Monkeys.mp3"]
pygame.mixer.music.load(music[0])
current_music=0
pygame.mixer.music.play()

while window:
    scr.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key==pygame.K_RIGHT:
                current_music=(current_music+1)%len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
            elif event.key==pygame.K_LEFT:
                current_music=(current_music-1)%len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
    pygame.display.update()