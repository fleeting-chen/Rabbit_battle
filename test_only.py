__author__ = 'chenhao'
__date__ = '14-7-9'
#encoding:utf-8

import math
import pygame
from classes.rabbit import Rabbit
from classes.terrain import Terrain
from classes.bullet import Bullet

rabbits = []
# main()
def main():
	pygame.init()

	Terrain.member = pygame.image.load(Terrain.background)
	Rabbit.member = pygame.image.load(Rabbit.img)
	Bullet.member = pygame.image.load(Bullet.img)

	rabbit = Rabbit(1, [0,0])
	rabbits.append(rabbit)
	rabbit1 = Rabbit(1, [50,60])
	rabbit1.shot([300,160])
	rabbits.append(rabbit1)

	screen = pygame.display.set_mode((Terrain.size[0], Terrain.size[1]))
	screen.fill(0)

	while True:
		for x in range(Terrain.size[0] / Terrain.member.get_width() + 1):
			for y in range(Terrain.size[1] / Terrain.member.get_height() + 1):
				screen.blit(Terrain.member, (x * 100, y * 100))

		for rbt in rabbits:
			rbtpos = (rbt.position[0] - Rabbit.member.get_rect().width / 2, rbt.position[1] - Rabbit.member.get_rect().height / 2)
			screen.blit(Rabbit.member, rbtpos)

		for blt in Rabbit.bullets:
			index = 0
			velx = math.cos(blt.angle) * Bullet.velocity
			vely = math.sin(blt.angle) * Bullet.velocity
			blt.move(velx, vely)
			if blt.position[0] < -Bullet.member.get_rect().width or blt.position[0] > Terrain.size[0] + Bullet.member.get_rect().width or blt.position[1] < -Bullet.member.get_rect().height or blt.position[1] > Terrain.size[1] + Bullet.member.get_rect().height:
				Rabbit.bullets.pop(index)
			index += 1
			for projectile in Rabbit.bullets:
				arrow1 = pygame.transform.rotate(Bullet.member, 360 - projectile.angle * 57.29)
				screen.blit(arrow1, (projectile.position[0], projectile.position[1]))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)

if __name__ == "__main__":
	main()
