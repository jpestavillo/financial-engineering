# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd
import numpy as np
import scipy.spatial.distance as sc
import sklearn.metrics as skm
import sklearn.datasets as datasets
import matplotlib.pyplot as plt

#%% Importar la tabla de datos
digits = datasets.load_digits()

#%% Dibujar una muestra de los digitos
ndig = 10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.axis('off')
    plt.imshow(digits.images[k],cmap=plt.cm.gray_r)
    plt.title('Digit: %i' % k)
plt.show()

#%% Seleccionar los datos que analizaremos
data = digits.data
umbral = 8
data[data<=umbral] = 0
data[data>umbral] = 1

datanew = pd.DataFrame(data)

    
#%% Calculo de los indices de similitud
cfm = skm.confusion_matrix(datanew.iloc[0,:],datanew.iloc[1,:])

# Empareajmiento simple
sim_simple = (cfm[0,0]+cfm[1,1])/np.sum(cfm)
sim_simple_lib = skm.accuracy_score(datanew.iloc[0,:],datanew.iloc[1,:])

# Jaccard
sim_jaccard = (cfm[1,1])/(np.sum(cfm)-cfm[0,0])
#sim_jaccard_lib = skm.jaccard_similarity_score(datanew.iloc[0,:],datanew.iloc[1,:])

#%% Calculo de las distancias
d1 = sc.matching(datanew.iloc[0,:],datanew.iloc[1,:])

D1 = sc.pdist(datanew,'matching')
D1 = sc.squareform(D1)

D2 = sc.squareform(sc.pdist(datanew,'jaccard'))

val_min = np.sort(D2)
val_min_ind = np.argsort(D2)

tmp = datanew.loc[[38,39]]




#%%
ndig = 10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.axis('off')
    plt.imshow(np.reshape(data[k],(8,8)),cmap=plt.cm.gray_r)
    plt.title('Digit: %i' % k)
plt.show()






















