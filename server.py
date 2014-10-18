__author__ = 'fleeting_chen'

import SocketServer
from SocketServer import StreamRequestHandler as SRH
from classes.rabbit import Rabbit
from classes.terrain import Terrain
import random

rabbits = []
for i in range(0,2):
	x = random.randint(0, Terrain.size[0])
	y = random.randint(0, Terrain.size[1])
	tmp_rbt = Rabbit(1, [x, y])
	rabbits.append(tmp_rbt)

class BattleServer(SRH):
	def handle(self):
		print "connection from:", self.client_address
		# test = test_pb2.Test()
		# test.ParseFromString(data)
		while True:
			data = self.request.recv(1024)
			if not data:
				break
			print data
			print "RECV from ", self.client_address[0]
			self.request.send(data.upper())

if __name__ == "__main__":
	addr = ('localhost', 9000)
	print 'server start:'
	server = SocketServer.ThreadingTCPServer(addr, BattleServer)
	server.serve_forever()
