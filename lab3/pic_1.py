import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))

back_color = (255, 255, 0)
screen.fill(back_color)

def multicloud (main_cloud_x, main_cloud_y, cloud_radius, ro_cloud):
	circle(screen, (0, 0, 0), (main_cloud_x, main_cloud_y), cloud_radius + 1) #Cloud0
	circle(screen, (255, 255, 255), (main_cloud_x, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud1
	circle(screen, (255, 255, 255), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius + 1) #Cloud2
	circle(screen, (255, 255, 255), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud3
	circle(screen, (255, 255, 255), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud4
	circle(screen, (255, 255, 255), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius + 1) #Cloud5
	circle(screen, (255, 255, 255), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud6
	circle(screen, (255, 255, 255), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius)

def umbrella(left_upper_x, left_upper_y, dx_umb, h_umb, umb_radius, umb_start, deltha):
	rect(screen, (210, 110, 34), (left_upper_x, left_upper_y, dx_umb, h_umb))
	polygon(screen, (249, 96, 75), [(left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start), (left_upper_x + dx_umb + umb_radius, left_upper_y + umb_start)])
	polygon(screen, (249, 96, 75), [(left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start), (left_upper_x - umb_radius, left_upper_y + umb_start)])
	rect(screen, (249, 96, 75), (left_upper_x, left_upper_y, dx_umb, umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start))
	
def draw_paluba(boat_0_x, boat_0_y, proportion):
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
	rect(screen, (0, 0, 0), (parus_x, parus_y, proportion * 2 - 2,  2 * 10 * proportion))
	polygon(screen, (218, 173, 128), [(parus_x + proportion * 2 - 2, parus_y), (parus_x + proportion * 6, parus_y + proportion * 10), (parus_x + proportion * 14, parus_y + proportion * 10)])
	polygon(screen, (218, 173, 128), [(parus_x + proportion * 2 - 2,parus_y + proportion * 10 * 2), (parus_x + proportion * 6, parus_y + proportion * 10), (parus_x + proportion * 14, parus_y + proportion * 10)])
	aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 14, parus_y + proportion * 10))
	aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y))
	aaline(screen, (0, 0, 0), (parus_x + proportion * 14, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y))
	aaline(screen, (0, 0, 0), (parus_x + proportion * 6, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y + 2 * 10 * proportion))
	aaline(screen, (0, 0, 0), (parus_x + proportion * 14, parus_y + proportion *10), (parus_x + proportion * 2 - 2, parus_y + 2 * 10 * proportion))

def draw_sin (w_start, w_stop, w_color, y_wave, h_wave):
	d_wave = (w_stop - w_start)/90
	for i in range(89):
		polygon(screen, w_color, [(w_start + d_wave * i, y_wave), (w_start + d_wave * (i + 1), y_wave), (w_start + d_wave * i, y_wave - np.sin(np.pi * i / 90) * h_wave), (w_start + d_wave * (i + 1), y_wave - np.sin(np.pi * (i + 1) / 90) * h_wave)])

def anti_sin (w_start, w_stop, w_color, y_wave, h_wave):
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


