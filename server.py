__author__ = 'fleeting_chen'

import gevent
from gevent.server import StreamServer
# import SocketServer
# from SocketServer import StreamRequestHandler as SRH
from classes.rabbit import Rabbit
from classes.terrain import Terrain
from classes import message
from classes.base_server import BaseServer
from proto import rabbit_pb2
import random
import struct

rabbits = []
for i in range(0,2):
	x = random.randint(0, Terrain.size[0])
	y = random.randint(0, Terrain.size[1])
	tmp_rbt = Rabbit(1, [x, y])
	rabbits.append(tmp_rbt)

# msgs = rabbit_pb2.Rabbits()
# for rbt in rabbits:
# 	msg = rabbit_2_protobuf(rbt)
	# msgs.rabbit.append(msg)
	# addRabbit(rbt, msgs.rabbit.add())
# class BattleServer(SRH):
# 	def handle(self):
# 		print "connection from:", self.client_address
# 		test = test_pb2.Test()
		# while True:
		# 	data = self.request.recv(1024)
		# 	if not data:
		# 		break
		# 	print data
		# 	print "RECV from ", self.client_address[0]
		# 	self.request.send(data.upper())

# if __name__ == "__main__":
# 	addr = ('localhost', 9000)
# 	print 'server start:'
# 	server = SocketServer.ThreadingTCPServer(addr, BattleServer)
# 	server.serve_forever()

class BattleServer(BaseServer):
	# def handle(self, socket, address):
	# 	print "connection from:", address
	# 	while True:
	# 		data = socket.recv(1024)
	# 		if data == 'start':
	# 			break
	#
	# 	msg = message.all_messages.pack_rabbit_message(rabbits)
	# 	socket.send(msg)

		# for rbt in rabbits:
		# 	msg = rabbit_2_protobuf(rbt)
		# 	socket.send(msg.SerializeToString())

	def on_data(self, msg):
		# data = rabbit_pb2.Rabbits()
		# data.ParseFromString(msg)
		print msg
		self.put_data('hello,moto')
		self.send_data()

class ServerManage(gevent.Greenlet):
	def __init__(self):
		gevent.Greenlet.__init__(self)

	def handle(self, my_socket, address):
		print "connection from:", address
		bs = BattleServer(my_socket)
		bs.start()

	def _run(self):
		addr = ('localhost', 9000)
		print 'server start:'
		server = StreamServer(addr, self.handle)
		server.serve_forever()

SM = ServerManage()
SM._run()