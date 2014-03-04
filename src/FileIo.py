#! /usr/bin/env python

"""This class reads in and processes 
	input text from a file"""

class FileIo:
			

	def __init__(self, file):
		"""Opens input file for reading. Saves
			file to 'inputFile'. Then closes
			the input file."""
		self.f = open(file)
		self.inputFile = self.f.read()
		self.f.close()
		
	def toString(self):
		"""Prints out the contents of the input file"""
		print str(self.inputFile)

	def getFile(self):
		"""Returns the contents of the input file as a string"""
		return self.inputFile

