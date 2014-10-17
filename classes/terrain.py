__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

MAP_WIDTH = 640
MAP_HEIGHT = 480
BG_DIR = "resources/images/grass.png"

class Terrain(object):
	size = [MAP_WIDTH, MAP_HEIGHT]
	# width = MAP_WIDTH
	# height = MAP_HEIGHT
	background = BG_DIR
	member = None
	# def __init__(self):
		# self.member = None
		# self.screen = pygame.display.set_mode((self.width, self.height))
		# self.bg = pygame.image.load(self.background)
		# self.screen.fill(0)

	# def draw(self):
	# 	for x in range(self.width / self.bg.get_width() + 1):
	# 		for y in range(self.height / self.bg.get_height() + 1):
	# 			self.screen.blit(self.bg, (x * 100, y * 100))