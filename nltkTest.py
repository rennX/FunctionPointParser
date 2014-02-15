#! /usr/bin/env python
import re
import nltk

text = """#1The system shall allow users to login to their accounts. [[ILF]]
#2. The system shall maintain  permissions for what actions a user is permitted to perform. [[ILF]]
#3.The system shall maintain customized pages based on the user's role. [[ILF]]
#4 The system shall display a list of all events associated with the attraction's page if the user is an administrator, booking agent, business user, financial user, or the attration's manager agent.  [[EIF]]
5. The system shall display all the events scheduled at a venue on the venue's page if the user is an administrator, booking agent, business user, or financial user. [[EIF]]
#6. The system shall provide the ability to search the directory for an individual by phone number. [[EO]]"""
p = re.compile(r'#?\d[\s\.]?[\s]?')
out = filter(None, p.split(text))
i=0
for s in out:
	print 
	i += 1
	text = nltk.word_tokenize(s)
	pos = nltk.pos_tag(text)
	pattern = "NP: {<DT>?<JJ>*<NN>}"
	NPChunker = nltk.RegexpParser(pattern)
	result = NPChunker.parse(pos)  
	print "Chunked POS TAG:::Block " + str(i)
	print result
	

#print "\n".join(out)


