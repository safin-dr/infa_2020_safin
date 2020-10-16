
import os
import pygame as pg
import random as rnd
from random import randint
import sys


class Ball:
    '''
    Задаём класс шариков, обладающий определенными свойствами
    '''
    def __init__(self, x, y, dx, dy, image):
        '''
        Инициализация шарика - необходима для его создания
        x, y - произвольные координаты старта шарика
        dx, dy - смещение шарика за одну итерацию
        image - внешний вид шарика
        '''
        #print(x, y, dx, dy)
        self.img = pg.transform.scale(image, (150, 150))
        self.dx = dx
        self.dy = dy
        self.rect = screen.blit(self.img, (x, y))
        return

    def show(self):
        '''
        Функция, показывающая шарик
        '''
        screen.blit(self.img, self.rect)

    def move(self):
        '''
        Отвечает за перемещение шарика в каждой итерации
        '''  
        self.rect = self.rect.move([self.dx, self.dy])
        self.show()
        return

    def check_collide_with_walls(self, left_x, right_x, top_y, bottom_y):
        '''
        Функция отвечает за отражение шарика от стены
        left_x, right_x, top_y, bottom_y - границы картинки
        '''
        if self.rect.left < left_x or self.rect.right > right_x:
            self.dx *= -1

        if self.rect.top < top_y or self.rect.bottom > bottom_y:
            self.dy *= -1
        return
    
    def check_click(self, coords):
        '''
        Выдаёт очки в зависимости от попадания
        '''
        if self.rect.left < coords[0] and self.rect.right > coords[0] and self.rect.top < coords[1] and self.rect.bottom > coords[1]:
            return True

        return False   


class Target:
    '''
    Задаём класс мишеней, обладающий определенными свойствами
    '''
    def __init__(self, x, y, dx, dy, image):
        '''
        Инициализация мишени необходима для её создания
        x, y - произвольные координаты старта мишени
        dx, dy - смещение мишени за одну итерацию
        image - внешний вид мишени
        '''
        #print(x, y, dx, dy)
        self.img = pg.transform.scale(image, (150, 150))
        self.dx = dx
        self.dy = dy
        self.rect = screen.blit(self.img, (x, y))
        return

    def show(self):
        '''
        Функция, показывающая мишень
        '''
        screen.blit(self.img, self.rect)

    def move(self):
        '''
        Отвечает за перемещение мишени в каждой итерации
        '''  
        self.rect = self.rect.move([self.dx, self.dy])
        self.show()
        return

    def check_collide_with_walls(self, left_x, right_x, top_y, bottom_y):
        '''
        Функция отвечает за отражение мишени от стены
        left_x, right_x, top_y, bottom_y - границы картинки
        '''
        if self.rect.left < left_x or self.rect.right > right_x:
            self.dx *= -1

        if self.rect.top < top_y or self.rect.bottom > bottom_y:
            self.dy *= -1
        return
    
    def check_click(self, coords):
        '''
        Выдаёт очки в зависимости от попадания
        '''
        if self.rect.left < coords[0] and self.rect.right > coords[0] and self.rect.top < coords[1] and self.rect.bottom > coords[1]:
            return True

        return False   

        
''' Задаём исходные данные'''

size = width, height = 1000, 600
white = 255, 255, 255

screen = pg.display.set_mode(size)

balls_array = []
balls_n = 4
targets_array = []
targets_n = 1

##########!!!!!!!!!!!!!
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
##########!!!!!!!!!!!!!

'''Цикл, задающий необходимое количество шариков и мишеней'''
for i in range(balls_n):
    balls_array.append(Ball(randint(100, width - 100),
                            randint(100, height - 100),
                            randint(1, 6),
                            randint(1, 6),
                            pg.image.load(os.path.join(img_folder, 'rat.jpg'))))

for i in range(targets_n):
    targets_array.append(Target(randint(100, width - 100),
                            randint(100, height - 100),
                            randint(6, 10),
                            randint(6, 10),
                            pg.image.load(os.path.join(img_folder, 'dgap.jpg'))))

clock = pg.time.Clock()

score = 0
change = 1

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for ball in balls_array:
                if ball.check_click(event.pos):
                    score += 1
                    break
            for Target in targets_array:
                if target.check_click(event.pos):
                    score += 2
                    break
                
            print(score)
            
    if change % 10 == 1 :
        color = randint(0, 255), randint(0, 255), randint(0, 255)
    change += 1
    screen.fill(color)

    for ball in balls_array:
        ball.move()
        ball.check_collide_with_walls(0, width, 0, height)
        
    for target in targets_array:
        target.move()
        target.check_collide_with_walls(0, width, 0, height)

    pg.display.flip()
    clock.tick(30)    
