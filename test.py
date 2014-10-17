__author__ = 'chenhao'
__date__ = '14-7-9'
#encoding:utf-8

import pygame
from classes.rabbit import Rabbit
from classes.terrain import Terrain

# main()
def main():
	pygame.init()
	rabbit = Rabbit(1, [0,0])
	terrain = Terrain()

	terrain.member = pygame.image.load(terrain.background)
	rabbit.member = pygame.image.load(rabbit.img)

	screen = pygame.display.set_mode((terrain.width, terrain.height))
	screen.fill(0)

	while True:
		for x in range(terrain.width / terrain.member.get_width() + 1):
			for y in range(terrain.height / terrain.member.get_height() + 1):
				screen.blit(terrain.member, (x * 100, y * 100))
		playerpos = (rabbit.position[0] - rabbit.member.get_rect().width / 2, rabbit.position[1] - rabbit.member.get_rect().height / 2)
		screen.blit(rabbit.member, playerpos)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)

if __name__ == "__main__":
	main()
