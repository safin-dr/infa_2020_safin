import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))

back_color = (255, 255, 0)
screen.fill(back_color)

rect(screen, (0, 0, 255), (0, 0, 600, 260))
circle(screen, (0, 0, 0), (360, 190), 35)
circle(screen, (139, 80, 20), (360, 190), 35) #Boat_start
rect(screen, (0, 0, 255), (0, 0, 600, 190))
rect(screen, (0, 0, 255), (360, 190, 35, 35))
rect(screen, (129, 218, 247), (0, 0, 600, 170))
rect(screen, (0, 0, 0), (360, 190, 143, 35))
rect(screen, (139, 80, 20), (361, 190, 141, 35))
polygon(screen, (0, 0, 0), [(503, 190), (503, 224),(560,190)])
polygon(screen, (139, 80, 20), [(503, 190), (503, 224),(580,190)])
circle(screen, (0, 0, 0), (525, 203), 10)
circle(screen, (255, 255, 255), (525, 203), 7)
rect(screen, (0, 0, 0), (420, 110, 6, 80))
polygon(screen, (0, 0, 0), [(426,110), (440, 150), (480, 150)])
polygon(screen, (218, 173, 128), [(427,111), (441, 149), (478, 149)])
polygon(screen, (0, 0, 0), [(426,190), (440, 150), (480, 150)])
polygon(screen, (218, 173, 128), [(427,189), (441, 151), (478, 151)]) #Boat_end
circle(screen, (255, 255, 0), (540, 60), 40) #Sun
circle(screen, (0, 0, 0), (170, 40), 16) #Cloud0
circle(screen, (255, 255, 255), (170, 40), 15)
circle(screen, (0, 0, 0), (160, 55), 16) #Cloud1
circle(screen, (255, 255, 255), (160, 55), 15)
circle(screen, (0, 0, 0), (190, 40), 16) #Cloud2
circle(screen, (255, 255, 255), (190, 40), 15)
circle(screen, (0, 0, 0), (180, 55), 16) #Cloud3
circle(screen, (255, 255, 255), (180, 55), 15)
circle(screen, (0, 0, 0), (200, 55), 16) #Cloud4
circle(screen, (255, 255, 255), (200, 55), 15)
circle(screen, (0, 0, 0), (210, 40), 16) #Cloud5
circle(screen, (255, 255, 255), (210, 40), 15)
circle(screen, (0, 0, 0), (220, 55), 16) #Cloud6
circle(screen, (255, 255, 255), (220, 55), 15)
rect(screen, (210, 110, 34), (110, 220, 8, 140)) #Umbrella
polygon(screen, (249, 96, 75), [(118, 220), (118, 245), (172, 245)])
polygon(screen, (249, 96, 75), [(110, 220), (110, 245), (56, 245)])
rect(screen, (249, 96, 75), (110, 220, 8, 25))
line(screen, (0, 0, 0), (110, 220), (71, 245), 1)
line(screen, (0, 0, 0), (110, 220), (86, 245), 1)
line(screen, (0, 0, 0), (110, 220), (101, 245), 1)
line(screen, (0, 0, 0), (118, 220), (127, 245), 1)
line(screen, (0, 0, 0), (118, 220), (142, 245), 1)
line(screen, (0, 0, 0), (118, 220), (157, 245), 1)
line(screen, (0, 0, 255), (118, 220), (118, 245), 1)
line(screen, (0, 0, 255), (110, 220), (110, 245), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
