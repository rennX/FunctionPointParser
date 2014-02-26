#!/usr/bin/python

import nltk
import re

def distinctWords( aList )
	"""
	Takes a list of strings and returns the count of total distinct words in list.
		
	Args:
		aList: a list of strings for processing
				ex.  ['text1','text2',...]

	Returns:
		Integer value of the count of total distinct words in list
	"""
  	print len(set(aList))

def main ():
	"""
	Main method to test functions

	"""
	text = """##1Business requirements are what must be delivered to provide value. Products, systems, software, and processes are the ways how to deliver, satisfy, or meet the business requirements whats. Consequently, the topic of business requirements often arises in the context of developing or procuring software or other system; but business requirements exist much more broadly. That is, 'business' can be at work or personal, for profit or non-profit.[[EO,EI]]
	##2 Confusion arises for three main reasons. (1) A common practice is to refer to objectives, or expected benefits, as 'business requirements.' (2) People commonly use the term 'requirements' to pertain to the features of the product, system, software expected to be created. (3) A widely-held model says these two types of requirements differ only in level of detail or abstraction—wherein 'business requirements' are high-level and vague and decompose into product, system, or software requirements that are detailed.[[EI]]
	##3.Such confusion can be avoided by recognizing that business requirements are not objectives but rather meet objectives (i.e., provide value) when satisfied. Business requirements whats do not decompose into product/system/software requirements hows. Rather, products and their requirements represent a response to business requirements—a way how presumably to satisfy the whats. Business requirements exist within the business environment and must be discovered, whereas product requirements are human-defined (specified). Business requirements are not just high-level but need to be driven down to detail. No matter how far down in detail they are driven, business requirements are always business deliverable whats that provide value when satisfied; driving them down to detail never turns business requirements into product requirements.[1][[IEF]]
	##4. In system or software development projects, business requirements usually requires authority from stakeholders. This typically leads to the creation or updating of a product, system, or piece of software. The product/system/software requirements usually consist of both functional requirements and non-functional requirements. Although typically defined in conjunction with the product/system/software functionality (features and usage), non-functional requirements often actually reflect a form of business requirements which sometimes are considered constraints, such as necessary performance, security, or safety that apply at the business level.[[EO]]
	##5.Business requirements are often listed in a Business Requirements Document or BRD. The emphasis in a BRD is on what is required, rather than on how to achieve it, which is usually delegated to a Systems Requirements Specification or Document (SRS or SRD) or other variation such as a Functional Specification Document. While supposedly describing the product, system, or software from an external perspective, such documents often define the product/system/software requirements in the context of a chosen technology (a solution approach or architecture). Further confusion often arises when people writing BRDs do not understand the distinctions; and consequently many BRDs actually describe requirements of a product, system, or software.[[EO,EI]]"""

	p = re.compile(r'#?\d[\s\.]?[\s]?')
	out = filter(None, p.split(text))
	#print out[2]
	#print len(out)
	i = 0

	for s in out:
		i += 1
		text = nltk.word_tokenize(s)
		
	distinctWords( text )


if __name__ == '__main__':
	main()
