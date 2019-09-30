#!/usr/bin/env python
# encoding: utf-8
#Author - Yang Hu & Jinyu Tian

import tweepy #Installed on premises


#Twitter API credentials
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_key = "access_key"
access_secret = "access_secret"


def get_all_tweets(keyword):
  
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    
    #index for max_id in search
    oldest = -1

    #keep grabbing tweets until it hits 100 count (the result isn't not necessarily 100 tweets)
    while len(alltweets) < 100:
        
        #get new tweets from api search
        new_tweets = api.search(q = keyword,count = 10,max_id = str(oldest),include_entities = False)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest
        oldest = new_tweets[-1].id-1
        if(not new_tweets):
            break
        #print ("...%s tweets downloaded so far" % (len(alltweets)))
    print("%s tweets downloaded in total." % (len(alltweets)))   
    
    x = []
    for i in range(0,20):
    	x.append(str(i)+".txt")
    
    for j in range(0,20):
    	f = open(x[j],"a+")
    	print(alltweets[j].text, "\n", file = f)	#print the first 20 tweets to txt files
    	f.close()
    

if __name__ == '__main__':
    #get keyword from search the '#' is added in front of the word for hashtag
    get_all_tweets("Vape")