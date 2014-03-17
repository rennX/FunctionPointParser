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

print "\n###################################################################################\n"

print "Original input text:"
fio.toString();

print "\n###################################################################################\n\n"

raw_input("Preparing to run processInput(). Press Enter to continue...")
processInput = ip.processInput(fio.getFile())
print processInput

print "\n###################################################################################\n\n"

raw_input("Preparing to run tokenize(). Press Enter to continue...")
tokenize = ip.tokenize()
print tokenize

print "\n###################################################################################\n\n"

raw_input("Preparing to run posTagger(). Press Enter to continue...")
posTagger = bp.posTagger(processInput)
print posTagger

print "\n###################################################################################\n\n"

raw_input("Preparing to run chunkNounPhrase(). Press Enter to continue...")
chunkNounPhrase = bp.chunkNounPhrase(tokenize)
# print chunkNounPhrase

print "\n###################################################################################\n\n"

raw_input("Preparing to run nounCount(). Press Enter to continue...")

pos = bp.posTagger(processInput)
print "\n"
nouns = bp.countNouns(pos)
print "\nTotal nouns found: " + str(nouns)

print "\n###################################################################################\n\n"

raw_input("Preparing to run wordCount(). Press Enter to continue...")
words = bp.wordCount(ip.getBlock(processInput))
print "Total word count: " + str(words)





