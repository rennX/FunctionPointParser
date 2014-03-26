#! /usr/bin/env/ python

import nltk
import re
from FileIo import *

def wordCount( aList ):
    """
    Takes a list of strings and returns the count of total words in list.

    Args:
            aList: a list of strings for processing
                            ex.  ['text1','text2',...]

    Returns:
            Integer value of the count of total words in list
    """
    return len( aList )


def main ():
    """
    Main method to test functions

    """
    fio = FileIo("../input2.txt")
    text = fio.getInput()
    p = re.compile(r'#?\d[\s\.]?[\s]?')
    out = filter(None, p.split(text))
    #print out[2]
    #print len(out)
    wc = 0

    for s in out:
        text = nltk.word_tokenize(s)
        wc += wordCount( text )
    print wc


if __name__ == '__main__':
    main()
