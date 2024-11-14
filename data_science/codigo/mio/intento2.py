# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:44:26 2018

@author: juanp
"""

import pandas as pd

file='../data/coches.csv'
coches=pd.read_csv(file)
data=coches

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
    #%% reporte de calidad de los datos}