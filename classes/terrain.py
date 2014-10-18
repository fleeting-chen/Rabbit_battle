__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

MAP_WIDTH = 640
MAP_HEIGHT = 480
BG_DIR = "resources/images/grass.png"

class Terrain(object):
	size = [MAP_WIDTH, MAP_HEIGHT]
	background = BG_DIR
	member = None
