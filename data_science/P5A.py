# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:29:11 2018

@author: riemannruiz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as skm
import scipy.spatial.distance as sc
from mylib import mylib

#%%
accidents = pd.read_csv('../data/Accidents_2015.csv')

mireporte = mylib.dqr(accidents)

#%% Seleccionar variables categoricas
indx = np.array(accidents.dtypes=='int64')
col_names = list(accidents.columns.values[indx])
accidents_int = accidents[col_names].dropna()

#%%
mireporte2 = mylib.dqr(accidents_int)

#%% Seleccionar columnas con menos valores unicos que 15
indx = mireporte2.Unique_Values<15
col_names_unique = np.array(col_names)[indx]
accidents_int_uni = accidents_int[col_names_unique]

#%% Generar las variables dummies
dummy1 = pd.get_dummies(accidents_int_uni.Accident_Severity,
                        prefix='Accident_Severity')
#%% Aplicarle la generacion de dummies a toda la tabla y juntarla en una sola
ac_dummy = pd.get_dummies(accidents_int_uni[col_names_unique[0]],
                          prefix=col_names_unique[0])
for col in col_names_unique[1:]:
    tmp = pd.get_dummies(accidents_int_uni[col],
                         prefix=col)
    ac_dummy = ac_dummy.join(tmp)
del tmp

#%% Aplicacion de los indices similitud
#D1 = sc.pdist(ac_dummy,'matching')
D1 = sc.pdist(ac_dummy.iloc[0:50000,:],'matching')
D1 = sc.squareform(D1)














