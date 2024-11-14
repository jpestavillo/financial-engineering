# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:54:19 2018

@author: riemannruiz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%% Importar los datos
data = pd.read_excel('../Data/Datos_2015.xlsx',sheetname='Atemajac')

#%% Quitar los valores nulos
data = data.iloc[:,0:7].dropna()

#%%
plt.scatter(data['CO'],data['NO2'])
plt.xlabel('CO')
plt.ylabel('NO2')
plt.axis('square')
plt.show()

plt.scatter(data['NO2'],data['PM10'])
plt.xlabel('NO2')
plt.ylabel('PM10')
plt.axis('square')
plt.show()

#%% Obtener distancias con datos originales
D1 = sc.pdist(data.iloc[:,2:],'euclidean')
D1 = sc.squareform(D1)


#%% Normalizado de los datos
data = data.iloc[:,2:7]
#%%
data_norm = (data-data.mean(axis=0))/data.std(axis=0)

plt.scatter(data_norm['NO2'],data_norm['PM10'])
plt.xlabel('NO2')
plt.ylabel('PM10')
plt.axis('square')
plt.show()























