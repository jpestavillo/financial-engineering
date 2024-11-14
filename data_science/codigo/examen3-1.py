# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:37:09 2018

@author: Mario Abel García
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial as sc
import pandas as pd
from sklearn.cluster import KMeans
#%%
data = pd.read_csv('../Data/dataset_1.csv')
#%% normalizar o estandarizar datos
data_norm = (data-data.mean(axis=0))/data.std(axis=0)

#%%
z = hierarchy.linkage(data_norm,metric='euclidean',method='complete')

plt.figure(figsize=(15,5))
plt.title('Dendrograma completo')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn = hierarchy.dendrogram(z)
plt.show()

#%%
last = z[-15:,2]
last_rev = last[::-1] #reordena al reves los valores (todas las filas, t columans,-1 al reves)
idx = np.arange(1,len(last_rev)+1)

plt.plot(idx,last_rev)
plt.title('Gráfica de codo')
plt.xlabel('Num de grupos')
plt.ylabel('Distancia o similaridad')
plt.grid()
plt.show()
#%%
# segundo criterio: grradiente 

grad = np.diff(last)
grad_rev = grad[::-1]
plt.plot(idx[1:],grad_rev)
plt.title('criterio: grradiente ')
plt.xlabel('Num de grupos')
plt.ylabel('Distancia o similaridad')
plt.grid()
plt.show()

#%%
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
