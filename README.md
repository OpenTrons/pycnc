# Python CNC Drivers

This repository serves two purposes:

1. Interface between the SmoothieBoard and Python via USB
2. Serve as an example of proper Python module structure.

You're probably here for the second reason.

## Installation

From the root directory, type:

    python ./setup.py install

This will install your module, as well as its dependencies, and allow you to use included binary commands on your system.

## Running the Tests

To see if everything works as it should, especially after making changes, you can type:

	nosetests

Again, from the root directory.

## Test Coverage Map

If you want to see which lines of the module are lacking adequate code coverage, you can type:

	nosetests --with-coverage

This will produce a list of all files and the lines that haven't been covered.  Code coverage includes conditional branches.

While in an ideal world, we'd have 100% coverage, this becomes difficult for things like Serial drivers, where we're executing device-specific code to connect under real-world conditions and using a mockup during test.

Try to cover as much as possible. For example, you can test device-specific behavior, and try to test on as many different platforms as possible. This will show up as incomplete test coverage on any given device, but provide full coverage when everyone runs tests on their own systems.

### Mock classes

This repository contains an example of using the mock class MockSerial, which pretends to be a serial port connection.  In reality, it simply saves data written to it and returns this information to the test cases.

### Custom assertions

Custom assertions (in a parent UnitTest class instance) can make your tests much more readable.

For example, in concert with our MockSerial class, we can write assertions which very specifically state what we're trying to ensure has happened within the system as a result of our test activity.

		self.assertLastCommand('G999')
		self.assertLastArguments('X1', 'Y1', 'Z1')

When an assertion fails, we get a domain-specific error message:

	AssertionError: Last CNC command (G28) matches one of: G0

What this tells us is that we were expecting the last CNC command to be G28, but instead it was G0.  Don't be afraid to use `*args` and `**kwargs` to make this code work harder for you.

## Executable scripts

Executable scripts live in ./bin.  You'll also need to add them to the scripts array inside of setup.py.

If you want to run Python code on the command line, add the following line to the top of the file:

	#!/usr/bin/env python

You can then import your module packages and use them like normal.

On the command line, run `chmod +x <filename>` to ensure that all the script files are executable.
