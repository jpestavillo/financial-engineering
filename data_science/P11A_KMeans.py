# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:14:24 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#%% Generar los datos para clasificarlos
semilla = 1500
X,Y = make_blobs(n_samples=1000,random_state=semilla)

plt.scatter(X[:,0],X[:,1])
plt.show()

#%% Aplicar el algotimo de KMeans
model = KMeans(n_clusters=5,random_state=semilla,init='random')

model = model.fit(X)
Ypredict = model.predict(X)
centroides = model.cluster_centers_

plt.scatter(X[:,0],X[:,1],c=Ypredict)
plt.plot(centroides[:,0],centroides[:,1],'x')
plt.show()

J = model.inertia_

#%% Criterio de descision el numero de clusters
inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,random_state=semilla,init='random')
    model = model.fit(X)
    inercias[k-1] = model.inertia_

plt.plot(np.arange(1,11),inercias)
plt.xlabel('num grupos')
plt.ylabel('Inercia global')
plt.show()

















