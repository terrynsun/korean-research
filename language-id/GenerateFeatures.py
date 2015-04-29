#!/usr/bin/env python

from collections import Counter
import string

with open('data/kor_pretrain.txt') as fp:
	kor_pretrain = fp.read()

# preprocessing
exclude = string.punctuation + string.digits
kor_pretrain = kor_pretrain.translate(None, exclude)

def get_most_freq_n_letters(n, text=kor_pretrain, k=10):
	# 'lettergrams'
	lg_counter = Counter()
	lgs = [ text[i:i+n] for i in range(len(text)-n+1) if ' ' not in text[i:i+n] ]
	for lg in lgs:
		lg_counter[lg] += 1.0/len(lgs)
	return [j[0] for j in lg_counter.most_common(k)]

features = []
for n in range(2,5):
	features += get_most_freq_n_letters(n)

with open('data/features.txt', 'w') as f:
	[f.write("%s\n" % s) for s in features]

