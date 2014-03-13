#! /usr/bin/env python

from FileIo import *
from InputProcessor import *
from BlockProcessor import *
import nltk

    
input = "../input2.txt"
#input = "input2"
fio = FileIo(input)
ip = InputProcessor()
bp = BlockProcessor()

raw_input("Preparing to run processInput(). Press Enter to continue...")
processInput = ip.processInput(fio.getFile())
print processInput

raw_input("\nPreparing to run tokenize(). Press Enter to continue...")
tokenize = ip.tokenize()
print tokenize

raw_input("\nPreparing to run chunkNounPhrase(). Press Enter to continue...")
chunkNounPhrase = bp.chunkNounPhrase(tokenize)
print chunkNounPhrase

raw_input("\nPreparing to run nounCount(). Press Enter to continue...")
#nouns = bp.countNouns(chunkNounPhrase)
#print nouns
pos = bp.getPOS(processInput)
print "\n"
nouns = bp.countNouns(pos)
print nouns


#for x in pos:
#	print x

raw_input("\nPreparing to run wordCount(). Press Enter to continue...")
words = bp.wordCount(ip.getBlock(processInput))
print words


	
