#! /usr/bin/env python

"""This is the main method for the FPP project. It calls all methods necessary to 
process input text into three csv files containing the required data. """

from FileIo import *
from InputProcessor import *
from BlockProcessor import *
from Switch import *
import sys, os
import nltk
import zipfile


if __name__ == "__main__":

    ##############################################################################

    # initialize variables
    input = "../input.txt"
    fio = FileIo(input)
    ip = InputProcessor()
    bp = BlockProcessor()

    # initial setup, process input, tokenize, find parts of speech
    the2DArray = ip.processInput(fio.getFile())
    the2DArray = bp.removeCommas(the2DArray)
    tokenized = ip.tokenize(the2DArray)
    pos = bp.posTagger(the2DArray)


    ##############################################################################

    # noun and verb phrase chunking
    chunkPattern = """
            NP: {<DT|PP\$>?<CD>?(<JJ>|<JJR>|<JJS>)*(<NN>|<NNP>|<NNPS>|<NNS>|<POS>)+}
            {<NNP>+}
            {<NN>+}
            {<PRP>+}
            {<DT><JJ>}
            
            VP: {<MD|TO|RB>?<VB.*>+<RB>?<VB.*>?}
            {<VB.*>+}
            """
    phraseChunk = bp.phraseChunker(tokenized, chunkPattern)
    #for tree in phraseChunk:
    #    print tree

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
    wordCountDict = bp.wordCount(tokenized)
    for key, value in wordCountDict.iteritems() :
        if key is 'total':
            totalWordCount = value
        else:
            the2DArray = bp.updateArray(the2DArray,key,'totalWordCount',value)

    ##############################################################################

    # update the2DArray with totals
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'nounCount',totalNouns)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'verbCount',totalVerbs)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'adjectiveCount',totalAdjectives)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'pronounCount',totalPronouns)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'adverbCount',totalAdverbs)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'otherCount',totalOther)
    the2DArray = bp.updateArray(the2DArray,len(the2DArray)-1,'totalWordCount',totalWordCount)

    ##############################################################################

    # process distinct word count and TF-IDF 
    distinctWordCountArray = bp.distinctWordCount(tokenized)
    tf_idfArray = bp.tf_idf_Count(tokenized)

    ##############################################################################

    # now we have our 3 data structures, lets convert to csv
    outputDirBase = '../output/' 
    numpy.savetxt(outputDirBase + 'the2DArray.csv', the2DArray, delimiter=",", fmt="%s")
    numpy.savetxt(outputDirBase + 'distinctWordCountArray.csv', distinctWordCountArray, delimiter=",", fmt="%s")
    numpy.savetxt(outputDirBase + 'tf_idfArray.csv', tf_idfArray, delimiter=",", fmt="%s")

    #zip up files for output
    count = 1
    baseName = 'teamNLP'
    zipFileName = baseName + '.zip'
    #print zipFileName + ' ' + str(os.path.exists(outputDirBase + zipFileName))
    while (os.path.exists(outputDirBase + zipFileName)):
        count += 1
        zipFileName = baseName + str(count) + '.zip'
        #print zipFileName + ' ' + str(os.path.exists(outputDirBase + zipFileName))
    #print 'Creating: ' + zipFileName
    zf = zipfile.ZipFile(outputDirBase + zipFileName, mode='a')
    try:
        for filename in [ 'the2DArray.csv', 'distinctWordCountArray.csv','tf_idfArray.csv' ]:
            #print 'adding '+filename
            zf.write(outputDirBase + filename, arcname=filename)
            os.remove(outputDirBase + filename)
    finally:
        #print 'closing'
        zf.close()
        

