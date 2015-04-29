#!/usr/bin/env python

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.metrics import precision_score, recall_score
from collections import Counter


############## load data
with open('data/eng.txt') as ef:
    eng = np.array( ef.read().splitlines() )
with open('data/kor.txt') as kf:
	kor = np.array( kf.read().splitlines() )
with open('data/features.txt') as ff:
	feats = ff.read().splitlines()


############## labels
y = np.array( [0 for e in eng] + [1 for k in kor] )


############## generate features

# s: sentence; f: list of features
def get_features(sentence, features):
	feature_counter = Counter()
	for f in features:
		div = len([ sentence[i:i+len(f)] for i in range(len(sentence)-len(f)+1) if ' ' not in sentence[i:i+len(f)] ])
		feature_counter[f] = sentence.count(f)*1.0 / div
	return feature_counter

data_dict = dict()
for e in eng:
	data_dict[e] = get_features(e, feats)
for k in kor:
	data_dict[k] = get_features(k, feats)

X = np.array( [ [data_dict[e][f] for f in feats] for e in eng ]
	+ [ [data_dict[k][f] for f in feats] for k in kor ] )

n = int(len(X)*0.6)
shuffled_indices = np.random.permutation(range(len(X)))
train, test = shuffled_indices[:n], shuffled_indices[n:]

X_train, y_train = X[train,:], y[train]
X_test, y_test = X[test,:], y[test]

print X_train

############### train classifier - Logistic Ridge Regression

model = LogisticRegression(penalty='l2')

model.fit(X_train,y_train)

predictions = model.predict(X_test)


print 'Accuracy: ', model.score(X_test, y_test)
print 'Precision: ', precision_score(y_test, predictions)
print 'Recall: ', recall_score(y_test, predictions)
