__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

import time
from arrow import Arrow
from terrain import Terrain
import pygame
from pygame.locals import *


class Rabbit(object):
	def __init__(self, id, position):
		self.id = id
		self.position = position
		self.hp = 100
		self.img = "resources/images/dude.png"
		self.arrow = Arrow()

	def check_position(self, position):
		x, y = position.x, position.y
		if x<0 or x>Terrain.width or y<0 or y>Terrain.height:
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

	def shot(self):
		if self.can_shot():
			return True #shot

	def can_shot(self):
		if (int(time.time()) - self.arrow.last_shot_time) < self.arrow.interval:
			return False
		return True
