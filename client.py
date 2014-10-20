__author__ = 'fleeting_chen'


from socket import *
import gevent
from gevent.socket import *
import math
import pygame
from pygame.locals import *
from classes import terrain
from classes.message import *
from classes.base_server import BaseServer
from proto import rabbit_pb2

HOST = 'localhost'
PORT = 9000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# client = socket(AF_INET, SOCK_STREAM)
# client.connect(ADDR)
# msg = 'start'
# client.sendall(msg)
# rabbits = []
# while True:
# 	rec = client.recv(BUFSIZE)
# 	if not rec:
# 		continue
# 	msgs = rabbit_pb2.Rabbits()
# 	msgs.ParseFromString(rec)
# 	print msgs
	# for rbt in msgs.rabbit:
	# 	rabbits.append(protobuf_2_rabbit(rbt))
	# print rabbits
# client.close()

class BattleClient(BaseServer):
	def on_data(self, data):
		print data
		# msg = message.all_messages.pack_rabbit_message(rabbits)
		# socket.send(msg)

		# for rbt in rabbits:
		# 	msg = rabbit_2_protobuf(rbt)
		# 	socket.send(msg.SerializeToString())

class ClientManage():
	def _run(self):
		client = socket(AF_INET, SOCK_STREAM)
		client.connect(ADDR)
		bc = BattleClient(client)
		bc.start()

		data = 'hello'
		bc.put_data(data)
		bc.send_data()

cm = ClientManage()
cm._run()