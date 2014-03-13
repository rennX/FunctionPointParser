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
	#print aList
	findNoun = re.compile('NN')
	for x in aList:
		for y in x
			if findNoun.search(str(y)) is not None:
				nounCount += 1
		print( nounCount )
		print( "\n" )
		totalNounCount += nounCount
		nounCount = 0
	#print( nounCount )
	return totalNounCount

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
	
def main ():
	"""
	Main method to test functions

	"""

	fio = fileIo('input.txt')
        text = fio.getInput()

	p = re.compile(r'#?\d[\s\.]?[\s]?')
	out = filter(None, p.split(text))
	#print out[2]
	#print len(out)
	i = 0

	for s in out:
		i += 1
		text = nltk.word_tokenize(s)
		#print text
		pos = nltk.pos_tag(text)
		#print pos
		pattern = "NP: {<DT>?<JJ>*<NN>}"
		NPChunker = nltk.RegexpParser(pattern)
		result = NPChunker.parse(pos)
		#print "Chunked POS TAG:::Block " + str(i)

	#print result
	print "Total nouns = " + str(countNouns( result ))
	print "Total verbs = " + str(countVerbs( result ))
	print "Total adjectives = " + str(countAdjectives( result ))
	
	
if __name__ == '__main__':
	main()
