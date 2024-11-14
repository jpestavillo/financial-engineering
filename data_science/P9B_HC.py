# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:39:20 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc

#%% Generar los datos para clasificar
np.random.seed(1000)
a = np.random.multivariate_normal([10,0],[[3,0],[0,3]],size=[100])
b = np.random.multivariate_normal([0,20],[[3,0],[0,3]],size=[100])
c = np.random.multivariate_normal([20,20],[[3,0],[0,3]],size=[100])

X = np.concatenate((a,b,c),)
plt.scatter(X[:,0],X[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#%% Aplicar clusterig jerarquico a los datos X
Z = hierarchy.linkage(X,metric='euclidean',method='complete')

plt.figure(figsize=(25,15))
plt.title('Dendrograma Completo')
plt.xlabel('Indice de la muestra')
plt.ylabel('Distancia o similaridad')
dn = hierarchy.dendrogram(Z)
plt.show()

#%% Mostrar un conjunto formado en el clustering
idx = [161,132,153]
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.scatter(X[idx,0],X[idx,1],c='r')
plt.show()

#%% Modificar el aspecto del dendrograma
#plt.figure(figsize=(25,15))
plt.figure()
plt.title('Dendrograma Truncado')
plt.xlabel('Indice de la muestra')
plt.ylabel('Distancia o similaridad')
#dn = hierarchy.dendrogram(Z,
#                          truncate_mode='lastp',
#                          p=12)
dn = hierarchy.dendrogram(Z,
                          truncate_mode='level',
                          p=3)
plt.show()
#%% Criterio del codo (1er criterio)
last = Z[-15:,2]
last_rev=last[::-1]
idxs = np.arange(1,len(last_rev)+1)
plt.plot(idxs,last_rev)
plt.show()
#%%
# Criterio del gradiente (2do criterio)
gradiente = np.diff(last)
grad_rev = gradiente[::-1]
plt.plot(idxs[1:],grad_rev)
plt.xlabel('Num de Grupos')
plt.ylabel('Gradiente distancia')
plt.show()

#%% Seleccion de los grupos por numero de grupos
gruposmax = 3
grupos = hierarchy.fcluster(Z,gruposmax,criterion='maxclust')

plt.figure()
plt.scatter(X[:,0],X[:,1],c=grupos,cmap=plt.cm.prism)
plt.show()

#%% Seleccion de los grupos por ditancia maxima
distmax = 5
grupos = hierarchy.fcluster(Z,distmax,criterion='distance')

plt.figure()
plt.scatter(X[:,0],X[:,1],c=grupos,cmap=plt.cm.prism)
plt.show()

#%% Filtrar o tomar los datos que pertenezcan a un grupo
idx = grupos==15
subdata = X[idx,:]











