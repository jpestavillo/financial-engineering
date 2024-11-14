# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:12:34 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc

#%% Generar datos para el clustering
np.random.seed(4711)
a = np.random.multivariate_normal([10,0],[[3,0],[0,3]],size=[100])
b = np.random.multivariate_normal([0,20],[[3,0],[0,3]],size=[100])
c = np.random.multivariate_normal([3,7],[[3,0],[0,3]],size=[100])

X = np.concatenate((a,b,c),)

plt.scatter(X[:,0],X[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.grid()
plt.show()

#%% Aplicar el algoritmo de clustering
Z = hierarchy.linkage(X,metric='euclidean',method='complete')

plt.figure(figsize=(25,15))
plt.title('Dendrograma completo')
plt.xlabel('Indice de la muestra')
plt.ylabel('Distancia o Similitud')
dn = hierarchy.dendrogram(Z)
plt.show()

#%% Modificacion de la visualizacion del dendrograma
plt.figure(figsize=(25,15))
plt.title('Dendrograma completo')
plt.xlabel('Indice de la muestra')
plt.ylabel('Distancia o Similitud')
#dn = hierarchy.dendrogram(Z,
#                          truncate_mode='lastp',
#                          p=12)
dn = hierarchy.dendrogram(Z,
                          truncate_mode='level',
                          p=5)
plt.show()

#%% Criterios de seleccion de grupos
# Primer criterio: grafica de codo
last = Z[-15:,2]
last_rev = last[::-1]
idx = np.arange(1,len(last_rev)+1)

plt.plot(idx,last_rev)
plt.xlabel('Num grupos')
plt.ylabel('Distancia o similaridad')
plt.grid()
plt.show()

# Segundo criterio: Gradiente
grad = np.diff(last)
grad_rev = grad[::-1]
plt.plot(idx[1:],grad_rev)
plt.xlabel('Num grupos')
plt.ylabel('Diferencia Distancia o similaridad')
plt.grid()
plt.show()

#%% Seleccionar los datos que pertenecen a cada grupo
gruposmax = 4
grupos = hierarchy.fcluster(Z,gruposmax,criterion='maxclust')

plt.scatter(X[:,0],X[:,1],c=grupos)
plt.axis('square')
plt.show()

#%% partir en grupos de maxima distancia
distmax = 8
grupos = hierarchy.fcluster(Z,distmax,criterion='distance')

plt.scatter(X[:,0],X[:,1],c=grupos)
plt.axis('square')
plt.show()











