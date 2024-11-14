# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:34:04 2018

@author: riemannruiz
"""

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cluster import KMeans

#%% Descargar los datos de la serie de tiempo
start = datetime(2017,9,25)
end = datetime(2018,9,25)
data = web.YahooDailyReader(symbols='MSFT',start=start,end=end,interval='d').read()
#data = web.DataReader(symbols='MSFT',start=start,end=end)

#%%
plt.plot(data['Close'])
plt.show()

#%% Descomponer la serie original en subseries de longitud nv
dat = data['Close']
nv = 5
n_prices = len(dat)
dat_new = np.zeros((n_prices-nv,nv))
for k in np.arange(nv):
    dat_new[:,k] = dat[k:(n_prices-nv)+k]

#%%
plt.plot(dat_new.transpose())
plt.xlabel('time')
plt.ylabel('prices')
plt.show()

#%% Normalizar los datos por filas
tmp = dat_new.transpose()
tmp = (tmp-tmp.mean(axis=0))/tmp.std(axis=0)
dat_new = tmp.transpose()




#%% Buscar el numero de grupos segun la gráfica de codo
n_clusters = np.arange(1,16)
inercias = np.zeros(15)
for k in n_clusters:
    model = KMeans(n_clusters=k,init='random').fit(dat_new)
    inercias[k-1] = model.inertia_

#%% Dibujar la gráfica de codo
plt.plot(n_clusters,inercias)
plt.xlabel('Num grupos')
plt.ylabel('Inercia')
plt.show()

#%% Aplicar el clutering con el numero de grupos determinado
model = KMeans(n_clusters=5,init='k-means++').fit(dat_new)
grupos = model.predict(dat_new)
centroides = model.cluster_centers_

plt.plot(centroides.transpose())
plt.show()


#%% Dibujar todos los centroides con su respectiva etiqueta
n_subfig = np.ceil(np.sqrt(len(np.unique(grupos))))
for k in np.unique(grupos):
    plt.subplot(n_subfig,n_subfig,k+1)
    plt.plot(centroides[k,:])
    plt.ylabel('Grupo %d'%k)
plt.show()

#%% Comparar la generación de los grupos con la serie original
plt.subplot(211)
plt.plot(dat)
plt.xlabel('time')
plt.ylabel('price')
plt.subplot(212)
plt.bar(np.arange(nv,len(dat)),grupos)
plt.xlabel('time')
plt.ylabel('grupo')
plt.show()

#%%Colorear la serie de tiempo en funcion de un grupos deseado
pos = np.arange(nv,len(dat))[grupos==3]
plt.plot(np.array(dat),'b-')
for k in pos:
    plt.plot(np.arange(k-nv,k),np.array(dat[k-nv:k]),'r-')
plt.xlabel('time')
plt.ylabel('price')
plt.show()









