#! /usr/bin/env python

"""This class offers several methods to processes input using the NLTK and other libraries."""

import re
import nltk
import numpy

from fileIo import *

class InputProcessor:
	
	"""
	self.blockList:  list of blocks split off of block number (##1)

	self.outputList:  2D array.  Row 0 is header row [block,text,tag].  
			  Each additional row contains data for an individual block.
	"""		

	def __init__(self):
		"""Initializes a new empty InputProcessor object."""
		pass

	def parseBlock(self,inFile):
		"""
		Parses inpput text into individual blocks.
		
		Args:
			inFile: Text with blocks denoted by ##<num>
				ex.  ##1 First block of text
				     ##2 Second block of text

		Returns:
			A list of blocks split on the (##<num>) block delimiter.
		 """

		blockRegEx = re.compile(r'##\d[\s\.]?[\s]?')
		tempList = filter(None, blockRegEx.split(inFile))
		self.blockList = []

		# strip newlines from each block
		for block in tempList:
			self.blockList.append( block.rstrip() )

		return self.blockList
		
	def sepTag(self,blocks):
		"""
		Separate tags from input blocks and organizes into a list.

		Args:
			blocks:  A list with one block per index.  Tags are denoted by [[<tag1>,<tag2>]].
				 ex. First block of text [[tag1,tag2]]

		Returns: 
			A two-dimensional array.
			Row 0 contains headers [block, test, tag].  
			Block contains the index number of the block.
			Test contains the text of the block.
			Tag contains the tags associated with the block.
		"""

		self.outputList = ['block','text','tag']
		tagRegEx = re.compile(r'\[\[(.+?)\]\]')
		blockCounter = 0

		for block in blocks:
			blockCounter += 1
			tagFound = re.search(tagRegEx, block)  # search block for regex match
			if tagFound:
				tag = tagFound.group(1)  # store tag value in tag
			blockText = re.sub(tagRegEx,'',block)  # remove tag from block text
			tempList = [str(blockCounter),blockText,tag]  # generates new row to be added to outputList
			self.outputList = numpy.vstack([self.outputList,tempList])  # add tempList as new row to self.outputList

		return self.outputList

	def numBlocks(self):
		"""
		Returns the number of blocks in self.outputList.  
		Because there is header row, this is number of rows minus 1.
	
		Args:
			None

		Returns:
			Integer value of blocks in the list
		"""	

		num = len(self.outputList)
		blocks = num - 1
	
		return blocks

        def numCols(self):
                """
                Returns the number of columns in self.outputList.  
        
                Args:
                        None

                Returns:
                        Integer value of columns in the list
                """

                num = len(self.outputList[0])

                return num

        def printColumn(self,colNum):
                """
                Prints out a particular column in self.outputList based on input parameter.  
        
                Args:
                        colNum:  The column number to be printed. The list is zero-based, so 0 is the leftmost column.

                Returns:
                        None
                """

		print "\nPrinting column " + str(colNum)
		for val in self.outputList:
			print val[colNum]            


	def printRow(self,rowNum):
                """
                Prints out a particular row in self.outputList based on input parameter.  
        
                Args:
                        rowNum:  The row number to be printed. The list is zero-based, so 0 is the first row. 
				 Thr first row is also the header row.

                Returns:
                        None
                """
		
		sol = self.outputList
		count = 0
                print "\nPrinting row " + str(rowNum) + "..." 
		for val in sol[rowNum]:
			print "\n" + sol[0][count] + ":\n\t" + val
			count += 1

        def tokenize(self, blockNum='allBlocks'):
                """
                Tokenizes a block of text using nltk.word_tokenize.  
        
                Args:
                        blockNum:  (default:  allBlocks) If a blockNum is provided, only that particular block is tokenized. 
				If no blockNum is provided, all blocks are tokenized.

                Returns:
                        If blockNum is specified, returns a list of tokenized words. 
			If blockNum is not specifies, returns a list of tokenized lists.
                """

		if blockNum == 'allBlocks':
			print "allBlocks"
			returnList = []
			for block in self.outputList:
				returnList.append(nltk.word_tokenize(block[1]))
				
		else:
			returnList = nltk.word_tokenize(self.outputList[blockNum][1])
		
		return returnList

def main():
	"""
	Main method to run test cases.
	"""
	print "In main..."

	fio = fileIo('input.txt')
	inFile = fio.getInput()
	#print inFile

	ip = InputProcessor()

	blocks = ip.parseBlock(inFile)
#	print blocks[1]

	list = ip.sepTag(blocks)
#	for x in list:
#      		print "\n\n"
#	       	print x

	rows = ip.numBlocks()
#	print rows

	cols = ip.numCols()
#	print cols

#	ip.printColumn(2)	

#	ip.printRow(1)

	tokens = ip.tokenize()
	print tokens

if __name__ == '__main__':
	main()
