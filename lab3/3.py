import pygame
import numpy as np

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (64, 128, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
SKY = (170, 238, 255)
SKIN = (244, 227, 215)

FPS = 30
screen = pygame.display.set_mode((1000, 750))

# outside
pygame.draw.rect(screen, SKY, (0, 0, 1000, 375))
pygame.draw.rect(screen, GREEN, (0, 375, 1000, 750))


def women(x, y, size, i):
    # hands
    pygame.draw.line(screen, BLACK, (x, y), (x + 110 * size * i, y - 80 * size))
    pygame.draw.line(screen, BLACK, (x + 130 * size * i, y - 90 * size), (x + 170 * size * i, y - 50 * size))
    pygame.draw.line(screen, BLACK, (x + 170 * size * i, y - 50 * size), (x + 220 * size * i, y - 80 * size))
    # feet
    pygame.draw.line(screen, BLACK, (x + 140 * size * i, y + 80 * size), (x + 140 * size * i, y + 170 * size))
    pygame.draw.line(screen, BLACK, (x + 140 * size * i, y + 170 * size), (x + 160 * size * i, y + 175 * size))
    pygame.draw.line(screen, BLACK, (x + 100 * size * i, y + 80 * size), (x + 100 * size * i, y + 170 * size))
    pygame.draw.line(screen, BLACK, (x + 100 * size * i, y + 170 * size), (x + 70 * size * i, y + 170 * size))
    # body head
    pygame.draw.polygon(screen, BLUE, [[x + 120 * size * i, y - 130 * size], [x + 60 * size * i, y + 80 * size],
                                       [x + 190 * size * i, y + 80 * size]])
    pygame.draw.circle(screen, SKIN, (x + 120 * size * i, y - 130 * size), 30)


'''
Функция рисует женщин
x, y - координаты кисти несогнутой руки
size - отношение размера человечка к дефолтному, соответствующему 1
i -  ориентация относительно оси Oy
'''


def man(x, y, size, i):
    # hands
    pygame.draw.line(screen, BLACK, (x, y), (x - 50 * size * i, y + 85 * size))
    pygame.draw.line(screen, BLACK, (x + 55 * size * i, y - 5 * size), (x + 125 * size * i, y + 85 * size))
    # feet
    pygame.draw.line(screen, BLACK, (x + 10 * size * i, y + 145 * size), (x - 30 * size * i, y + 255 * size))
    pygame.draw.line(screen, BLACK, (x - 30 * size * i, y + 255 * size), (x - 25 * size * i, y + 256 * size))
    pygame.draw.line(screen, BLACK, (x + 50 * size * i, y + 145 * size), (x + 65 * size * i, y + 250 * size))
    pygame.draw.line(screen, BLACK, (x + 65 * size * i, y + 250 * size), (x + 105 * size * i, y + 254 * size))
    # body head
    if i == 1:
        pygame.draw.ellipse(screen, PINK, (x - 20 * size * i, y - 25 * size, 100 * size, 200 * size))
    else:
        pygame.draw.ellipse(screen, PINK, (x - 20 * size * i - 100 * size, y - 25 * size, 100 * size, 200 * size))
    pygame.draw.circle(screen, SKIN, (x + 30 * size * i, y - 45 * size), 30 * size)


'''
Функция рисует мужчин
x, y - координаты кисти одной из рук
size - отношение размера человечка к дефолтному, соответствующему 1
i -  ориентация относительно оси Oy
'''


def sun(x_cord, y_cord, radius, resolution, len_shines):
    pygame.draw.circle(screen, YELLOW, (x_cord, y_cord), radius)
    t: int = 0
    for i in range(resolution):
        t += 2 * np.pi / resolution
        pygame.draw.line(screen, YELLOW, (x_cord, y_cord), (x_cord + np.cos(t) * radius * len_shines, y_cord + np.sin(t)
                                                            * radius * len_shines))


'''
Функция рисует солнце
x_cord, y_cord - координаты центра солнца (а именно его лучей)
radius - радиус солнца без лучей
resolution - кол-во лучей
len_shines - отношение длины луча к радиусу солнца
'''


def cloud(x_cord, y_cord, size, reverse):
    if reverse == 'normal':
        i_reverse = 1
    elif reverse == 'reverse':
        i_reverse = -1

    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * 30 * size), int(y_cord + 15 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * 30 * size), int(y_cord + 15 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * 0 * size), int(y_cord + 15 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * 0 * size), int(y_cord + 15 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * -30 * size), int(y_cord + 15 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * -30 * size),
                                       int(y_cord + 15 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * 50 * size), int(y_cord + 45 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * 50 * size), int(y_cord + 45 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * 20 * size), int(y_cord + 45 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * 20 * size), int(y_cord + 45 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * -10 * size), int(y_cord + 45 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * -10 * size),
                                       int(y_cord + 45 * size)), int(30 * size), 1)
    pygame.draw.circle(screen, WHITE, (int(x_cord + i_reverse * -40 * size), int(y_cord + 45 * size)), int(30 * size))
    pygame.draw.circle(screen, BLACK, (int(x_cord + i_reverse * -40 * size),
                                       int(y_cord + 45 * size)), int(30 * size), 1)


'''
Функция рисует облако
x_cord, y_cord - координаты крайнего кружка
size - отношение радиуса рисуемого облака к дефолтному радиусу, равному 50
reverse - ориентация облака относительно оси Oy
'''


def ice_cream1(x, y, size):
    pygame.draw.polygon(screen, YELLOW, [[x, y], [x + 12 * size, y - 90 * size], [x + 70 * size, y - 50 * size]])
    pygame.draw.circle(screen, BLACK, (x + 30 * size, y - 85 * size), 20 * size)
    pygame.draw.circle(screen, RED, (x + 60 * size, y - 60 * size), 20 * size)
    pygame.draw.circle(screen, WHITE, (x + 57 * size, y - 90 * size), 20 * size)


'''
Функция рисует разноцветное мороженое
x, y - координаты
size - отношение размера к дефолтному, соответствующему size = 1
'''


def balloons(x, y, size):
    pygame.draw.line(screen, BLACK, (x - 10, y), (x + 10 * size, y - 180 * size))
    pygame.draw.polygon(screen, YELLOW, [[x + 10 * size, y - 180 * size], [x + 70 * size, y - 290 * size],
                                         [x - 40 * size, y - 280 * size]])
    pygame.draw.circle(screen, BLACK, (x - 15 * size, y - 295 * size), 30 * size)
    pygame.draw.circle(screen, RED, (x + 43 * size, y - 300 * size), 30 * size)
    pygame.draw.circle(screen, WHITE, (x + 10 * size, y - 320 * size), 30 * size)


'''
Функция рисует шары
x, y - координаты начала верёвки
size - отношение размера к дефолтному, соответствующему size = 1
'''


def ice_creame2(x, y, size):
    pygame.draw.line(screen, BLACK, (x + 5, y - 8), (x - 39 * size, y - 135 * size))
    pygame.draw.polygon(screen, RED, [[x - 39 * size, y - 135 * size], [x - 82 * size, y - 215 * size],
                                      [x - 5 * size, y - 225 * size]])
    pygame.draw.circle(screen, RED, (x - 25 * size, y - 235 * size), 25 * size)
    pygame.draw.circle(screen, RED, (x - 65 * size, y - 231 * size), 25 * size)


'''
Функция рисует шары
x, y - координаты начала верёвки
size - отношение размера к дефолтному, соответствующему size = 1
'''

women(290, 460, 1, 1)
women(730, 460, 1, -1)
man(780, 375, 1, 1)
man(235, 370, 1, -1)
ice_cream1(900, 460, 1)
balloons(520, 380, 1)
ice_creame2(105, 465, 1)
sun(100, 100, 60, 40, 1.2)
cloud(800, 60, 1, 'normal')
cloud(300, 70, 1.3, 'reverse')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
