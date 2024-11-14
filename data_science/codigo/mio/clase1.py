# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd

file='../data/coches.csv'
vehicles= pd.read_csv(file)
file1='../data/accidents.csv'
accidents=pd.read_csv(file1)
file2='../data/casualties.csv'
casualties=pd.read_csv(file)

data=vehicles

#def dpr(data):
    #%%
columnas=pd.DataFrame(list(data.columns.values))
#%% lista de tipos de variables 

d_types=pd.DataFrame(data.dtypes,columns=['D_types'])

#%%
missing=pd.DataFrame(data.isnull().sum(),columns=['missing_values'])

#%% lista de los datos presentes 
present= pd.DataFrame(data.count(),columns=['present_values'])
#%%
unique_values=pd.DataFrame(columns=['Unique_Values'])
for col in list(data.columns.values) :
    unique_values.loc[col]=[data[col].nunique()]
    
    #data[vehicl_type]
#%% lista 
min_values=pd.DataFrame(columns=['min'])
for col in list(data.columns.values):
    try: 
        min_values.loc[col]=[data[col].min()]
    except: 
        pass
max_values=pd.DataFrame(columns=['max'])
for col in list(data.columns.values):
    try:
        max_values.loc[col]=[data[col].max()]
    except:
        pass
dpr=d_types.join(missing).join(present).join(unique_values).join(min_values).join(max_values)
    #%% reporte de calidad de los datos}
    #return d_types.join(missing).join(present).join(unique_values).join(min_values).join(max_values)
mireporte=dpr(data)

mireporte=dpr(vehicles)
mireporte1=dpr(accidents)
mireporte2=dpr(casualties)