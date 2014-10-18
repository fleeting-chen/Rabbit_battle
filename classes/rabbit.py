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
RABBIT_VELOCITY = 5

class Rabbit(object):
	img = RABBIT_IMG_DIR
	member = None
	bullets = []

	def __init__(self, id, position):
		self.id = id
		self.position = position
		self.hp = 100
		self.last_shot_time = 0
		self.angle = 0

	def check_position(self, position):
		x, y = position.x, position.y
		if x < 0 or x > Terrain.size[0] or y < 0 or y > Terrain.size[1]:
			return False
		return True

	def move(self, target_position):
		if self.check_position(target_position):
			angle = math.atan2(target_position[1] - self.position[1], target_position[0] - self.position[0])
			self.angle = angle
			velx = math.cos(angle) * Bullet.velocity
			vely = math.sin(angle) * Bullet.velocity
			self.position[0] += velx
			self.position[1] += vely


	def got_damaged(self):
		self.hp -= 10

	def died(self):
		return self.hp <= 0

	def can_shot(self):
		if (int(time.time()) - self.last_shot_time) < SHOT_INTERVAL:
			return False
		return True

	def shot(self, t_position):
		'''
		Args:
			t_position: target position
		'''
		if self.can_shot():
			angle = math.atan2(t_position[1] - self.position[1], t_position[0] - self.position[0])
			self.angle = angle
			bullet = Bullet(copy.deepcopy(self.id), angle, copy.deepcopy(self.position))
			Rabbit.bullets.append(bullet)
			self.last_shot_time = time.time()