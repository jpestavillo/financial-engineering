# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd
import numpy as np
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%% Importar la tabla de datos
data = pd.read_excel('../Data/Test_Pelis.xlsx')

#%% Seleccionar los datos validos
csel = np.arange(6,96,3)
names = list(data.columns.values[csel])
datanew = data[names]

#%% Cambiar a me gusta o no megusta
for col in names:
    datanew[col][datanew[col]<=3]=0
    datanew[col][datanew[col]>3]=1
    datanew[col][datanew[col].isnull()]=0
    
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




























