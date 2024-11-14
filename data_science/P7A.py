# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:59:09 2018

@author: riemannruiz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc

#%% Importar datos
data = pd.read_excel('../Data/Datos_2015.xlsx',sheetname='Atemajac')

#%% Filtrar datos
data = data.iloc[:,2:7].dropna()

#%% 
plt.scatter(data['CO'],data['NO2'])
plt.xlabel('CO')
plt.ylabel('NO2')
plt.axis('square')
plt.show()

plt.scatter(data['CO'],data['PM10'])
plt.xlabel('CO')
plt.ylabel('PM10')
plt.axis('square')
plt.show()

#%% Normalizar o estandarizar datos
data_norm = (data-data.mean(axis=0))/data.std(axis=0)

plt.scatter(data_norm['CO'],data_norm['NO2'])
plt.xlabel('CO')
plt.ylabel('NO2')
plt.axis('square')
plt.show()


#%% Distancias e indices

D1 = sc.pdist(data_norm,'euclidean')
D1 = sc.squareform(D1)

D2 = sc.pdist(data_norm.transpose(),'euclidean')
D2 = sc.squareform(D2)

#%% Medir tiempos de ejecución
import time

t0 = time.time()
D1 = sc.pdist(data_norm,'euclidean')
D1 = sc.squareform(D1)
time.time()-t0

#%%
t0 = time.time()
D1 = sc.pdist(data_norm,'cosine')
D1 = sc.squareform(D1)
time.time()-t0

#%%
t0 = time.time()
D1 = sc.pdist(data_norm,'correlation')
D1 = sc.squareform(D1)
time.time()-t0




















