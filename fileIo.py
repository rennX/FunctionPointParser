#! /usr/bin/env python

"""This class reads in and processes 
	input text from a file"""

class fileIo:
			

	def __init__(self, file):
		"""Opens input file for reading. Saves
			file to 'inputFile'. Then closes
			the input file."""
		self.f = open(file)
		self.inputFile = self.f.read()
		self.f.close()
		
	def displayInput(self):
		"""Prints out the contents of the input file"""
		print self.inputFile

	def getInput(self):
		"""Returns the contents of the input file"""
		return self.inputFile

