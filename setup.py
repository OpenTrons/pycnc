try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': "Python CNC drivers",
	'author': "OpenTrons",
	'url': 'http://opentrons.com',
	'version': '0.1',
	'install_requires': [
		'nose',
		'coverage',
		'pyserial'
	],
	'packages': ['pycnc'],
	'scripts': ['./bin/cnc-hello'],
	'name': 'pycnc'
}

setup(**config)
