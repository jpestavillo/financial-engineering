# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:43:07 2018

@author: if709274
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sklearn.metrics as skm
import scipy.spatial.distance as sc
from mylib import mylib

#%%
accidents=pd.read_csv('../data/accidentes.csv')

mireporte= mylib.dqr(accidents)
#%%
indx=np.array(accidents.dtypes=='int64')
col_names=list(accidents.columns.values[indx])
accidents_int=accidents[col_names]
#col_data=data[col_names]
#%%
mireporte2=mylib.dqr(accidents_int)
#%%
indx=mireporte2.Unique_Values<60
col_names_unique=np.array(col_names)[indx]
accidents_int_unique= accidents_int[col_names_unique]
#%%
dummy1=pd.get_dummies(accidents_int_unique.Accident_Severity)

ac_dummy=pd.get_dummies(accidents_int_unique[col_names_unique[0]],prefix=col_names_unique[0])

for col in col_names_unique[1:]:
    tmp= pd.get_dummies(accidents_int_unique[col],
                        prefix=col)
    ac_dummy=ac_dummy.join(tmp)
del tmp
                         
#%%
D1=sc.pdist(ac_dummy.iloc[0:100,:],'matching')