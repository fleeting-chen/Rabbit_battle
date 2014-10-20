__author__ = 'fleeting_chen'

from proto import rabbit_pb2
from classes.rabbit import Rabbit

def rabbit_2_protobuf(rabbit):
	msg = rabbit_pb2.Rabbit()
	msg.id = rabbit.id
	msg.position.x, msg.position.y = rabbit.position
	msg.hp = rabbit.hp
	msg.angle = rabbit.angle
	msg.status = 1

	return msg

def protobuf_2_rabbit(msg):
	rabbit = Rabbit(msg.id)
	rabbit.position = (msg.position.x, msg.position.y)
	rabbit.hp = msg.hp
	rabbit.angle = msg.angle

	return rabbit

def addRabbit(rabbit, msg):
	msg.id = rabbit.id
	msg.position.x, msg.position.y = rabbit.position
	msg.hp = rabbit.hp
	msg.angle = rabbit.angle
	msg.status = 1

class Messages(object):
	def pack_rabbit_message(self, rabbits):
		message = rabbit_pb2.Rabbits()
		for rbt in rabbits:
			addRabbit(rbt, message.rabbit.add())

		return message.SerializeToString()

all_messages = Messages()