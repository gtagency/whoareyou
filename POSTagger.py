#Thomas Shields - thomas.shields@gatech.edu
#9/30/2014
# 10/7/2014 Edits: reads files from ./texts, prints output in results - Robert Smith smithrobertlawrence@gmail.com

from __future__ import division
from nltk import *
import operator
from os import listdir
from os.path import isfile, join
path = "./data/texts"
raw = "/raw"
onlyfiles = [ f for f in listdir(path+raw) if (isfile(join(path+raw,f)) and f[-4:] == ".txt")]

#runs some nlp on the given file
#returns the average sentence length and a sorted array of
#POS/occurence-percentage pairs.
def process_file(filename):
	contents = "".join([line.decode('utf-8').strip() for line in open(filename).readlines()]).split(".")
	parts = {}
	word_count = 0
	for sentence in contents:
		#this is the actual nltk magic
		words = word_tokenize(sentence)
		word_count += len(words)
		#and here
		poss = pos_tag(words)
		for word, pos in poss:
			c = parts.setdefault(pos, 0) + 1
			parts[pos]= c
	parts = sorted(parts.items(), key=operator.itemgetter(1), reverse=True)
	parts = [(a, round(b / word_count, 2)) for (a,b) in parts]
	sent_avg = word_count / len(contents)
	return (round(sent_avg, 2), parts)

for speech in onlyfiles:
    result = open(path + "/processed/" + speech, 'w+')
    result.write(str(process_file(path + raw + "/" + speech)))
#print process_file("texts/BarrackObama.txt")
#print process_file("RonaldReagan.txt")

# uncomment the below to see the POS codes
# help.upenn_tagset()
