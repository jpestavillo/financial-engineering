# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:34:36 2018

@author: juanp
"""
import pandas as pd
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
from sklearn.cluster import KMeans
import numpy as np
import scipy.optimize as opt
#%%
data1=pd.read_csv('../data/dataset_1.csv')
data2=pd.read_csv('../data/dataset_2.csv')
data3=pd.read_csv('../data/dataset_4.csv')

#%%
data_norm=(data1-data1.mean())/data1.std()
data=data_norm
data1=data
#%%
Z= hierarchy.linkage(data1,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
#%% decidiendo el numero en el cluster

inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init = 'random')
    model = model.fit(data_norm)
    inercias[k-1] = model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.title('KMeans')
plt.xlabel('Num de grupos')
plt.ylabel('Inercia global')
plt.show()
#%%
model=KMeans(n_clusters=5,init='random')
model=model.fit(data)
Ypredict=pd.DataFrame(model.predict(data))



#%% ahora con maquina vector soporte 

