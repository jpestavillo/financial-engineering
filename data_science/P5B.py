# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:30:44 2018

@author: riemannruiz
"""

import numpy as np
import pandas as pd
import sklearn.metrics as skm
import scipy.spatial.distance as sc
from mylib import mylib

#%% Importar los datos
accidents = pd.read_csv('../Data/Accidents_2015.csv')

#%% Aplicar el dqr
mireporte = mylib.dqr(accidents)

#%% Elegir columnas solo con datos enteros
indx = np.array(accidents.dtypes == 'int64')
col_list = list(accidents.columns.values[indx])
accidents_int = accidents[col_list]
del indx
#%% aplicar nuevamente dqr
mireporte = mylib.dqr(accidents_int)

#%% Filtrar por los valores unicos de las variables
indx = np.array(mireporte.Unique_Values<=20)
#indx = np.array(mireporte['Unique_Values']<=20)
col_list_2 = np.array(col_list)[indx]
accidents_int_unique = accidents_int[col_list_2]

#%% Generar variables dummies 
dummy1 = pd.get_dummies(accidents_int_unique.Accident_Severity,
                        prefix='Accident_Severity')

#%% aplicar dummies a la tabla completa
accidents_dummy = pd.get_dummies(accidents_int_unique[col_list_2[0]],
                                 prefix=col_list_2[0])
for col in col_list_2[1:]:
    tmp = pd.get_dummies(accidents_int_unique[col],
                         prefix=col)
    accidents_dummy = accidents_dummy.join(tmp)
del tmp

#%% Aplicar indices de similitud o distancia
DIST1 = sc.squareform(sc.pdist(accidents_dummy.iloc[0:30,:],'matching'))
tmp = pd.DataFrame(DIST1)

#%% Buscar los más parecidos
D1_ordenado = np.sort(tmp)
D1_index = np.argsort(tmp)
























