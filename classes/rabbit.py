__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

import time
import math
import copy
from terrain import Terrain
from bullet import Bullet

RABBIT_IMG_DIR = 'resources/images/dude.png'
SHOT_INTERVAL = 1
class Rabbit(object):
	img = RABBIT_IMG_DIR
	member = None
	bullets = []
	def __init__(self, id, position):
		self.id = id
		self.position = position
		self.hp = 100
		self.last_shot_time = 0
		# self.member = None

	def check_position(self, position):
		x, y = position.x, position.y
		if x<0 or x>Terrain.size[0] or y<0 or y>Terrain.size[1]:
			# raise self.OutOfMap()
			return False
		return True

	def move(self, position):
		if self.check_position(position):
			return True #move

	def got_damaged(self):
		self.hp -= 10

	def died(self):
		return self.hp <= 0

	def can_shot(self):
		if (int(time.time()) - self.last_shot_time) < SHOT_INTERVAL:
			return False
		return True

	def shot(self, g_position):
		'''
		Args:
			g_position: goal position
		'''
		if self.can_shot():
			angle = math.atan2(g_position[1] - (self.position[1] + 32), g_position[0] - (self.position[0] + 26))
			bullet = Bullet(angle, copy.deepcopy(self.position))
			Rabbit.bullets.append(bullet)
			self.last_shot_time = time.time()
