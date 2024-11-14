# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
from datetime import datetime
import tweepy


#%% Códigos de autorización
consumer_key = '72ikfcjMJtGOsLEultRcpk2BJ'
consumer_secret = 'twspOaozH18gkp1oAHXs0FUPylPsJr5yzhX7Kgm7T21CWSMtFd'
access_token = '75700298-dpBbEGXECpRj7ZEvp82toe7gGwdt00HdnV8jPHCSl'
access_token_secret = 'XBOwRe1qTxRRm7gf3V80qkShcCtUDuiFbtJnpbj4JrpsM'

#%% Abrir la conexión a la API de Tweeter

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


#%% Descargar la información de una persona
p = '@realDonaldTrump'
new_tweets = api.user_timeline(screen_name=p,count=200)

#%% Formatear la información en una tabla
out_tweets = [[tweet.id_str,tweet.created_at,tweet.text] for tweet in new_tweets]
pd_tweets = pd.DataFrame(out_tweets)
pd_tweets.columns = ['id_str','created_at','text']

#%% Buscar la menciones de la persona por otros usuarios
mentions_tweets = api.search(q=p,count=100)
out_tweets = [[tweet.id_str,tweet.in_reply_to_status_id,
               tweet.user.screen_name,tweet.in_reply_to_screen_name,
               tweet.in_reply_to_user_id,tweet.retweet_count,
               tweet.created_at,tweet.text] for tweet in mentions_tweets]

pd_mentions = pd.DataFrame(out_tweets)


#%% Descargar más de 200 tweets
alltweets = []
alltweets.extend(new_tweets)

n_alltweets = len(alltweets)
n_alltweets_old = 0
max_tweets = 1000

oldesttweet = alltweets[-1].id-1

while (len(alltweets)<max_tweets and n_alltweets_old<n_alltweets):
    print('Getting tweets before %s' % oldesttweet)
    n_alltweets_old = n_alltweets
    
    new_tweets = api.user_timeline(screen_name=p,count=200,
                                   max_id=oldesttweet)
    alltweets.extend(new_tweets)
    n_alltweets = len(alltweets)
    
    oldesttweet = alltweets[-1].id-1
    
    print('...%s tweets downloaded so far'%n_alltweets)

#%% 
out_tweets = [[tweet.id_str,tweet.created_at,tweet.text] for tweet in alltweets]
pd_tweets = pd.DataFrame(out_tweets)
pd_tweets.columns = ['id_str','created_at','text']


#%% Trending topics
tweets_trend = api.trends_place(23424900)
trends = set([trend['name'] for trend in tweets_trend[0]['trends']])
print(trends)


#%% Trending topics
tweets_trend = api.trends_available()



















