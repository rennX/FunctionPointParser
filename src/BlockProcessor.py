#! /usr/bin/env python

"""This class offers several methods to processes blocks of text using NLTK and other libraries."""

import re
import nltk

from FileIo import *
from InputProcessor import *
from Switch import *

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
        totalNounCount = 0
        findNoun = re.compile("\'NN\w?\w?\'")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findNoun.search(str(y)) is not None:
                    nounCount += 1
            print "\nScanning..." + str(x)
            print "\tNouns found: " + str(nounCount)  # TODO instead of printing here, call function to add to 2D array
            totalNounCount += nounCount
            nounCount = 0
        return totalNounCount

##############################################################################

    def countVerbs( self, aList ):
        """
        Takes a list of strings and returns the count of total verbs in list.

        Args:
                aList: a list of strings for processing
                                ex.  "text"

        Returns:
                Integer value of the count of total verbs in list
        """
        verbCount = 0
        totalVerbCount = 0
        findVerb = re.compile("\'VB\w?\'")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findVerb.search(str(y)) is not None:
                    verbCount += 1
            print "\nScanning..." + str(x)
            print "\tVerbs found: " + str(verbCount)  # TODO instead of printing here, call function to add to 2D array
            totalVerbCount += verbCount
            verbCount = 0
        return totalVerbCount

##############################################################################

    def countAdjectives( self, aList ):
        """
        Takes a list of strings and returns the count of total adjectives in list.

        Args:
                aList: a list of strings for processing
                                ex.  "text"

        Returns:
                Integer value of the count of total adjectives in list
        """
        adjectiveCount = 0
        totalAdjectiveCount = 0
        findAdjective = re.compile("\'JJ\w?\'")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findAdjective.search(str(y)) is not None:
                    adjectiveCount += 1
            print "\nScanning..." + str(x)
            print "\tAdjectives found: " + str(adjectiveCount)  # TODO instead of printing here, call function to add to 2D array
            totalAdjectiveCount += adjectiveCount
            adjectiveCount = 0
        return totalAdjectiveCount

##############################################################################

    def countPronouns( self, aList ):
        """
        Takes a list of strings and returns the count of total pronouns in list.

        Args:
                aList: a list of strings for processing
                                ex.  "text"

        Returns:
                Integer value of the count of total pronouns in list
        """
        pronounCount = 0
        totalPronounCount = 0
        findPronoun = re.compile("[\'PRP\w?\'|\'WP\w?\']")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findPronoun.search(str(y)) is not None:
                    pronounCount += 1
            print "\nScanning..." + str(x)
            print "\tPronouns found: " + str(pronounCount)  # TODO instead of printing here, call function to add to 2D array
            totalPronounCount += pronounCount
            pronounCount = 0
        return totalPronounCount

##############################################################################

    def countAdverbs( self, aList ):
        """
        Takes a list of strings and returns the count of total adverbs in list.

        Args:
                aList: a list of strings for processing
                                ex.  "text"

        Returns:
                Integer value of the count of total adverbs in list
        """
        adverbCount = 0
        totalAdverbCount = 0
        findAdverb = re.compile("\'RB\w?\'")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findAdverb.search(str(y)) is not None:
                    adverbCount += 1
            print "\nScanning..." + str(x)
            print "\tAdverbs found: " + str(adverbCount)  # TODO instead of printing here, call function to add to 2D array
            totalAdverbCount += adverbCount
            adverbCount = 0
        return totalAdverbCount

##############################################################################

    def countOther( self, aList ):
        """
        Takes a list of strings and returns the count of total non-verb, non-noun, non-adv, non-adj,
                                and non-pronouns in list.

        Args:
                aList: a list of strings for processing
                                ex.  "text"

        Returns:
                Integer value of the count of total non-verb, non-noun, non-adv, non-adj, and
                                non-pronouns in list.
        """
        otherCount = 0
        totalOtherCount = 0
        findOther = re.compile("[\'$\'|\'\"\'|\'(\'|\')\'|\',\'|\'--\'|\'.\'|\'CC\'|\'CD\'|\'DT\'|\'EX\'|\'FW\'|\'IN\'|\'LS\'|\'MD\'|\'PDT\'|\'POS\'|\'RP\'|\'SYM\'|\'TO\'|\'UH\'|\'WDT\'|\'WRB\']")
        for x in aList:
            for y in x:
                #print "Scanning..." + str(y)
                if findOther.search(str(y)) is not None:
                    otherCount += 1
            print "\nScanning..." + str(x)
            print "\tOthers found: " + str(otherCount)  # TODO instead of printing here, call function to add to 2D array
            totalOtherCount += otherCount
            otherCount = 0
        return totalOtherCount

##############################################################################

    def phraseChunker(self, aList, pattern):
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
        result = []
        for s in aList:
            pos = nltk.pos_tag(s)
            NPChunker = nltk.RegexpParser(pattern)
            result.append(NPChunker.parse(pos))
        return result

#            regex pattern to define noun phrase
#            pattern = """
#                NP: {<DT|PP\$>?(<JJ>|<JJR>|<JJS>)*(<NN>|<NNP>|<NNPS>|<NNS>|<POS>)+}
#                    {<NNP>+}
#                    {<NN>+}
#                    {<PRP>+}
#            """


################################################################################

    def posTagger(self, aList):
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

        notWord = re.compile('^[\.|,|;|\(|\)|\[|\]]$')
        wordCount = 0
        for block in aList:
            text = nltk.word_tokenize(block)
            for word in text:
                if notWord.search( str(word) ) is None:
                    wordCount += 1

        return wordCount

##############################################################################

#['block','text','tag', 'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount']

    def updateArray (self, aList, blockNum, attrib, value):
        """
        Updates value in 2D array based on input parameters.

        Args:
                aList: the 2D array to be updated

                blockNum: the block number to be updated.  Valid values are:
                        'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount', 'totalWordCount', 'distinctWordCount'

                attrib: the attribute of the block to be updated

                value: the number or count value

        Returns:
                The updated 2D array, aList
        """
        for case in Switch(attrib):
                if case('nounCount'):
                        colNum = 3
                        print "I should be updating ["+str(blockNum)+"]["+str(colNum)+"] with " + str(value)
                        break
                if case('verbCount'):
                        colNum = 4
                        break
                if case('pronounCount'):
                        colNum = 5              
                        break
                if case('adjCount'):
                        colNum = 6
                        break
                if case('adverbCount'):
                        colNum = 7
                        break
                if case('otherCount'):
                        colNum = 8
                        break
                if case('totalWordCount'):
                        colNum = 9
                        break
                if case('distinctWordCount'):
                        colNum = 10
                        break
                if case():
                        raise Exception("Invalid attrib parameter")
        aList[blockNum][colNum] = value
        return aList
