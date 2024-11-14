# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
import scipy.spatial.distance as sc

#%%
np.random.seed(4711)
a= np.random.multivariate_normal([10,0],[[3,1],[1,3]],size=[100])
b= np.random.multivariate_normal([0,20],[[3,0],[0,3]],size=[100])
c= np.random.multivariate_normal([3,7],[[3,0],[0,3]],size=[100])

X=np.concatenate((a,b,c))

plt.scatter(X[:,0],X[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#%% aplicar el algoritmo de clustering
Z= hierarchy.linkage(X,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()

#%% modificacion de la visualizacion del dendograma
Z= hierarchy.linkage(X,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z,
                        truncate_mode='lastp',p=12)
#dn=hierarchy.dendogram(z, truncate_mode='level', p=5)
plt.show()
#%%criterios de seleccion de grupos 
#primer criterio: grafica de codo
last=Z[-15:,2]
last_rev=last[::-1]
idx=np.arange(1,len(last_rev)+1)

plt.plot(idx,last_rev)
plt.xlabel('num grupos')
plt.ylabel('distancia o similaridad')
plt.grid()
plt.show()
# segundo criterio: gradiente
grad= np.diff(last)
grad_rev=grad[::-1]
plt.plot(idx[1:],grad_rev)
plt.xlabel('Num grupos')
plt.ylabel('diferencia distancia o similaridad')
plt.grid()
plt.show()


#%%
gruposmax=4
grupos=hierarchy.fcluster(Z,gruposmax, criterion='maxclust')
plt.scatter(X[:,0],X[:,1],c=grupos)
plt.axis('square')
plt.show()
np.unique(grupos) #hay 18 grupos


#%%
distmax=8
grupos= hierarchy.fcluster(Z,distmax,criterion='distance')
plt.scatter(X[:,0],X[:,1],c=grupos)
plt.axis('square')
plt.show()