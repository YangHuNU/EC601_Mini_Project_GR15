#!/usr/bin/env python
# encoding: utf-8
#Author - Yang Hu & Jinyu Tian

import tweepy #Installed on premises
import json


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
        new_tweets = api.search(q = keyword,count = 10,max_id = str(oldest))
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest
        oldest = new_tweets[-1].id-1
        if(not new_tweets):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ("Done")
    file.close()

if __name__ == '__main__':
    #get keyword from search the '#' is added in front of the word for hashtag
    get_all_tweets("#Juul")