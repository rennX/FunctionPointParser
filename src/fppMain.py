#! /usr/bin/env python

"""This is the main method for the FPP project. It calls all methods necessary to 
process input text into three csv files containing the required data. """

from Tkinter import *
from ttk import *
from FileIo import *
from InputProcessor import *
from BlockProcessor import *
from Switch import *
import sys, os
import nltk
import tkFileDialog

class fppMain(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
          
        self.parent = parent
         
        self.initUI()
        
    def initUI(self):
       
        self.parent.title("Function Point Parser")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
 
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        self.instructions_txt = Label(self, text="Each block of text must be denoted by a hash,hash,number sequence:\n\tEx. ##1 Block 1 text ##2 Block 2 text\n\nEach tag must be denoted by left bracket, left bracket, tag(s), right bracket, right bracket sequence:\n\tEx. ##1 Block 1 text [[tag1,tag2]] ##2 Block 2 text [[tag3]]\n\nPaste Text Below:")
        self.instructions_txt.grid(sticky=W, pady=4, padx=5)
         
#         self.heading_txt = Label(self, text="Paste Text Below:")
#         self.heading_txt.grid(sticky=W, pady=4, padx=5)

        self.text_area = Text(self)
        self.text_area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
 
         
        self.submit_btn = Button(self, text="Submit",command=self.writeToFile)
        self.submit_btn.grid(row=1, column=3)
#     
    def writeToFile(self):
        file = open('user_input.txt', 'w')
        file.write(self.text_area.get("1.0",END+"-1c"))
        file.close()

        ##############################################################################

        # initialize variables
        input = "user_input.txt"
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

        # ask user for directory name where the output csv files will be saved to
        dirname = tkFileDialog.askdirectory(initialdir="/",title="Choose Directory Location for Results")
        outputDirBase = dirname + '/'
        
        # csv result files will be located in teamNLP file followed by a number
        # if one or more exist already in the user directory location
        count = 1
        baseName = 'teamNLP'
        outputFileName = outputDirBase + baseName
        while (os.path.exists(outputFileName)): # while the directory name exists
            count += 1 # increment the counter...
            outputFileName = outputDirBase + baseName + str(count) 
        os.mkdir(outputFileName) # create folder in user's chosen directory location
        
        numpy.savetxt(outputFileName + '/the2DArray.csv', the2DArray, delimiter=",", fmt="%s")
        numpy.savetxt(outputFileName + '/distinctWordCountArray.csv', distinctWordCountArray, delimiter=",", fmt="%s")
        numpy.savetxt(outputFileName + '/tf_idfArray.csv', tf_idfArray, delimiter=",", fmt="%s")
            
def main():
    root = Tk()
    root.geometry("750x700+700+700")
    app = fppMain(root)
    root.mainloop()

if __name__ == "__main__":
    main()
