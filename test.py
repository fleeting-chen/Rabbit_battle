__author__ = 'chenhao'
__date__ = '14-7-9'
#encoding:utf-8

import pygame
from pygame.locals import *
import classes
from classes.rabbit import Rabbit
from classes.terrain import Terrain

# main()
def main():
	rabbit = Rabbit(1, [100,100])
	terrain = Terrain()
	pygame.init()

	# rabbit.img = pygame.image.load(rabbit.img)
	terrain.background = pygame.image.load(terrain.background)

	screen = pygame.display.set_mode((terrain.width, terrain.height))
	screen.fill(0)

	while True:
		for x in range(terrain.width / terrain.background.get_width() + 1):
			for y in range(terrain.height / terrain.background.get_height() + 1):
				screen.blit(terrain.background, (x * 100, y * 100))
		playerpos = (rabbit.position[0] - rabbit.member.get_rect().width / 2, rabbit.position[1] - rabbit.member.get_rect().height / 2)
		screen.blit(rabbit.member, playerpos)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)

if __name__ == "__main__":
	main()
