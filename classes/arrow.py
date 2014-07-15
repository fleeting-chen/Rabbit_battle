__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

from bullet import Bullet
import time
import math
SHOT_INTERVAL = 1

class Arrow(object):
	interval = SHOT_INTERVAL
	def __init__(self):
		self.last_shot_time = 0
		self.bullets = []

	def can_shot(self):
		if (int(time.time()) - self.last_shot_time) < self.interval:
			return False
		return True

	def shot(self,s_position, g_position):
		angle = math.atan2(g_position[1] - (s_position[1] + 32), g_position[0] - (s_position[0] + 26))
		bullet = Bullet()

