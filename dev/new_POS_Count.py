#! /usr/bin/env python

import nltk
import re
from fileIo import *



def countNouns( aList ):
	"""
	Takes a list of lists of strings with POS information and returns 
	the count of total nouns in each sub-list.
		
	Args:
		aList: a list of lists of strings for processing
				ex.  [["text, NN"],["text2, NN"]]

	Returns:
		Integer value of the count of total nouns in list
	"""
	totalNounCount = 0
	nounCount = 0
	findNoun = re.compile('NN')
	for x in aList:
		for y in x:
			if findNoun.search(str(y)) is not None:
				nounCount += 1
		print( nounCount )
		print( "\n" )
		totalNounCount += nounCount
		nounCount = 0
	return totalNounCount

def countVerbs( aList ):
	"""
	Takes a list of lists of strings with POS information and returns 
	the count of total verbs in each sub-list.
		
	Args:
		aList: a list of lists of strings for processing
				ex.  [["text, VB"],["text2, VB"]]

	Returns:
		Integer value of the count of total verbs in list
	"""
	totalVerbCount = 0
	verbCount = 0
	findVerb = re.compile('VB')
	for x in aList:
		for y in x:
			if findVerb.search(str(xy) is not None:
				verbCount += 1
		print( verbCount )
		print( "\n" )
		totalVerbCount += verbCount
		verbCount = 0
	return totalVerbCount

def countAdjectives( aList ):
	"""
	Takes a list of lists of strings with POS information and returns 
	the count of total adjectives in each sub-list.
		
	Args:
		aList: a list of lists of strings for processing
				ex.  [["text, JJ"],["text2, JJ"]]

	Returns:
		Integer value of the count of total adjectives in list
	"""
	totalAdjectiveCount = 0
	adjectiveCount = 0
	findAdjective = re.compile('JJ')
	for x in aList:
		for y in x:
			if findAdjective.search(str(x)) is not None:
				adjectiveCount += 1
		print adjectiveCount
		print ("\n")
		totalAdjectiveCount += adjectiveCount
		adjectiveCount = 0
	return totalAdjectiveCount
	
def main ():
	"""
	Main method to test functions

	"""

	fio = fileIo('input.txt')
        text = fio.getInput()

	p = re.compile(r'#?\d[\s\.]?[\s]?')
	out = filter(None, p.split(text))
	i = 0
	listOfLists = []
	

	for s in out:
		i += 1
		text = nltk.word_tokenize(s)
		pos = nltk.pos_tag(text)
		pattern = "NP: {<DT>?<JJ>*<NN>}"
		NPChunker = nltk.RegexpParser(pattern)
		result = NPChunker.parse(pos)
		listOfLists.append( result )

	print "Noun Count:\n" + str(countNouns( listOfLists ))
	print "Verb Count:\n" + str(countVerbs( listOfLists ))
	print "Adjective Count:\n" + str(countAdjectives( listOfLists ))
	
	
if __name__ == '__main__':
	main()
