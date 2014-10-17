__author__ = 'chenhao'
__date__ = '14-7-7'
#encoding:utf-8

BULLET_VELOCITY = 10
BULLET_IMG_DIR = 'resources/images/bullet.png'
class Bullet(object):
	velocity = BULLET_VELOCITY
	img = BULLET_IMG_DIR
	member = None
	def __init__(self, angle, position):
		self.angle = angle
		self.position= position

	def move(self, x, y):
		self.position[0] += x
		self.position[1] += y
