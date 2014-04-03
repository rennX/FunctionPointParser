#! /usr/bin/env python

"""This class offers several methods to processes input using the NLTK and other libraries."""

import re
import nltk
import numpy

from FileIo import *

class InputProcessor:
	
	"""
	Attributes:
		self.blockList:  list of blocks split off of block number (##1)

		self.outputList:  2D array.  Row 0 is header row [block,text,tag].  
			  Each additional row contains data for an individual block.

		**Note:  most functions rely on the self.outputList attribute.  This is  returned by the sepTag() function
	"""		

##############################################################################

	def __init__(self):
		"""Initializes a new InputProcessor object. With """
		pass

##############################################################################

	def processInput (self,inFile):
		"""Parses properly formatted text file into a 2D array 
		
		Args:  
			Infile: Text with blocks denoted by ##<num>
				ex.  ##1 First block of text
				     ##2 Second block of text
				Tags are denoted by [[<tag1>,<tag2>]].
				ex. First block of text [[tag1,tag2]]
				
		Returns: 
			A two-dimensional array.
			Row 0 contains headers [block, test, tag].  
			Block contains the index number of the block.
			Test contains the text of the block.
			Tag contains the tags associated with the block.

		"""
		return (self._sepTag(self._parseBlock(inFile)))

##############################################################################

	def _parseBlock(self,inFile):
		"""
		Parses input text into individual blocks.
		
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

##############################################################################
		
	def _sepTag(self,blocks):
		"""
		Separate tags from input blocks and organizes into a list.

		Args:
			blocks:  A list with one block per index.  Tags are denoted by [[<tag1>,<tag2>]].
				 ex. First block of text [[tag1,tag2]]

		Returns: 
			A two-dimensional array.
			Row 0 contains headers ['blockNumber','blockText','blockTags', 'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount', 'totalWordCount', 'distinctWordCount'].  
			
			blockNumber contains the index number of the block.
			blockText contains the text of the block.
			blockTags contains the tags associated with the block.
			nounCount contains the number of nouns found in the block text.
			verbCount contains the number of verbs found in the block text.
			pronounCount contains the number of pronouns found in the block text.
			adjCount contains the number of adjectives found in the block text.
			adverbCount contains the number of adverbs found in the block text.
			otherCount contains the number of other text characters found in the block text.
			totalWordCount contains the number of words found in the block text.
			distinctWordCount contains the number of distinct words found in the block text.
		"""

		self.outputList = ['blockNumber','blockText','blockTags', 'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount', 'totalWordCount']  
		tagRegEx = re.compile(r'\[\[(.+?)\]\]')
		blockCounter = 0

		for block in blocks:
			blockCounter += 1
			tagFound = re.search(tagRegEx, block)  # search block for regex match
			if tagFound:
				tag = tagFound.group(1)  # store tag value in tag
			else:
			    tag = None
			blockText = re.sub(tagRegEx,'',block)  # remove tag from block text
			tempList = [str(blockCounter),blockText,tag, 0, 0, 0, 0, 0, 0, 0]  # generates new row to be added to outputList
			self.outputList = numpy.vstack([self.outputList,tempList])  # add tempList as new row to self.outputList
		tempList = ["total","This row contains overall totals of the parts of speech and word count", None, 0, 0, 0, 0, 0, 0, 0] # add total row to the2DArray
		self.outputList = numpy.vstack([self.outputList,tempList]) # add tempList as new row to self.outputList

		return self.outputList

##############################################################################

	def numBlocks(self, aList):
		"""
		Returns the number of blocks in aList.  
		Because there is header row, this is number of rows minus 1.
	
		Args:
			None

		Returns:
			Integer value of blocks in the list
		"""	

		num = len(aList)
		blocks = num - 1
	
		return blocks

##############################################################################

        def numCols(self, aList):
                """
                Returns the number of columns in aList.  
        
                Args:
                        None

                Returns:
                        Integer value of columns in the list
                """

                num = len(aList[0])

                return num

##############################################################################

        def printColumn(self, aList ,colNum):
                """
                Prints out a particular column in aList based on input parameter.  
        
                Args:
                        colNum:  The column number to be printed. The list is zero-based, so 0 is the leftmost column.

                Returns:
                        None
                """

		print "\nPrinting column " + str(colNum)
		for val in aList:
			print val[colNum]            

##############################################################################

	def printRow(self, aList ,rowNum):
                """
                Prints out a particular row in aList based on input parameter.  
        
                Args:
                        rowNum:  The row number to be printed. The list is zero-based, so 0 is the first row. 
				 Thr first row is also the header row.

                Returns:
                        None
                """
		
		sol = aList
		count = 0
                print "\nPrinting row " + str(rowNum) + "..." 
		for val in sol[rowNum]:
			print "\n" + sol[0][count] + ":\n\t" + val
			count += 1

##############################################################################

        def tokenize(self, aList, blockNum='allBlocks'):
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
			#print "allBlocks"
			returnList = []
			for block in aList:
				returnList.append(nltk.word_tokenize(block[1]))
				
				
		else:
			returnList = nltk.word_tokenize(aList[blockNum][1])
		
		return returnList

##############################################################################

	def getBlock(self, aList):
		"""
		Accepts a 2D array (aList).  Returns the column aList[1] minus the header (first) row.
		
		Args: aList
		
		Returns:  blockList - a list with one block per entry
		
		"""
		rowCount = 1
		blockList = []
		for row in aList:
			block = row[1]
			#print block
			blockList.append(row[1])
			rowCount+=1
	
		return blockList

