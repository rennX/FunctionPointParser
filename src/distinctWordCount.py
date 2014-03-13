#! /usr/bin/env/ python

import nltk
import re
from fileIo import *

def distinctWords( aList ):
	"""
	Takes a list of strings and returns the count of total distinct words in list.
		
	Args:
		aList: a list of strings for processing
				ex.  ['text1','text2',...]

	Returns:
		Integer value of the count of total distinct words in list
	"""
  	text = []
  	for x in aList:
  		y = x.lower()
  		text.append( y )
  	return len(set(text))
  	
  	
 def totalDistinctWords( aList ):
	"""
	Takes a list of lists of strings and returns the count of total distinct words in entire list.
		
	Args:
		aList: a list of list of strings for processing
				ex.  [['text1','text2',...], ['text1', 'text3']]

	Returns:
		Integer value of the count of total distinct words in entire list
	"""
  	text = []
  	for x in aList:
  		for z in x:
  			y = z.lower()
  			text.append( y )
  	return len(set(text))


def main ():
	"""
	Main method to test functions

	"""
	text = "two words"
	#fio = fileIo("input.txt")
	#text = fio.getInput()
	p = re.compile(r'#?\d[\s\.]?[\s]?')
	out = filter(None, p.split(text))
	#print out[2]
	#print len(out)
	i = 0

	for s in out:
		i += 1
		text = nltk.word_tokenize(s)
		
	dw = distinctWords( text )
	print dw


if __name__ == '__main__':
	main()
