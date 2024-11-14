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

#%% Funcion de descarga de tweets
def obtener_tweets(guy,tweet_max):
    new_tweets = api.user_timeline(screen_name=guy,count=200)
    alltweets = []
    alltweets.extend(new_tweets)
    n_alltwets = len(new_tweets)
    n_alltwets_old = 0
    oldest_tweet = alltweets[-1].id-1
    while (n_alltwets<tweet_max and n_alltwets>n_alltwets_old):
        n_alltwets_old=n_alltwets
        new_tweets = api.user_timeline(screen_name=guy,
                                       count=200,
                                       max_id=oldest_tweet)
        alltweets.extend(new_tweets)
        n_alltwets = len(alltweets)
        oldest_tweet = alltweets[-1].id-1
        print('... %s tweets downloaded so far'%n_alltwets)
    return alltweets 

#%% Descargar lo tweets de las personas de interes
guy1 = '@realDonaldTrump'
guy2 = '@lopezobrador_'

tweets_guy1 = obtener_tweets(guy1,5000)
tweets_guy2 = obtener_tweets(guy=guy2,tweet_max=5000)
    
#%% Funcion para extraer la informacion importante
def extraer_info(alltweets):
    out = [[tweet.id_str,tweet.created_at,
            tweet.retweet_count,
            tweet.text] for tweet in alltweets]
    pd_tweets = pd.DataFrame(out)
    pd_tweets.columns = ['id_str','created_at',
                         'retweet_count','text']
    return pd_tweets

#%% Extraer información
pd_guy1 = extraer_info(tweets_guy1)
pd_guy2 = extraer_info(tweets_guy2)

#%% Filtrar la informacion (solo 2018)
pd_guy1_2018=pd_guy1[pd_guy1.created_at>
                     datetime.strptime('31-12-2017',
                                       '%d-%m-%Y')]
pd_guy2_2018=pd_guy2[pd_guy2.created_at>
                     datetime.strptime('31-12-2017',
                                       '%d-%m-%Y')]

#%% Importar el archivo del peso_dolar
peso_dollar = pd.read_csv('..\Data\Peso_Dolar_A.csv',
                          header=10)

#%% Convertir la columne FECHA a formato fecha
def convertir_fecha(x):
    return datetime.strptime(x,'%m/%d/%Y')

peso_dollar.FECHA=peso_dollar.FECHA.apply(convertir_fecha)

#%% Filtrar peso dollar en 2018
peso_dollar_2018 = peso_dollar[peso_dollar.FECHA>
                               datetime.strptime('31-12-2017',
                                       '%d-%m-%Y')]


#%% Visualizar los resultados
import matplotlib.pyplot as plt
fig = plt.figure(figsize =(8,8))
plt.subplot(3,1,1)
plt.plot(pd_guy1_2018.created_at,pd_guy1_2018.retweet_count)
plt.ylabel(guy1)
plt.xticks(rotation=45)
plt.grid()

plt.subplot(3,1,2)
plt.plot(peso_dollar_2018.FECHA,peso_dollar_2018.DATO)
plt.ylabel('Peso-Dollar')
plt.xticks(rotation=45)
plt.grid()

plt.subplot(3,1,3)
plt.plot(pd_guy2_2018.created_at,pd_guy2_2018.retweet_count)
plt.ylabel(guy2)
plt.xticks(rotation=45)
plt.grid()
fig.savefig('result.png')
plt.show()











