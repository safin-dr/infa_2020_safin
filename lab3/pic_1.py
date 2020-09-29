import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))

back_color = (255, 255, 0)
screen.fill(back_color)

def multicloud (main_cloud_x, main_cloud_y, cloud_radius, ro_cloud):
    
    '''
    Функция рисует облако из шести кругов
    main_cloud_x - икс-координата первого круга
    main_cloud_y - игрик-координата первого круга
    cloud_radius - радиус круга
    ro_cloud - сдвиг между соседними кругами
    '''
    
    for i in range(4):
        circle(screen, (0, 0, 0), (main_cloud_x + 4*i * ro_cloud, main_cloud_y), cloud_radius + 1)
        circle(screen, (255, 255, 255), (main_cloud_x + 4*i * ro_cloud, main_cloud_y), cloud_radius)
    for i in range(3):
        circle(screen, (0, 0, 0), (main_cloud_x + 4*i * ro_cloud + ro_cloud, main_cloud_y + 2*ro_cloud), cloud_radius + 1)
        circle(screen, (255, 255, 255), (main_cloud_x + 4*i * ro_cloud + ro_cloud, main_cloud_y + 2*ro_cloud), cloud_radius)
 
def umbrella(left_upper_x, left_upper_y, dx_umb, h_umb, umb_radius, umb_start, deltha):
    
    '''
    Функция рисует пляжный зонт
    left_upper_x - икс-координата левого верхнего конца ноги зонта
    left_upper_y - игрик-координата правого верхнего конца ноги зонта
    dx_umb - ширина ноги зонта
    h_umb - высота ноги зонта
    umb_radius - радиус основания конуса, образованного зонтом
    deltha - расстояние между полосками на зонте понизу
    umb_start - высота самого зонта 
    '''
    
    rect(screen, (210, 110, 34), (left_upper_x, left_upper_y, dx_umb, h_umb))
    polygon(screen, (249, 96, 75), [(left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start), (left_upper_x + dx_umb + umb_radius, left_upper_y + umb_start)])
    polygon(screen, (249, 96, 75), [(left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start), (left_upper_x - umb_radius, left_upper_y + umb_start)])
    rect(screen, (249, 96, 75), (left_upper_x, left_upper_y, dx_umb, umb_start))
    for i in range(4):
        aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + i * deltha, left_upper_y + umb_start))
    for i in range(4):
        aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - i * deltha, left_upper_y + umb_start))
    aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start))
    aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start))
    
def draw_paluba(boat_0_x, boat_0_y, proportion):
    '''
    Функция рисует корабль без паруса 
    boat_0_x - икс-координата кормы
    boat_0_y - игрик-координата кормы
    proportion - характеристический линейный размер корабля
    '''
    circle(screen, (139, 80, 20), (boat_0_x, boat_0_y), proportion * 7)
    rect(screen, (0, 0, 255), (boat_0_x - proportion * 7, boat_0_y - proportion * 7, proportion * 7 * 2, proportion * 7))
    rect(screen, (0, 0, 255), (boat_0_x, boat_0_y, proportion * 7, proportion * 7))
    rect(screen, (0, 0, 0), (boat_0_x, boat_0_y, proportion * 28 + 2, proportion * 7))
    rect(screen, (139, 80, 20), (boat_0_x + 1, boat_0_y, proportion * 28, proportion * 7))
    polygon(screen, (0, 0, 0), [(boat_0_x + proportion * 28 + 2, boat_0_y), (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
    polygon(screen, (139, 80, 20), [(boat_0_x + proportion * 28 + 2, boat_0_y), (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
    circle(screen, (0, 0, 0), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2)
    circle(screen, (255, 255, 255), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2 - 3)
    
def draw_parus(parus_x, parus_y, proportion):
    '''
    Функция рисует парус и мачту кораблю
    parus_x - икс-координата верхнего левого конца мачты
    parus_y - игрик-координата верхнего правого конца мачты
    proportion - характеристический линейный размер корабля
    '''
    rect(screen, (0, 0, 0), (parus_x, parus_y, proportion * 2 - 2,  2 * 10 * proportion))
    polygon(screen, (218, 173, 128), [(parus_x + proportion * 2 - 2, parus_y), (parus_x + proportion * 6, parus_y + proportion * 10), (parus_x + proportion * 14, parus_y + proportion * 10)])
    polygon(screen, (218, 173, 128), [(parus_x + proportion * 2 - 2,parus_y + proportion * 10 * 2), (parus_x + proportion * 6, parus_y + proportion * 10), (parus_x + proportion * 14, parus_y + proportion * 10)])
    aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 14, parus_y + proportion * 10))
    aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y))
    aaline(screen, (0, 0, 0), (parus_x + proportion * 14, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y))
    aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y + 2 * 10 * proportion))
    aaline(screen, (0, 0, 0), (parus_x + proportion * 14, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y + 2 * 10 * proportion))

def draw_sin (w_start, w_stop, w_color, y_wave, h_wave):
    '''
    Функция рисует округлую выпуклость берега
    w_start - икс-координата начала первой волна
    w_stop - икс-координата конца первой волны
    w_color - цвет берега
    y_wave - игрик-координата волны, совпадает с линией раздела суши и моря
    h_wave - высота верхушки
    '''
    d_wave = (w_stop - w_start)/90
    for i in range(89):
        polygon(screen, w_color, [(w_start + d_wave * i, y_wave), (w_start + d_wave * (i + 1), y_wave), (w_start + d_wave * i, y_wave - np.sin(np.pi * i / 90) * h_wave), (w_start + d_wave * (i + 1), y_wave - np.sin(np.pi * (i + 1) / 90) * h_wave)])

def anti_sin (w_start, w_stop, w_color, y_wave, h_wave):
    '''
    Функция рисует округлую вогнутость берега
    w_start - икс-координата начала первой волна
    w_stop - икс-координата конца первой волны
    w_color - цвет моря
    y_wave - игрик-координата волны, совпадает с линией раздела суши и моря
    h_wave - высота низушки
    '''
    d_wave = (w_stop - w_start)/90
    for i in range(89):
        polygon(screen, w_color, [(w_start + d_wave * i, y_wave), (w_start + d_wave * (i + 1), y_wave), (w_start + d_wave * i, y_wave + np.sin(np.pi * i / 90) * h_wave), (w_start + d_wave * (i + 1), y_wave + np.sin(np.pi * (i + 1) / 90) * h_wave)])

R = 40
r = 8
Sunlights = 60

rect(screen, (0, 0, 255), (0, 0, 600, 260))	

for i in range (7):
	draw_sin (43 * i * 2, 43 * (i * 2 + 1), (255, 255, 0), 260, 10)
	anti_sin (43 * (i * 2 + 1), 43 * (i * 2 + 2), (0, 0, 255), 260, 10)
	
aaline(screen, (0, 0, 0), (0, 260), (600, 260))

draw_paluba(360, 190, 5)
draw_paluba(185, 170, 3)
rect(screen, (0, 0, 255), (0, 0, 600, 170))
rect(screen, (129, 218, 247), (0, 0, 600, 160))
draw_parus(415, 90, 5)
draw_parus(225, 110, 3)
circle(screen, (255, 255, 0), (540, 60), R) #Sun
multicloud(170, 40, 15, 5)
multicloud(306, 30, 25, 8)
multicloud(116, 98, 19, 7)

for i in range(60):
	polygon(screen, (255, 255, 0), [(540 + R * np.sin ( 2 * i * np.pi / Sunlights), 60 - R * np.cos (2 * i * np.pi / Sunlights)), (540 + R * np.sin ( (2 * i + 1) * np.pi / Sunlights), 60 - R * np.cos ((2 * i + 1) * np.pi / Sunlights)), ((540 + (R + r) * np.sin ((2 * i + 0.5) * np.pi / Sunlights), 60 - (R + r) * np.cos ((2 * i + 0.5) * np.pi / Sunlights)))])


umbrella(110, 220, 8, 140, 54, 25, 15)
umbrella(240, 245, 4, 96, 28, 28, 7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()


