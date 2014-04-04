#! /usr/bin/env python

"""This class reads in and processes input text from a file"""

class FileIo:
                        

    def __init__(self, file):
        """
        Opens input file for reading. Saves file to 'inputFile'. Then closes the input file.
        
        Args:
            file:  the file to be processed

        Returns:
            none
        """
        self.f = open(file)
        self.inputFile = self.f.read()
        self.f.close()
        
    def toString(self):
        """
        Prints out the contents of the input file as a string
        
        Args:
            none

        Returns:
            none
        """
        print str(self.inputFile)

    def getFile(self):
        """
        Returns the contents of the input file as a string
        
        Args:
            none

        Returns:
            The input file that was processed upon instantiation
        """
        return self.inputFile

