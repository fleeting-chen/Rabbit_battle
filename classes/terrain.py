__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

import pygame

MAP_WIDTH = 640
MAP_HEIGHT = 480

class Terrain(object):
	width = MAP_WIDTH
	height = MAP_HEIGHT
	background = "resources/images/grass.png"
	def __init__(self):
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.bg = pygame.image.load(self.background)
		self.screen.fill(0)

	def draw(self):
		for x in range(self.width / self.bg.get_width() + 1):
			for y in range(self.height / self.bg.get_height() + 1):
				self.screen.blit(self.bg, (x * 100, y * 100))