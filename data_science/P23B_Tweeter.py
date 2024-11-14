# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:21:21 2018

@author: riemannruiz
"""

import pandas as pd
import numpy as np
import tweepy
from datetime import datetime

#%% Codigos de autorizacion
consumer_key = '72ikfcjMJtGOsLEultRcpk2BJ'
consumer_secret = 'twspOaozH18gkp1oAHXs0FUPylPsJr5yzhX7Kgm7T21CWSMtFd'
access_token = '75700298-UMGaPUvjnPxAPJvXYIjblkgUaeCW52Wa9RUOApbi2'
access_token_secret = 'ZXgw0gJF3GlLhMc7hbsSA7qp9ie4DUlvCRKdz65IEvU7C'

#%% Abrir conexion con la API de tweeter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


#%% Descargar los tweets de la persona de interes
user = '@Buffett_es'
new_tweets = api.user_timeline(screen_name=user,count=200)


#%% Darle formato a los 200 tweets
out_t = [[tweet.id_str,tweet.created_at,tweet.text] for tweet in new_tweets]
pd_tweets = pd.DataFrame(out_t)

#%% Trending topics
tweets_trend = api.trends_place(151582)










