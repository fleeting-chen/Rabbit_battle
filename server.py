__author__ = 'fleeting_chen'

import gevent
from gevent.server import StreamServer
from classes.rabbit import Rabbit
from classes.terrain import Terrain
from classes.base_server import BaseServer
from classes import message
from proto import rabbit_pb2
import random

rabbits = []
for i in range(0,2):
	x = random.randint(0, Terrain.size[0])
	y = random.randint(0, Terrain.size[1])
	tmp_rbt = Rabbit(1, [x, y])
	rabbits.append(tmp_rbt)

class BattleServer(BaseServer):
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