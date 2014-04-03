#! /usr/bin/env python
import re
import nltk
import numpy

# this can be its own function
# it open a text file for reading
file = '../input.txt'
f = open(file)
input = f.read()
f.close()


# this can be its own function
# it splits the input text into blocks
blockRegEx = re.compile(r'##\d[\s\.]?[\s]?')
out = filter(None, blockRegEx.split(input))

# this can be its own function
# list is initialized with headings - 
# then the regex pattern for tags is set
# then a 2D array is populated with data
# one block per row
list = ['block','text','tag']
tagRegEx = re.compile(r'\[\[(.+?)\]\]')
i=0

for x in out:
	i += 1
	m = re.search(tagRegEx, x)
	if m:
	    tag = m.group(1)
	x = re.sub(tagRegEx,'',x)
	list2=[str(i),x,tag]
	list = numpy.vstack([list,list2])
print len(out)
print list

# test to check number of rows and columns
numrows = len(list)
numcols = len(list[0])
print "Num Rows: " + str(numrows-1) + ":: Num Cols: " + str(numcols)

# test to print tags column only
i=0
for t in list:
	i += 1
	print t[2]

# this can be its own function
# it processes the 2nd column of the 
# 2D array row by row - for each row 
# the block is tokenized, tagged, 
# noun phrases are chunked out
# the variable result is a text based
# representation of a tree w/ 'S' as 
# the head
i=-1
for s in list:
	i += 1
	text = nltk.word_tokenize(s[1])
	print text
	pos = nltk.pos_tag(text)
	# regex pattern to define noun phrase
	pattern = "NP: {<DT>?<JJ>*<NN>}"
	NPChunker = nltk.RegexpParser(pattern)
	result = NPChunker.parse(pos)
#	print "Chunked POS TAG:::Block " + str(i)
	print result
	



