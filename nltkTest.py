#! /usr/bin/env python
import re
import nltk

#text = """#1The system shall allow users to login to their accounts.The Python interpreter changes the prompt from >>> to ... after encountering the colon at the end of the first line. The ... prompt indicates that Python expects an indented code block to appear next. It is up to you to do the indentation, by typing four spaces or hitting the tab key. To finish the indented block just enter a blank line. [[ILF]]
#2. The system shall maintain  permissions for what actions a user is permitted to perform. [[ILF]]
#3.The system shall maintain customized pages based on the user's role. [[ILF]]
#4 The system shall display a list of all events associated with the attraction's page if the user is an administrator, booking agent, business user, financial user, or the attration's manager agent.  [[EIF]]5. The system shall display all the events scheduled at a venue on the venue's page if the user is an administrator, booking agent, business user, or financial user. [[EIF]]
#6. The system shall provide the ability to search the directory for an individual by phone number. [[EO]]"""

text = """#1 one. [[tag]]
#2 two.
#3 three.
#4 four
#5 five."""
p = re.compile(r'#?\d[\s\.]?[\s]?')
out = filter(None, p.split(text))
print out[2]
print len(out)
i=0
for s in out:
	i += 1
	text = nltk.word_tokenize(s)
#	print text
	pos = nltk.pos_tag(text)
#	print pos
	pattern = "NP: {<DT>?<JJ>*<NN>}"
	NPChunker = nltk.RegexpParser(pattern)
	result = NPChunker.parse(pos)  
#	print "Chunked POS TAG:::Block " + str(i)
#	print result
	

#print "\n".join(out)


