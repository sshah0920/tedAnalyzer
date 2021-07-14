# -*- coding: utf-8 -*-
"""
Created on Thurs April 16 01:15:50 2020

@author: Samarth Shah, Bharat Matai
"""

import twitter

#To access the Twitter account, setting the Authorization keys wihtout exposing sensitive data

CONSUMER_KEY = 'xqtuksBxOcL9GL9GvQczclKEm'
CONSUMER_SECRET = '0iNMTxxEXAbbYxvLNTlSJ0mEzlLn1F4eo1DMFLdl6BdYGZLBAB'
OAUTH_TOKEN = '895910040-abmFxim6uEEKSDSZuQbZOa0A8Un4ZowxDMEQgPUZ'
OAUTH_TOKEN_SECRET = 'n45gPqaPB7E6qGSkvjXo6yrkTKniiBW5ug07AVvXrD5Me'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

def searchTweets():
    #The given method below displays 20 tweets which includes #TedTalk.
    count = 20
    search_results = twitter_api.search.tweets(q="#TedTalk", count=count,result_type='mixed')
    statuses = search_results['statuses']
    status_text = [status['text'] for status in statuses]
    for tweet in status_text:
        print("===="*10)
        print('Tweet: ',tweet)
        print("===="*10)
        print()
#%%
