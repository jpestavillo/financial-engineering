# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:17:13 2018

@author: riemannruiz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as skm # metricas de similitud
import scipy.spatial.distance as sc # metricas de distancia
from sklearn import datasets

#%% Importat los nuevos datos

digits = datasets.load_digits()

#%% Graficar algunos numeros
ndig = 10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.axis('off')
    plt.imshow(digits.images[k],cmap=plt.cm.gray_r)
    plt.title('Digits: %i' % k)
plt.show()

#%% Seleccionar una muestra de los datos
data = digits.data[0:20]
umbral = 8
data[data<=umbral] = 0
data[data>umbral] = 1

datan = pd.DataFrame(data)


    
#%% Calcular indices de similitud en usuarios
cf_m = skm.confusion_matrix(datan.iloc[0,:],datan.iloc[1,:])

sim_simple = skm.accuracy_score(datan.iloc[0,:],datan.iloc[1,:])
sim_simple_new = (cf_m[0,0]+cf_m[1,1])/np.sum(cf_m)

#sim_jac = skm.jaccard_similarity_score(datan.iloc[0,:],datan.iloc[1,:])
sim_jac_new = (cf_m[1,1])/(np.sum(cf_m)-cf_m[0,0])

#%% Calculo de las distancias
d1 = sc.matching(datan.iloc[0,:],datan.iloc[1,:])
d2 = sc.jaccard(datan.iloc[0,:],datan.iloc[1,:])

#%% Calcular todas las combinaciones posibles
D1 = sc.pdist(datan,'matching')
D1 = sc.squareform(D1)

D2 = sc.pdist(datan,'jaccard')
D2 = sc.squareform(D2)































