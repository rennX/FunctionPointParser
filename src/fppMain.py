#! /usr/bin/env python

from FileIo import *
from InputProcessor import *
from BlockProcessor import *
from Switch import *
import sys, os
import nltk

##############################################################################

# initialize variables
input = "../input2.txt"
fio = FileIo(input)
ip = InputProcessor()
bp = BlockProcessor()

the2DArray = ip.processInput(fio.getFile())
tokenized = ip.tokenize(the2DArray)
pos = bp.posTagger(the2DArray)
totalNouns = None

##############################################################################

# noun and verb phrase chunking
nounPattern = """
        NP: {<DT|PP\$>?(<JJ>|<JJR>|<JJS>)*(<NN>|<NNP>|<NNPS>|<NNS>|<POS>)+}
        {<NNP>+}
        {<NN>+}
        {<PRP>+}
        """
verbPattern = """
        VP: {<MD|TO|RB>?(<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBZ>)+<RB>?}
        """
nounChunk = bp.phraseChunker(tokenized, nounPattern)
verbChunk = bp.phraseChunker(tokenized, verbPattern)

##############################################################################

# count nouns per block and total, update the2DArray
nounDict = bp.countNouns(pos)
for key, value in nounDict.iteritems() :
    if key is 'total':
        totalNouns = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'nounCount',value)

##############################################################################

# count verbs per block and total, update the2DArray
verbDict = bp.countVerbs(pos)
for key, value in verbDict.iteritems() :
    if key is 'total':
        totalVerbs = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'verbCount',value)

##############################################################################

# count adjectives per block and total, update the2DArray
adjectiveDict = bp.countAdjectives(pos)
for key, value in adjectiveDict.iteritems() :
    if key is 'total':
        totalAdjectives = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'adjectiveCount',value)

##############################################################################

# count pronouns per block and total, update the2DArray
pronounDict = bp.countPronouns(pos)
for key, value in pronounDict.iteritems() :
    if key is 'total':
        totalPronouns = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'pronounCount',value)

##############################################################################

# count adverbs per block and total, update the2DArray
adverbDict = bp.countAdverbs(pos)
for key, value in adverbDict.iteritems() :
    if key is 'total':
        totalAdverbs = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'adverbCount',value)

##############################################################################

# count other parts of speech per block and total, update the2DArray
otherDict = bp.countOther(pos)
for key, value in otherDict.iteritems() :
    if key is 'total':
        totalOther = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'otherCount',value)

##############################################################################

# count words per block and total, update the2DArray
wordCountDict = bp.countOther(pos)
print wordCountDict
for key, value in wordCountDict.iteritems() :
    if key is 'total':
        totalWordCount = value
    else:
        the2DArray = bp.updateArray(the2DArray,key,'totalWordCount',value)

##############################################################################

#print "Nouns: "+str(totalNouns)
#print "Verbs: "+str(totalVerbs)
#print "Adjectives: "+str(totalAdjectives)
#print "Pronouns: "+str(totalPronouns)
#print "Adverbs: "+str(totalAdverbs)
#print "Other: "+str(totalOther)
#print "Word Count: "+str(totalWordCount)


##TODO To handle a the totals we will need to add an additional row to 
##TODO the2DArray.  It can be block number 'total', block text
##TODO 'This row contains totals of the parts of speech and word count.'
##############################################################################

# process distinct word count and TF-IDF 
distinctWordCountArray = bp.distinctWordCount(tokenized)
tf_idfArray = bp.tf_idf_Count(tokenized)

##############################################################################

# now we have out 3 data structures, lets convert to csv
numpy.savetxt("./output/the2DArray.csv", the2DArray, delimiter=",", fmt="%s")
numpy.savetxt("./output/distinctWordCountArray.csv", distinctWordCountArray, delimiter=",", fmt="%s")
numpy.savetxt("./output/tf_idfArray.csv", tf_idfArray, delimiter=",", fmt="%s")





















