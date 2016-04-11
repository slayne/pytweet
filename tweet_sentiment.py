import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def getScore(tweet):
	affinfile =  open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	res=0

	for line in affinfile:
		term,score = line.split("\t")
		scores[term]=int(score)

	tabtweet=tweet.split()

	for t in tabtweet:
		if scores.has_key(t):
			res+=scores[t]

	return res


def main():


	tweetfile = open(sys.argv[2])


	for line in tweetfile:

	 	tweet = json.loads(line)
	 	if 'text' in tweet.keys():
	 		print getScore(tweet['text'])


	


if __name__ == '__main__':
    main()
