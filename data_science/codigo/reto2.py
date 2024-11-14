# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:19:02 2018

@author: juanp
"""

import pandas as pd
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from  scipy.cluster import hierarchy
from sklearn.cluster import KMeans
from sklearn.metrics import (accuracy_score,precision_score,recall_score)
#%%
#data=pd.read_csv('../data/dataset_reto_digit.csv',index_col='Index')
datapng=genfromtxt('../data/dataset_reto_digit.csv',delimiter=',')
realdigits=datapng[1:,-1]
datapng=datapng[1:,1:]
plt.imshow(datapng)
plt.show()



#%%
#for contador in range(360):
 #   prim_reng=np.zeros((8,8))
  #  for i in range (1,8):
   #     for j in range (1,8):
    
#        prim_reng[i,j]=datapng[contador,j+(8*i)]
 #   plt.imshow(prim_reng)
  #  plt.show()

#%% aqui podemos ver que solo son 2 grupos 
data=pd.read_csv('../data/dataset_reto_digit.csv',index_col='Index')
data=(data-data.mean(axis=0))/data.std(axis=0)
data=data.dropna(axis='columns')
Z= hierarchy.linkage(data,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
#%%
model=KMeans(n_clusters=2,init='random')
model=model.fit(data)
Ypredict=pd.DataFrame(model.predict(data))
#%%
Y=datapng[:,-1]
Y=pd.DataFrame(Y)
Ypredict=pd.DataFrame(Ypredict)
modelo= Ypredict==Y
porcentaje=np.sum(modelo)
porcentaje=porcentaje/360


