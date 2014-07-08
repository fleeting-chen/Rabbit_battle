__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

import bullet
SHOT_INTERVAL = 1

class Arrow(object):
	interval = SHOT_INTERVAL
	def __init__(self):
		self.last_shot_time = 0
