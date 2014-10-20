__author__ = 'fleeting_chen'

import gevent
from gevent.queue import Queue
import struct

class BaseServer(gevent.Greenlet):
	def __init__(self, transport):
		self.transport = transport
		self.header_fmt = struct.Struct('>i')
		self.inbox = Queue()
		self.jobs = []

		gevent.Greenlet.__init__(self)

	def connection_closed(self):
		raise NotImplementedError()

	def connection_lost(self):
		raise NotImplementedError()

	def recv_data(self):
		while True:
			try:
				length = self.transport.recv(4)
				if not length:
					self.connection_closed()
					break
				length = self.header_fmt.unpack(length)[0]
				data = self.transport.recv(length)
			except:
				self.connection_lost()
				break

			self.on_data(data)

	def send_data(self):
		while True:
			data = self.inbox.get()
			data_length = len(data)
			fmt = '>i%ds' % data_length
			data_struct = struct.Struct(fmt)
			data = data_struct.pack(data_length, data)
			self.transport.sendall(data)

	def put_data(self, data):
		self.inbox.put(data)

	#would be overrided in the child class
	def on_data(self, data):
		raise NotImplementedError()

	def terminate(self):
		gevent.killall(self.jobs)
		self.transport.close()
		self.kill()

	def _run(self):
		job_recv = gevent.spawn(self.recv_data)
		job_send = gevent.spawn(self.send_data)

		def _exit(glet):
			job_recv.unlink(_exit)
			job_send.unlink(_exit)
			self.terminate()

		job_recv.link(_exit)
		job_send.link(_exit)

		self.jobs.append(job_recv)
		self.jobs.append(job_send)
