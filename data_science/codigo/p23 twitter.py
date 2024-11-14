# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd 
from datetime import datetime
import tweepy

#%% codigos de autorización 


Consumer_Key= '72ikfcjMJtGOsLEultRcpk2BJ'
Consumer_Secret = 'twspOaozH18gkp1oAHXs0FUPylPsJr5yzhX7Kgm7T21CWSMtFd'
Access_Token= '75700298-dpBbEGXECpRj7ZEvp82toe7gGwdt00HdnV8jPHCSl'
Access_Token_Secret= 'XBOwRe1qTxRRm7gf3V80qkShcCtUDuiFbtJnpbj4JrpsM'
#%%abrir la coneccion
auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(auth)
#%% informacion
p='@MichelleMRmz'
new_tweets=api.user_timeline(screen_name=p,count=200)

#%%
out_tweets=[[tweet.id_str,tweet.created_at,tweet.text]for tweet in new_tweets]
pd_tweets=pd.DataFrame(out_tweets)
pd_tweets.columns=['id_str','created_at','text']

#@MichelleMRmz 
#new_tweets[0]._json
#%%
mentions_tweets=api.search(q=p,count=100)
out_tweets=[[tweet.id_str,tweet.in_reply_to_status_id,tweet.user.screen_name,tweet.in_reply_to_screen_name,tweet.in_reply_to_user_id,tweet.retweet_count,
             tweet.created_at,tweet.text]for tweet in mentions_tweets]
pd_mentions=pd.DataFrame(out_tweets)

#%% descargar mas de 200 tweets
alltweets=[]
alltweets.extend(new_tweets)

n_alltweets=len(alltweets)
n_alltweets_old=0
max_tweets=1000

oldesttweet=alltweets[-1].id-1

while(len(alltweets)<max_tweets and n_alltweets_old < n_alltweets):
    print('getting tweets before %s' %oldesttweet )
    n_alltweets_old=n_alltweets
    
    new_tweets=api.user_timeline(screen_name=p,count=200,max_id=oldesttweet)
    
    alltweets.extend(new_tweets)
    n_alltweets=len(alltweets)
    
    oldesttweet=alltweets[-1].id-1
    print('...%s tweets downloades so far' %n_alltweets)
#%%
out_tweets=[[tweet.id_str,tweet.created_at,tweet.text]for tweet in alltweets]
all_tweets=pd.DataFrame(out_tweets)
pd_tweets.columns=['id_str','created_at','text']
#%% where on earth identifiers 
#http://www.woeidlookup.com/
tweets_trend=api.trends_place(23424900)
trends=set([trend['name']for trend in tweets_trend[0]['trends']])
print(trends)

#%% trending topics
#tweets_trend=api.trends_place 