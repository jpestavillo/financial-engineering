# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc
import pandas as pd
from sklearn.cluster import KMeans

#%% Leer los datos
data = pd.read_csv('../Data/creditcard.csv')

#%% Seleccionar los datos para el análisis
data = data.drop(['Time','Class'],axis=1)

#%% Normalizar la columna Amount
data['Amount'] =(data['Amount']-data['Amount'].mean())/data['Amount'].std()

#%% Aplicar el algoritmo de clustering
inercias = np.zeros(7)
for k in np.arange(7)+1:
    model = KMeans(n_clusters=k,init='random')
    model = model.fit(data)
    inercias[k-1] = model.inertia_

#%% Crear la grafica de codo
plt.plot(np.arange(1,8),inercias)
plt.xlabel('Num grupos')
plt.ylabel('Inercia')
plt.show()

#%% Ejecutar el algoritmo con el numero de grupos deseado
model = KMeans(n_clusters=6,init='random')
model = model.fit(data)
grupos = model.predict(data)

#%% Graficar o verificar los centroides
centroides = model.cluster_centers_
plt.plot(centroides.transpose())
plt.grid()
plt.show()












