#! /usr/bin/env python

"""This class reads in and processes 
	input text from a file"""

import unittest

class FileIoTest(unittest.TestCase):	

	det setUp(self):
		self.fileIo = FileIo("input.txt")

	def tearDown(self):
		self.fileIo = None

	def toStringTest(self):
		"""Prints out the contents of the input file"""
		assert
		print str(self.fileIo.inputFile())

	def getFileTest(self):
		"""Returns the contents of the input file as a string"""
		return self.inputFile

