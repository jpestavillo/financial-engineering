# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd

#%% Leer datos de las tarjetas de credito
data = pd.read_csv('../Data/creditcard.csv')

#%% Elegir los datos del analisis
clasificacion = data.Class
data = data.drop(['Class','Time'],axis=1)

#%%Aplicar clustering usando KMeans
inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init='random')
    model = model.fit(data)
    inercias[k-1] = model.inertia_

plt.plot(np.arange(1,11),inercias)
plt.xlabel('num grupos')
plt.ylabel('Inercia global')
plt.show()

#%% Suponemos que hay 3 grupos en los datos, ver los perfiles
model = KMeans(n_clusters=3,init='random')
model = model.fit(data)

#%% Ver los resultados
Ypredict = pd.DataFrame(model.predict(data))

datos_grupo0 = data.loc[Ypredict[0]==0]

datos_grupo0.transpose().plot()

#%% Graficar los centroides
centroides = model.cluster_centers_

plt.plot(centroides[:,0:28].transpose())












