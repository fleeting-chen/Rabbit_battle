__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

from arrow import Arrow

class Rabbit(object):
	def __init__(self,id,position):
		self.id = id
		self.position = position
		self.hp = 100
		self.img = "../resources/images/dude.png"
		self.arrow = Arrow()

