# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:31:53 2018

@author: if709274
"""

import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
import pandas_datareader.data as web

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import datetime

#%%
start= datetime(2017,9,24)
end=datetime(2018,9,24)
data=web.YahooDailyReader(symbols='ALFAA.MX',start=start,end=end,interval='d').read()


#%%
plt.plot(data['Close'])
plt.show()

#%%
dat=data['Adj Close']
n=5
n_prices= len(dat)
dat_new=np.zeros((n_prices-n,n))
for k in np.arange(n):
    dat_new[:,k]=dat[k:(n_prices-n)+k]
    
#%%
plt.plot(dat_new.transpose())
plt.xlabel('time')
plt.ylabel('price')
plt.plot()
#%%
tmp=dat_new.transpose()
tmp=(tmp-tmp.mean(axis=0))/tmp.std(axis=0)
dat_new=tmp.transpose()
#%% clustering using Kmeans
num_grupos=np.arange(1,16)
inercias=np.zeros(15)
for k in num_grupos:
    model=KMeans(n_clusters=k,init='random')
    model=model.fit(dat_new)
    inercias[k-1]=model.inertia_
#exec('cadena de codigo')

#%% decidir basados en la grafica de codo
plt.plot(num_grupos,inercias)
plt.xlabel('Num_grupos')
plt.ylabel('Incercia')
plt.show()
        #%%)
model=KMeans(n_clusters=4,init='random')
model=model.fit(dat_new)
grupos=model.predict(dat_new)
centroides=model.cluster_centers_


plt.plot(centroides.transpose())
plt.show()

#%% interpretar la agrupacion en funcion del timepo
plt.subplot(211)
plt.plot(dat)
plt.xlabel('time')
plt.ylabel('precio')
plt.subplot(212)
plt.bar(np.arange(n,len(dat)),grupos)
plt.xlabel('time')
plt.ylabel('grupos')
plt.show()
#%% graficar los grupos separado con su respectiva etiqueta
n_subfig=np.ceil(np.sqrt(len(np.unique(grupos))))
plt.figure(figsize=(10,15))
for k in np.arange(len(np.unique(grupos)))+1:
    plt.subplot(n_subfig,n_subfig,k)
    plt.plot(centroides[k-1,:])
    plt.ylabel('cluster %d'%k)
plt.show()
#%%
nclust= grupos[-1]
pos=np.arange(n,len(dat))[grupos==nclust]
plt.figure(figsize=(8,8))
plt.plot(dat,'b-')
for k in pos:
    plt.plot(np.arange(k-n,k),np.array(dat[k-n:k]),'r-')
plt.xlabel('time')
plt.ylabel('precio')
plt.show()

