#! /usr/bin/env python

import nltk
import re
from nltk import word_tokenize, wordpunct_tokenize

amend1 = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."
amend2 = "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."
amend3 = "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law."
amend4 = "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."
amend5 = "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation."
amendments = [["Congress shall make no law respecting an establishment of religion or prohibiting the free exercise thereof or abridging the freedom of speech or of the press or the right of the people peaceably to assemble and to petition the Government for a redress of grievances"],["A well regulated Militia being necessary to the security of a free State the right of the people to keep and bear Arms shall not be infringed"],["No Soldier shall in time of peace be quartered in any house without the consent of the Owner nor in time of war but in a manner to be prescribed by law"],["The right of the people to be secure in their persons houses papers and effects against unreasonable searches and seizures shall not be violated and no Warrants shall issue but upon probable cause supported by Oath or affirmation and particularly describing the place to be searched and the persons or things to be seized"],["No person shall be held to answer for a capital or otherwise infamous crime unless on a presentment or indictment of a Grand Jury except in cases arising in the land or naval forces or in the Militia when in actual service in time of War or public danger nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb nor shall be compelled in any criminal case to be a witness against himself nor be deprived of life liberty or property without due process of law nor shall private property be taken for public use without just compensation"]]

#####################################################################
# amendments is list of 5 blocks for processing distinct word count #
#####################################################################

amendmentLists = []
for each in amendments:
	print "\n",each
	tempList = word_tokenize(str(each))
	amendmentLists.append(tempList)

raw_input("\nPress Enter to continue...")
	
newList = []
for each in amendments:
	newList.extend(word_tokenize(str(each)))
	
distinctWords = []
distinctWords = set(newList)
distinctWords2 = []
for each in distinctWords:
	distinctWords2.append(str(each))
	
wordMat = [['theWord', 'block1', 'block2', 'block3', 'block4', 'block5']]
x = 1
wordCount = len(distinctWords2)
blockCount = 5
for each in distinctWords2:
	tempList = [str(each)]
	while x <= blockCount:
		tempList.append(int(0))
		x+= 1
	x = 1
	wordMat.append(tempList)
	
	
################################################################################
# wordMat is initial 2D array full of words and 0 for each block for wordCount #
################################################################################

x = 1
y = 1
wordCount = len(distinctWords2)
totalWords = 0

for block in amendmentLists:
	for word in block:
		while y <= wordCount:
			if word == wordMat[y][0]:
				wordMat[y][x] += 1
				totalWords += 1
				break
			else:
				y += 1
		y = 1
	x += 1
	
for each in wordMat:
	print each
	
print "\nTotal words in wordMat: ", totalWords

totalWords = 0
for each in amendmentLists:
	totalWords += len(each)
print "\nTotal words in amendmentLists: ",totalWords

raw_input("Press Enter to quit...")
