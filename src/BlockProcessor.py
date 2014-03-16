#! /usr/bin/env python

"""This class offers several methods to processes blocks of text using NLTK and other libraries."""

import re
import nltk

from FileIo import *
from InputProcessor import *

class BlockProcessor:

	def __init__(self):
		"""Initializes a new empty BlockProcessor object."""
		pass

##############################################################################

	def countNouns( self, aList ):
		"""
		Takes a list of strings and returns the count of total nouns in list.
		
		Args:
			aList: a list of strings for processing
					ex.  "text"

		Returns:
			Integer value of the count of total nouns in list
		"""
		nounCount = 0
		#print aList
		findNoun = re.compile('NN')
		for x in aList:
			for y in x:
				print "Scanning..." + str(y)
				if findNoun.search(str(y)) is not None:
					nounCount += 1
			print( nounCount )
			nounCount = 0
		return nounCount

##############################################################################

	def countVerbs( aList ):
		"""
		Takes a list of strings and returns the count of total verbs in list.
		
		Args:
			aList: a list of strings for processing
					ex.  "text"

		Returns:
			Integer value of the count of total verbs in list
		"""
		verbCount = 0
		findVerb = re.compile('VB')
		for x in aList:
			if findVerb.search(str(x)) is not None:
				verbCount += 1
	#	print( verbCount )
		return verbCount

##############################################################################

	def countAdjectives( aList ):
		"""
		Takes a list of strings and returns the count of total adjectives in list.
		
		Args:
			aList: a list of strings for processing
					ex.  "text"

		Returns:
			Integer value of the count of total adjectives in list
		"""
		adjectiveCount = 0
		findAdjective = re.compile('JJ')
		for x in aList:
			if findAdjective.search(str(x)) is not None:
				adjectiveCount += 1
	#	print( adjectiveCount )
		return adjectiveCount

##############################################################################
		
	def chunkNounPhrase(self, list):
		"""
		Processes the 2nd column of the 2D array row by row - for each row 
		the block is tokenized, tagged, noun phrases are chunked out
		the variable result is a text based representation of a tree w/ 'S' as 
		the head

        Args:
                TODO

        Returns:
                TODO
        """

		i=-1
		for s in list:
			#i += 1
			#text = nltk.word_tokenize(s[1])
			#print text
			pos = nltk.pos_tag(s)
			#print pos
			# regex pattern to define noun phrase
			pattern = "NP: {<DT>?<JJ>*(<NN>|<NNP>|<NNPS>|<NNS>)*}"
			NPChunker = nltk.RegexpParser(pattern)
			result = NPChunker.parse(pos)
		#	print "Chunked POS TAG:::Block " + str(i)
			print result
		
################################################################################
		
	def getPOS (self, aList):
		posList = []
		for block in aList:
			text = nltk.word_tokenize(block[1])
			pos = nltk.pos_tag(text)
			posList.append(pos)
		return posList

##############################################################################

	def wordCount( self,aList ):
		"""
		Takes a list of strings and returns the count of total words in list.
		
		Args:
			aList: a list of strings for processing
					ex.  ['text1','text2',...]

		Returns:
			Integer value of the count of total words in list
		"""
		
		#### TODO This counts periods.  Need to regex these out
	  	wordCount = 0
	  	for block in aList:
	  		text = nltk.word_tokenize(block)
	  		for word in text:
	  			wordCount += 1
	  	
	  	return wordCount

	

















		
		
		
		
		
		
		
		
