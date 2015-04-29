#!/usr/bin/env python

import nltk.data as nd
import string

tokenizer = nd.load('tokenizers/punkt/english.pickle')
with open("data/eng_raw.txt") as fp:
	eng_raw = fp.read()

with open("data/kor_raw.txt") as fp:
	kor_raw = fp.read()

eng_sentences = tokenizer.tokenize(eng_raw) # list
# kor_sentences = tokenizer.tokenize(kor_raw) # doesn't work
kor_sentences = kor_raw.split('.')

# clean punctuation, numbers
exclude = string.punctuation + string.digits # + '“”‘’'
eng_sentences = [ s.translate(None, exclude).lstrip().lower() for s in eng_sentences ]
kor_sentences = [ s.translate(None, exclude).lstrip().lower() for s in kor_sentences ]

# write to file
with open('data/eng.txt', 'w') as e:
	[e.write("%s\n" % s) for s in eng_sentences]

with open('data/kor.txt', 'w') as k:
	[k.write("%s\n" % s) for s in kor_sentences]

