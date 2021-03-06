#! /usr/bin/env python

"""This class offers several methods to processes blocks of text using NLTK and other libraries."""

import re
import nltk
import math
import string

from FileIo import *
from InputProcessor import *
from Switch import *
from nltk.corpus import stopwords

class BlockProcessor:

    def __init__(self):
        """Initializes a new empty BlockProcessor object."""
        pass

##############################################################################

    def countNouns( self, aPosList ):
        """
        Takes a list of strings and returns the count of total nouns in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                nounDict:  a dictionary with format <block number>:<number of nouns>, also 'total':<total number of nouns>
        """
        findNoun = re.compile("\'NN\w?\w?\'")
        blockCount = -1
        nounDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading and total
                nounDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findNoun.search(str(y)) is not None:
                        nounDict[blockCount] += 1
                        nounDict['total'] += 1
                    
        return nounDict

##############################################################################

    def countVerbs( self, aPosList ):
        """
        Takes a list of strings and returns the count of total verbs in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                verbDict:  a dictionary with format <block number>:<number of verbs>, also 'total':<total number of verbs>
        """
        findVerb = re.compile("\'VB\w?\'")
        blockCount = -1
        verbDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading and total
                verbDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findVerb.search(str(y)) is not None:
                        verbDict[blockCount] += 1
                        verbDict['total'] += 1

        return verbDict

##############################################################################

    def countAdjectives( self, aPosList ):
        """
        Takes a list of strings and returns the count of total adjectives in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                adjectiveDict:  a dictionary with format <block number>:<number of adjectives>, also 'total':<total number of adjectives>
        """
        findAdjective = re.compile("\'JJ\w?\'")
        blockCount = -1
        adjectiveDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading and total
                adjectiveDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findAdjective.search(str(y)) is not None:
                        adjectiveDict[blockCount] += 1
                        adjectiveDict['total'] += 1
                    
        return adjectiveDict

##############################################################################

    def countPronouns( self, aPosList ):
        """
        Takes a list of strings and returns the count of total pronouns in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                pronounDict:  a dictionary with format <block number>:<number of pronouns>, also 'total':<total number of pronouns>
        """
        findPronoun = re.compile("\'PRP\$?\'|\'WP\$?\'")
        blockCount = -1
        pronounDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading and total
                pronounDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findPronoun.search(str(y)) is not None:
                        pronounDict[blockCount] += 1
                        pronounDict['total'] += 1
                        #print "Found pronoun: " + str(y) + "Block:" +str(pronounDict[blockCount])+ "Total:"+ str(pronounDict['total'])
                    
        return pronounDict

##############################################################################

    def countAdverbs( self, aPosList ):
        """
        Takes a list of strings and returns the count of total adverbs in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                adverbDict:  a dictionary with format <block number>:<number of adverbs>, also 'total':<total number of adverbs>
        """
        findAdverb = re.compile("\'RB\w?\'")
        blockCount = -1
        adverbDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading
                adverbDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findAdverb.search(str(y)) is not None:
                        adverbDict[blockCount] += 1
                        adverbDict['total'] += 1
                    
        return adverbDict

##############################################################################

    def countOther( self, aPosList ):
        """
        Takes a list of strings and returns the count of total other parts of speech in list.

        Args:
                aPosList: a list of pos tagged lists
                                ex. [[('Business', 'NN'), ('requirements', 'NNS')], [('are', 'VBP'), ('what', 'WP')], [('must', 'MD'), ('be', 'VB'),('delivered', 'VBN')]]

        Returns:
                otherDict:  a dictionary with format <block number>:<number of others>, also 'total':<total number of others>
        """
        findOther = re.compile("\'$\'|\'\"\'|\'(\'|\')\'|\',\'|\'--\'|\'CC\'|\'CD\'|\'DT\'|\'EX\'|\'FW\'|\'IN\'|\'LS\'|\'MD\'|\'PDT\'|\'POS\'|\'RP\'|\'SYM\'|\'TO\'|\'UH\'|\'WDT\'|\'WRB\'")
        blockCount = -1
        otherDict = { 'total': int(0) }
        for x in aPosList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aPosList)-1): # skip over heading and total
                otherDict[blockCount] = 0
                for y in x:
                    #print "Scanning..." + str(y)
                    if findOther.search(str(y)) is not None:
                        otherDict[blockCount] += 1
                        otherDict['total'] += 1
                    
        return otherDict

##############################################################################

    def phraseChunker(self, aList, pattern):
        """
        Processes the 2nd column of the 2D array row by row - for each row
        the block is tokenized, tagged, noun phrases are chunked out
        the variable result is a text based representation of a tree w/ 'S' as
        the head

Args:
        aList: a 2DArray of blocks and assoicated values
        pattern: the regex pattern to use for word phrase chunking

Returns:
        A list of lists.  Each list is block of text chunked based on the input pattern
        and formatted into a sentence tree structure.
"""

        i=-1
        result = []
        for s in aList:
            pos = nltk.pos_tag(s)
            NPChunker = nltk.RegexpParser(pattern)
            result.append(NPChunker.parse(pos))
        return result

################################################################################

    def removeCommas(self,aList):
        for block in aList:
            block[1] = block[1].replace(',',"")
            block[1] = block[1].replace('.',"")
            block[2] = str(block[2]).replace(',',"|")
        return aList

################################################################################$
    
    def posTagger(self, aList):
        """
        Processes the2DArray to determine and label the part of speech for each word

        Args:
            aList: a 2DArray of blocks and associated values

        Returns:
            A list of lists.  Each list is a block of text tokenized with parts of speech
        """
        posList = []
        for block in aList:
            text = nltk.word_tokenize(block[1])
            #filtered_words = [w for w in text if not w in ',' and not w in stopwords.words('english')]
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
        isWord = re.compile("\w+\-?\w+")
        blockCount = -1
        wordCountDict = { 'total': int(0) }
        for x in aList:
            blockCount += 1
            if blockCount != 0 and blockCount != (len(aList)-1): # skip over heading and total
                wordCountDict[blockCount] = 0
                for y in x:
                    #print "Scanning..."+str(y)
                    if isWord.search(str(y)) is not None:
                        #print "Found..."+str(y)
                        wordCountDict[blockCount] += 1
                        wordCountDict['total'] += 1
                    
        return wordCountDict

##############################################################################

#['block','text','tag', 'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount']

    def updateArray (self, aList, blockNum, attrib, value):
        """
        Updates value in 2D array based on input parameters.

        Args:
                aList: the 2D array to be updated

                blockNum: the block number to be updated.  Valid values are:
                        'nounCount', 'verbCount', 'pronounCount', 'adjCount', 'adverbCount', 'otherCount', 'totalWordCount'

                attrib: the attribute of the block to be updated

                value: the number or count value

        Returns:
                The updated 2D array, aList
        """
        for case in Switch(attrib):
                if case('nounCount'):
                        colNum = 3
                        break
                if case('verbCount'):
                        colNum = 4
                        break
                if case('pronounCount'):
                        colNum = 5              
                        break
                if case('adjectiveCount'):
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
                if case():
                        raise Exception("Invalid attrib parameter: " + str(attrib))
        aList[blockNum][colNum] = value
        return aList

##############################################################################

    def distinctWordCount(self,tokenized):
        """
        Processes blocks of text to determine distinct words and the frequency with which they occur

        Args:
            tokenized: a list of lists with each list containing tokenized text for one block of input

        Returns:
            wordMat: a 2d array containing distinct words on the y-axis and count per block and in
            total on the x-axis
        """
        # from tokenized blocks of words, create dictionary of distinct words
        wordDict = {}
        numBlocks = -1 # start at -1, we will strip off 0th row
        for block in tokenized:
            numBlocks += 1
            #if numBlocks != 0: # skip over heading
            if numBlocks != 0 and numBlocks != (len(tokenized)-1): # skip over heading and total
                for word in block:
                    if word is not '.':
                        wordDict[word.lower()] = 0

        wordCount = len(wordDict)

        # initialize distinct word array
        wordMat = ["Distinct_Word"]
        for i in range(1,numBlocks+1):
            wordMat=numpy.hstack( (wordMat,["Block_"+str(i)]) )
        wordMat = numpy.hstack ( (wordMat,["Total_Count"]) )

        # add new row to wordMat for each word in wordDict
        totalCount = 0
        for word in wordDict: # for every word in wordDict
            tempList=[word] # start a new tempList
            blockCount = -1 # keep track of block we are parsing
            for block in tokenized: # for every block in the tokenized list
                blockCount += 1
                if blockCount != 0: # skip over heading
                    for w in block: # for every word in the block
                        if w.lower() == word: # if the word matches the wordDict word
                            wordDict[w.lower()] += 1 # increment the word count
                    count = int(wordDict[word])
                    tempList.append(count) # after done with block, append count to tempList
                totalCount += wordDict[word] # increment total count
                wordDict[word] = 0 # reset word count for next block
            tempList.append(int(totalCount)) # after all blocks done, append totalCount to tempList
            totalCount = 0 # reset totalCount for next word in wordDict
            #print tempList
            wordMat = numpy.vstack( (wordMat,tempList) ) # done with that word, append tempList to wordMat

        return wordMat
        
##############################################################################

    def tf_idf_Count(self,tokenized):
        """
        Processes blocks of text to determine term frequency and inverse document frequency data (tf-idf)

        Args:
            tokenized: a list of lists with each list containing tokenized text for one block of input

        Returns:
            wordMat: a 2d array containing distinct words on the y-axis and tf-idf data per block
            on the x-axis
        """
        # from tokenized blocks of words, create dictionary of distinct words
        wordDict = {}
        numBlocks = -1 # start at -1, we will strip off 0th row
        for block in tokenized:
            numBlocks += 1
            #if numBlocks != 0: # skip over heading
            if numBlocks != 0 and numBlocks != (len(tokenized)-1): # skip over heading and total
                for word in block:
                    if word is not '.':
                        wordDict[word.lower()] = 0

        wordCount = len(wordDict)

        # initialize distinct word array
        wordMat = ["Distinct_Word", "IDF"]
        for i in range(1,numBlocks+1):
            wordMat=numpy.hstack( (wordMat,["Block_"+str(i)+"_tf"]) )
            wordMat=numpy.hstack( (wordMat,["Block_"+str(i)+"_tfidf"]) )

        # add new row to wordMat for each word in wordDict
        for word in wordDict: # for every word in wordDict
            timesFound = 0
            tempList=[word,"IDF HERE"] # start a new tempList
            blockCount = -1 # keep track of block we are parsing
            for block in tokenized: # for every block in the tokenized list
                blockCount += 1
                numWords = 0
                if blockCount != 0: # skip over heading
                    for w in block: # for every word in the block
                        numWords += 1
                        if w.lower() == word: # if the word matches the wordDict word
                            wordDict[w.lower()] += 1 # increment the word count
                    count = int(wordDict[word])
                    if count is not 0:
                        timesFound += 1
                    tempList.append( round( (float(wordDict[word]) / float(numWords)),3 ) )
                    tempList.append("tfidf"+str(blockCount))
                wordDict[word] = 0 # reset word count for next block
            invDocFreq = math.log(numBlocks/timesFound)
            tempList[1] = round(invDocFreq,3)
            for i in range(3,(numBlocks*2)+2,2):
                tempList[i] = round((tempList[i-1]*tempList[1]),3)
                
            wordMat = numpy.vstack( (wordMat,tempList) ) # done with that word, append tempList to wordMat

        return wordMat
