__author__ = 'fleeting_chen'


from socket import *
import math
import pygame
from pygame.locals import *
from classes import terrain

HOST = 'localhost'
PORT = 9000
BUFSIZE = 1024
ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)
while True:
	data = raw_input('>')
	# data = test_pb2.Test()
	# # # data.x = 1
	# # data.y = 2
	# test = data.SerializeToString()
	client.sendall(data)
	rec = client.recv(BUFSIZE)
	if not rec:
		break
	print rec.strip()
client.close()
