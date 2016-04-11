import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def printScore(tweet):
	affinfile =  open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	res=0

	for line in affinfile:
		term,score = line.split("\t")
		scores[term]=int(score)

	tabtweet=tweet.split()

	pos=0
	neg=0
	computed_sentiment=0

	for t in tabtweet:
		if scores.has_key(t):
			res+=scores[t]
			if scores[t] > 0:
				pos+=1
			elif scores[t] < 0:
				neg+=1

	if (neg==0 or pos==0):
		computed_sentiment=res
	else:
		computed_sentiment=float(pos/neg)


	for t in tabtweet:
		if scores.has_key(t)==0:
			print t+' '+str(computed_sentiment)



def main():


	tweetfile = open(sys.argv[2])


	for line in tweetfile:

	 	tweet = json.loads(line)
	 	if 'text' in tweet.keys():
	 		printScore(tweet['text'])


	


if __name__ == '__main__':
    main()
