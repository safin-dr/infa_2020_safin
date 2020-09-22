import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

back_color = (191, 191, 191)
screen.fill(back_color)

circle(screen, (0, 0, 0), (300, 300), 200, 1)
circle(screen, (255, 255, 0), (300, 300), 199, 0) #yellow
polygon(screen, (0, 0, 0), [(220, 400), (220, 435), (380, 435), (380, 400)])
polygon(screen, (0, 0, 0), [(135, 130), (250, 190), (245, 200), (130, 140)])
polygon(screen, (0, 0, 0), [(380, 190), (385, 200), (505, 165), (500, 155)])
circle(screen, (0, 0, 0), (220, 220), 30, 2)
circle(screen, (255, 0, 0), (220, 220), 29, 0) #red
circle(screen, (0, 0, 0), (405, 220), 25, 2)
circle(screen, (255, 0, 0), (405, 220), 24, 0)
circle(screen, (0, 0, 0), (220, 220), 15)
circle(screen, (0, 0, 0), (405, 220), 14)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
