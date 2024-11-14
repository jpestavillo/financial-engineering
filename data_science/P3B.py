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

#%% Importar la tabla
data = pd.read_excel('../Data/Test_Pelis.xlsx')

#%%
csel = np.arange(6,96,3)
cnames = list(data.columns.values[csel])
datan = data[cnames]

#%% Cambiar las estrellas por me gusta o no me gusta
for col in cnames:
    indx = datan[col]<=3
    datan[col][indx]=0
    datan[col][datan[col]>3]=1
    datan[col][datan[col].isnull()]=0
    
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































