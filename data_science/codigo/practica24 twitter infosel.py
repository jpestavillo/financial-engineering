import pandas as pd 
from datetime import datetime
import tweepy
import matplotlib.pyplot as plt

#%% codigos de autorización 

#data=pd.read_excel('../data/ecobus16-607.xls')

Consumer_Key= '72ikfcjMJtGOsLEultRcpk2BJ'
Consumer_Secret = 'twspOaozH18gkp1oAHXs0FUPylPsJr5yzhX7Kgm7T21CWSMtFd'
Access_Token= '75700298-dpBbEGXECpRj7ZEvp82toe7gGwdt00HdnV8jPHCSl'
Access_Token_Secret= 'XBOwRe1qTxRRm7gf3V80qkShcCtUDuiFbtJnpbj4JrpsM'
#%%abrir la coneccion
auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(auth)
#%% informacion
def obtener_tweets(guy,tweet_max):
    new_tweets=api.user_timeline(screen_name=guy)
    alltweets=[]
    alltweets.extend(new_tweets)
    n_alltweets=len(new_tweets)
    n_alltweets_old=0
    oldest_tweet=alltweets[-1].id-1
    while (n_alltweets<tweet_max and n_alltweets<n_alltweets_old ):
        n_alltweets_old=n_alltweets
        new_tweets=api.user_timneline(screen_name=guy,count=200,max_id=oldest_tweet)
        alltweets.extend(new_tweets)
        n_alltweets=len(alltweets)
        oldest_tweet=alltweets[-1].id-1
        print('...%s tweets downloaded so far' %n_alltweets)
    return alltweets
#%% descargar los tweets de las personas de interes
guy1='@realDonaldTrump'
guy2='@Lopezobrador'

tweets_guy1=obtener_tweets(guy=guy1,tweet_max=5000)
tweets_guy2=obtener_tweets(guy=guy2,tweet_max=5000)
#%%% extraer la informacion importante
def extraer_info(alltweets):
    out=[[tweet.id_str,tweet.created_at,tweet.retweet_count,tweet.text] for tweet in alltweets]
    pd_tweets=pd.DataFrame(out)
    pd_tweets.columns=['id_str','created_at','retweet_count','text']
    return pd_tweets
#%%
pd_guy1=extraer_info(tweets_guy1)
pd_guy2=extraer_info(tweets_guy2)
#%% filtrar la informacion solo 2018
pd_guy1_2018= pd_guy1[pd_guy1.create_at>datetime.strptime('31-12-2017','%d-%m-%y')]
pd_guy2_2018= pd_guy1[pd_guy2.create_at>datetime.strptime('31-12-2017','%d-%m-%y')]
#%% imrpotar el archivo del peso dolar 
peso_dollar=pd.read_csv('../data/ecobus16-607.csv',header=10)
#%% 
#01-03-2018 == %d-%m-%Y
#   Mar-18  == %M-%y
def convertir_fecha(x):
    return datetime.strptime(x,'%m/%d/%Y')
peso_dollar.FECHA=peso_dollar.FECHA.apply(convertir_fecha)
#%% filtrar peso dollar en 2018
dollar_2018=peso_dollar[peso_dollar.FECHA>datetime.strptime('31-12-2017','%d-%m-%Y')]
#%% visualizar los resultados
fig=plt.figure(figsize=(8,8))
plt.subplot(3,1,1)
plt.plot(pd_guy1_2018.created_at,pd_guy1_2018.retweet)
plt.ylabel(guy1)
plt.grid()

plt.subplot(3,1,2)
plt.plot(peso_dollar_2018.FECHA,peso_dollar_2018.DATO)
plt.ylabel('Peso-dollar')
plt.grid()

plt.subplot(3,1,3)
plt.plot(pd_guy2_2018.created_at,pd_guy2_2018.retweet)
plt.ylabel(guy2)
plt.grid()
plt.show()
#%%
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

