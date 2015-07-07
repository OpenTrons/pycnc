import unittest
from pycnc.drivers import CNCDriver

from .mocks.serial import MockSerial
import re

class SerialTestCase(unittest.TestCase):

	def assertLastCommand(self, *commands):
		lastCommand = self.cnc.connection.write_buffer[-1]
		foundOne = False
		for command in commands:
			if lastCommand.startswith(command):
				foundOne = True
				break

		msg = "Expected last CNC command to be "

		if len(commands) is 1:
			msg += '"'+commands[0]+'" '
		else:
			msg += "one of: "+", ".join(commands)+" "

		msg += "but got \""+lastCommand.strip()+"\"."

		self.assertTrue(foundOne, msg=msg)

	def assertLastArguments(self, *arguments):
		lastCommand = self.cnc.connection.write_buffer[-1]
		for arg in arguments:
			msg = "Expected last command arguments to include "+\
			      "\""+arg+"\" but got \""+lastCommand.strip()+"\" instead."
			self.assertTrue(arg in lastCommand, msg=msg)

class CNCTest(SerialTestCase):

	def setUp(self):
		self.cnc = CNCDriver()
		self.cnc.connection = MockSerial()

	def test_home(self):
		self.cnc.home()
		self.assertLastCommand('G28')

	def test_move_x(self):
		self.cnc.move(x=1)
		self.assertLastCommand('G0', 'G1')
		self.assertLastArguments('X1')

	def test_move_y(self):
		self.cnc.move(y=1)
		self.assertLastCommand('G0', 'G1')
		self.assertLastArguments('Y1')

	def test_move_z(self):
		self.cnc.move(z=1)
		self.assertLastCommand('G0', 'G1')
		self.assertLastArguments('Z1')

	def test_send_command(self):
		self.cnc.send_command('G999 X1 Y1 Z1')
		self.assertLastCommand('G999')
		self.assertLastArguments('X1', 'Y1', 'Z1')

	def test_send_command_with_kwargs(self):
		self.cnc.send_command('G999', x=1, y=2, z=3)
		self.assertLastCommand('G999')
		self.assertLastArguments('X1', 'Y2', 'Z3')

	def test_wait(self):
		self.cnc.wait(1)
		self.assertLastCommand('G4')

	def test_halt(self):
		self.cnc.halt()
		self.assertLastCommand('M112')

	def test_resume(self):
		self.cnc.resume()
		self.assertLastCommand('M999')