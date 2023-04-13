import pygame, sys
from pygame.locals import *
import random, time
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("images/racer/Roboto-Medium.ttf", 60)
font_small = pygame.font.SysFont("images/racer/Roboto-Medium.ttf", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("images/racer/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/racer/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        if pygame.sprite.collide_rect(self, P1):
            global SCORE
            SCORE += 10
            self.kill()
            coins.remove(self)
            all_sprites.remove(self)


P1 = Player()
E1 = Enemy()
C1=Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group() # Create a new sprite group for the coins
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 5000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.1)
        DISPLAYSURF.fill("RED")
        DISPLAYSURF.blit(font.render("Game Over", True, "Black"), (200, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()

    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 1
        # Speed += 0.5
        coins.update()

    # pygame.sprite.groupcollide(coins, enemies, True, False)  # Remove coins that collide with enemies
    # pygame.sprite.groupcollide(coins, all_sprites, True, False)
    pygame.display.update()
    FramePerSec.tick(FPS)
