import nltk
import re

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
#print "\n".join(out)

def countNouns( aList ):
	nounCount = 0
	findNoun = re.compile('NN')
	for x in aList:
		if findNoun.search(str(x)) is not None:
			nounCount += 1
	print( nounCount )

def countVerbs( aList ):
	verbCount = 0
	findVerb = re.compile('VB')
	for x in aList:
		if findVerb.search(str(x)) is not None:
			verbCount += 1
	print( verbCount )

def countAdjectives( aList ):
	adjectiveCount = 0
	findAdjective = re.compile('JJ')
	for x in aList:
		if findAdjective.search(str(x)) is not None:
			adjectiveCount += 1
	print( adjectiveCount )
	
	
