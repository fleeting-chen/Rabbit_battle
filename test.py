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

	# rabbit.img = pygame.image.load(rabbit.img)
	# terrain.background = pygame.image.load(terrain.background)

	# screen = pygame.display.set_mode((terrain.width, terrain.height))
	# screen.fill(0)

	while True:
		terrain.draw()
		playerpos = (rabbit.position[0] - rabbit.member.get_rect().width / 2, rabbit.position[1] - rabbit.member.get_rect().height / 2)
		terrain.screen.blit(rabbit.member, playerpos)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)

if __name__ == "__main__":
	main()
