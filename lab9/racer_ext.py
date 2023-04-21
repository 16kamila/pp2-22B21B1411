import pygame
import random
import time
pygame.init()

scrw, scrh=800, 670
Speed=5
SCORE=0

#Display, font
screen = pygame.display.set_mode((scrw,scrh))
background = pygame.Surface((scrw,scrh))
big_font = pygame.font.SysFont("images/races/Roboto-Medium.ttf", 70)
small_font = pygame.font.SysFont("images/races/Roboto-Medium.ttf", 30)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/racer/car1.png"), (50, 100))
        self.rect = self.image.get_rect(center = (400, scrh-100))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 150:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_d] and self.rect.right <scrw- 150:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/racer/car2.png"), (50,100))
        self.rect = self.image.get_rect(center=(random.randint(200,scrw- 200), 75))

    def update(self):
        if self.rect.y <scrh- 20:
            self.rect.y += Speed
        else:
            self.rect.center = (random.randint(200,scrw-200), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/racer/coin.png"), (40, 40))
        self.rect = self.image.get_rect(center=(random.randint(200,scrw- 200), -50))

    def update(self):
        # self.rect.move_ip(0, Speed)
        if self.rect.y <scrh- 20:
            self.rect.y += Speed
        else:
            self.rect.center = (random.randint(200,scrw-200), 0)
        if self.rect.top >scrh:
            self.kill()

    def collect(self):
        self.kill()
        return 1


#setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

weight = random.choice([1, 2, 3])
w = small_font.render(str(weight), True, "Black")
w_rect = w.get_rect(center = (15, 15))
C1.image.blit(w, w_rect)

#game Loop
running = True
while running:
    #Screen
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, "white", (150, 0), (150,scrh), 10)
    pygame.draw.line(screen, "white", (scrw-150, 0), (scrw-150,scrh), 10)
    Score = small_font.render(f"Score:{SCORE}", True, "Red")
    screen.blit(Score, (670, 0))

    #moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.update()

    # Update the coins and remove any that have gone off the screen
    for coin in coins:
        # coin.move()
        if coin.rect.top>scrh:
            coin.kill()
    max=2
    earned=SCORE
    # if earned>0 and earned%2==0:
    #     Speed += 1
    #     if earned>3:
    #         earned=0

    #add new coins randomly
    if len(coins)<2:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    #to be run if collision occurs between p1 and e1 and p1 and c1
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.2)
        screen.fill("RED")
        screen.blit(big_font.render("Game Over", True, "Black"), (200, 350))
        pygame.display.update()
        pygame.display.update()

    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += weight
        coins.update()
        weight = random.choice([1, 3, 5])
        w = small_font.render(str(weight), True, "Black")
        w_rect = w.get_rect(center=(15, 15))
        C1.image.blit(w, w_rect)
        Speed += 2

    for coin in pygame.sprite.spritecollide(P1, coins, True):
        SCORE += C1.collect()
        C1 = Coin()
        coins.add(C1)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()