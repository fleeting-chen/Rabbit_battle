__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

MAP_WIDTH = 640
MAP_HEIGHT = 480

class Terrain(object):
	def __init__(self):
		self.width = MAP_WIDTH
		self.height = MAP_HEIGHT
		self.background = "../resources/images/grass.png"
