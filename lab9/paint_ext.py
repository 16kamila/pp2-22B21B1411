import pygame
import math
import random

pygame.init()
# const vars
W, H = 1000, 600
eraser_size=40
SCREEN = pygame.display.set_mode((W, H), pygame.RESIZABLE)
FONT = pygame.font.SysFont("Arial", 20)
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30



class GameObject:
    def draw(self):
        return

    def update(self, end_pos):
        return


class Eraser(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                "BLACK",
                (self.points[idx][0], self.points[idx][1]),
                (self.points[idx + 1][0], self.points[idx + 1][1]),
                eraser_size
            )

    def update(self, end_pos):
        self.points.append(end_pos)



class Pen(GameObject):
    def __init__(self, color, *args, **kwargs):
        self.points = []
        self.color = color

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                self.color,
                (self.points[idx][0], self.points[idx][1]),
                (self.points[idx + 1][0], self.points[idx + 1][1]),
                5
            )

    def update(self, end_pos):
        self.points.append(end_pos)


class Rectangle(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x1 = min(self.start[0], self.end[0])
        y1 = min(self.start[1], self.end[1])
        x2 = max(self.start[0], self.end[0])
        y2 = max(self.start[1], self.end[1])

        pygame.draw.rect(
            SCREEN,
            self.color,
            (x1, y1, x2 - x1, y2 - y1),
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Square(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x = min(self.start[0], self.end[0])
        y = min(self.start[1], self.end[1])
        width = min(abs(self.start[0] - self.end[0]), abs(self.start[1] - self.end[1]))
        pygame.draw.rect(
            SCREEN,
            self.color,
            (x, y, width, width),
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Circle(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x1 = min(self.start[0], self.end[0])
        y1 = min(self.start[1], self.end[1])
        x2 = max(self.start[0], self.end[0])
        y2 = max(self.start[1], self.end[1])

        pygame.draw.circle(
            SCREEN,
            self.color,
            (self.start[0], self.start[1]),
            math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)),
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Equilateral_Triangle(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x1 = self.start[0]
        y1 = self.start[1]
        x2 = self.end[0]
        y2 = self.end[1]
        pygame.draw.polygon(
            SCREEN,
            self.color,
            [(x1, y1), (x1, y2), (x2, y2)],
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Right_Triangle(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x1 = self.start[0]
        y1 = self.start[1]
        x2 = self.end[0]
        y2 = self.end[1]
        pygame.draw.polygon(
            SCREEN,
            self.color,
            [(x1, y1), (x1 - (x2 - x1), y2), (x2, y2)],
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Rhombus(GameObject):
    def __init__(self, start_pos, color, *args, **kwargs):
        self.start = start_pos
        self.end = start_pos
        self.color = color

    def draw(self):
        x1 = self.start[0]
        y1 = self.start[1]
        x2 = self.end[0]
        y2 = self.end[1]
        pygame.draw.polygon(
            SCREEN,
            self.color,
            [(x1, y1), (x1 - (x2 - x1), y2), (x2, y2), (x2 + (x2 - x1), y1)],
            5
        )

    def update(self, end_pos):
        self.end = end_pos


class Button:
    def __init__(self, x, y, width, height, name, func=None, *args, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.func = func
        self.surf = pygame.Surface((width, height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = FONT.render(name, True, ("White"))
        self.font_rect = self.font.get_rect(center=(self.width / 2, self.height / 2))

    def draw(self):
        pos = pygame.mouse.get_pos()
        self.surf.fill((120, 20, 44))
        if self.rect.collidepoint(pos):
            self.surf.fill((99, 17, 37))
            if pygame.mouse.get_pressed()[0]:
                self.surf.fill((71, 12, 27))
                self.func()

        border_color = (64, 3, 18)
        border_width = 3
        pygame.draw.rect(self.surf, border_color, pygame.Rect(0, 0, self.width, self.height), border_width)

        self.surf.blit(self.font, self.font_rect)
        SCREEN.blit(self.surf, self.rect)




objects = [
]

buttons = [
    ["eraser", lambda: changeshape(Eraser)],
    ["erasersize", lambda: changeshape(EraserSizeButton)],
    ["default", lambda: changeshape(Pen)],
    ["▬", lambda: changeshape(Rectangle)],
    ["■", lambda: changeshape(Square)],
    ["●", lambda: changeshape(Circle)],
    ["▲", lambda: changeshape(Right_Triangle)],
    ["▶", lambda: changeshape(Equilateral_Triangle)],
    ["red", lambda: changecolor("RED")],
    ["green", lambda: changecolor("GREEN")],
    ["random color", lambda: changecolor((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))]
]
# buttons create
for idx, button in enumerate(buttons):
    if idx < 8:
        objects.append(Button(idx * 101, 0, BUTTON_WIDTH, BUTTON_HEIGHT, button[0], button[1]))
    else:
        objects.append(Button((idx - 8) * 101, 31, BUTTON_WIDTH, BUTTON_HEIGHT, button[0], button[1]))
# vars
curr_color = "RED"
game_object = GameObject()
curr_object = game_object
curr_shape = Pen


def changecolor(color):
    global curr_color
    curr_color = color


def changeshape(shape):
    global curr_shape
    curr_shape = shape


clock = pygame.time.Clock()
running = True
while running:
    SCREEN.fill("BLACK")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            curr_object = curr_shape(start_pos=pygame.mouse.get_pos(), color=curr_color)
            objects.append(curr_object)

        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            curr_object.update(end_pos=pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            curr_object = game_object

    for obj in objects:
        obj.draw()

    clock.tick(30)
    pygame.display.flip()