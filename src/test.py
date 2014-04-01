#! /usr/bin/env python

from FileIo import *
from InputProcessor import *
from BlockProcessor import *
import nltk
from Switch import *
import sys
import os

os.system('clear')
input = "../input2.txt"
#input = "input2"
fio = FileIo(input)
ip = InputProcessor()
bp = BlockProcessor()
processInput = ip.processInput(fio.getFile())
tokenize = ip.tokenize()

print "Original input text:"
print "###################################################################################\n\n"
fio.toString();

print "\n###################################################################################\n\n"

if (len(sys.argv) == 2):
    choice = str(sys.argv[1])	
else:
    choice = raw_input("""
    Please enter the number of the test to run:
    \tq) quit
    \t1) processInput()
    \t2) tokenize()
    \t3) posTagger()
    \t4) phraseChunker() for nouns
    \t5) phraseChunker() for verbs
    \t6) countNouns()
    \t7) countVerbs()
    \t8) countAdjectives()
    \t9) countPronouns()
    \t10) countAdverbs()
    \t11) countOther()
    \t12) wordCount()
    \t13) updateArray()
    \t14) distinctWordCount()
    \t15) tf_idf_Count()
    """)

#print choice

for case in Switch(choice):
    if case('q'):
        sys.exit("Thanks for playing")
    if case('1'):
        print"Preparing to run processInput()"
        print "###################################################################################\n\n"
        processInput = ip.processInput(fio.getFile())
        print processInput
        print "\n###################################################################################\n\n"
        break
    if case('2'):
        print"Preparing to run tokenize()"
        print "\n###################################################################################\n\n"
        tokenize = ip.tokenize()
        print tokenize
        print "\n###################################################################################\n\n"
        break
    if case('3'):
        print"Preparing to run posTagger()"
        print "\n###################################################################################\n\n"
        posTagger = bp.posTagger(processInput)
        print posTagger
        print "\n###################################################################################\n\n"
        break
    if case('4'):
        print"Preparing to run phraseChunker() for nouns"
        print "\n###################################################################################\n\n"
        pattern = """
                NP: {<DT|PP\$>?(<JJ>|<JJR>|<JJS>)*(<NN>|<NNP>|<NNPS>|<NNS>|<POS>)+}
                    {<NNP>+}
                    {<NN>+}
                    {<PRP>+}
        """
        nounPhrase = bp.phraseChunker(tokenize, pattern)
        for tree in nounPhrase:
            print tree
        print "\n###################################################################################\n\n"
        break
    if case('5'):
        print"Preparing to run phraseChunker() for verbs"
        #print"Except it's not ready yet...." # still need to define verb phrase pattern
        #break
        print "\n###################################################################################\n\n"
        pattern = """
                VP: {<MD|TO|RB>?(<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBZ>)+<RB>?}
        """
        verbPhrase = bp.phraseChunker(tokenize, pattern)
        for tree in verbPhrase:
            print tree
        print "\n###################################################################################\n\n"
        break
    if case('6'):
        print"Preparing to run countNouns()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        nouns = bp.countNouns(pos)
        print "\nTotal nouns found: " + str(nouns)
        print "\n###################################################################################\n\n"
        break
    if case('7'):
        print"Preparing to run countVerbs()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        verbs = bp.countVerbs(pos)
        print "\nTotal verbs found: " + str(verbs)
        print "\n###################################################################################\n\n"
        break
    if case('8'):
        print"Preparing to run countAdjectives()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        adjectives = bp.countAdjectives(pos)
        print "\nTotal adjectives found: " + str(adjectives)
        print "\n###################################################################################\n\n"
        break
    if case('9'):
        print"Preparing to run countPronouns()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        pronouns = bp.countPronouns(pos)
        print "\nTotal pronouns found: " + str(pronouns)
        print "\n###################################################################################\n\n"
        break
    if case('10'):
        print"Preparing to run countAdverbs()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        adverbs = bp.countAdverbs(pos)
        print "\nTotal adverbs found: " + str(adverbs)
        print "\n###################################################################################\n\n"
        break
    if case('11'):
        print"Preparing to run countOther()"
        print "###################################################################################\n\n"
        pos = bp.posTagger(processInput)
        other = bp.countOther(pos)
        print "\nTotal other found: " + str(other)
        print "\n###################################################################################\n\n"
        break
    if case('12'):
        print"Preparing to run wordCount()"
        print "\n###################################################################################\n\n"
        words = bp.wordCount(ip.getBlock(processInput))
        print "Total word count: " + str(words) + "\n\n"
        print "\n###################################################################################\n\n"
        break
    if case('13'):
        print"Preparing to run updateArray()"
        print "\n###################################################################################\n\n"
        #processInput = bp.updateArray(processInput,5,'breakIt',42)
        processInput = bp.updateArray(processInput,5,'nounCount',42)
        processInput = bp.updateArray(processInput,5,'verbCount',42)
        processInput = bp.updateArray(processInput,5,'pronounCount',42)
        processInput = bp.updateArray(processInput,5,'adjCount',42)
        processInput = bp.updateArray(processInput,5,'adverbCount',42)
        processInput = bp.updateArray(processInput,5,'otherCount',42)
        processInput = bp.updateArray(processInput,5,'totalWordCount',42)
        processInput = bp.updateArray(processInput,5,'distinctWordCount',42)
        print processInput
        print "\n###################################################################################\n\n"
        break
    if case('14'):
        print "Preparing to run distinctWordCount()"
        print "\n###################################################################################\n\n"
        temp = bp.distinctWordCount(tokenize)
        print "\n###################################################################################\n\n"
        break
    if case('15'):
        print "Preparing to run tf_idf_Count()"
        print "\n###################################################################################\n\n"
        temp = bp.tf_idf_Count(tokenize)
        print "\n###################################################################################\n\n"
        break
    if case():
         print "\n###################################################################################\n\n"
         raise Exception("Invalid choice selected")
        



















