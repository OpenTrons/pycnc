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

While in an ideal world, we'd have 100% coverage, this becomes difficult for things like Serial drivers, where we're executing device-specific code to connect to mocked up serial drivers.

## Executable scripts

Executable scripts live in ./bin.  You'll also need to add them to the scripts array inside of setup.py.

If you want to run Python code on the command line, add the following line to the top of the file:

	#!/usr/bin/env python

You can then import your module packages and use them like normal.

On the command line, run `chmod +x <filename>` to ensure that all the script files are executable.
