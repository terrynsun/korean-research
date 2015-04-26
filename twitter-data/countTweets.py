#!/usr/bin/env python

labeled_tweets =  open('korean_tweets', 'r')
split_tweets = { "0": [], "1":[]}

count = 0
for line in labeled_tweets:
	splitTweet = line.split('\t')
	split_tweets[splitTweet[0]].append(splitTweet[1])
	count+=1

print "Non-Korean Tweets: " + str(len(split_tweets["0"]))
print "Korean Tweets: " + str(len(split_tweets["1"]))