class MockSerial():

	open = False

	def __init__(self):
		self.write_buffer = []

	def isOpen(self):
		return True

	def close(self):
		self.open = False

	def open(self):
		self.open = True

	def write(self, data):
		if self.isOpen() is False:
			raise IOError("Connection not open.")
		self.write_buffer.append(data)

	def read(self, data):
		if self.isOpen() is False:
			raise IOError("Connection not open.")
		return None