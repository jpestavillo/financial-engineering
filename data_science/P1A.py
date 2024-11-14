# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import numpy as np

#%%

dir_file = '../Data/Vehicles_2015.csv'
#dir_file = 'G:/CDIN_O18/Data/Vehicles_2015.csv'
#dir_file = 'Vehicles_2015.csv'
vehicles = pd.read_csv(dir_file)

dir_file = '../Data/Accidents_2015.csv'
accidents = pd.read_csv(dir_file)

dir_file = '../Data/Casualties_2015.csv'
casualties = pd.read_csv(dir_file)

#%%
def dqr(data):
    #%% Lista de las variable de los datos
    columns = pd.DataFrame(list(data.columns.values))
    
    #%% Lista de los tipos de variables
    d_types = pd.DataFrame(data.dtypes,columns=['D_types'])
    
    #%% Lista con los datos faltantes
    missing = pd.DataFrame(data.isnull().sum(),
                           columns=['missing_values'])
    #%% Lista de datos presentes
    present = pd.DataFrame(data.count(),columns=['present_values'])
    
    #%% tabla de valores únicos
    unique_values = pd.DataFrame(columns=['Unique_Values'])
    for col in list(data.columns.values):
        unique_values.loc[col] = [data[col].nunique()]
        
    #%% Lista de valores minimos
    min_values = pd.DataFrame(columns=['Min'])
    for col in list(data.columns.values):
        try:
            min_values.loc[col] = [data[col].min()]
        except:
            pass
    
    #%% Lista de valores maximos
    max_values = pd.DataFrame(columns=['Max'])
    for col in list(data.columns.values):
        try:
            max_values.loc[col] = [data[col].max()]
        except:
            pass

    #%% crear el reporte de calidad de los datos (data quality report)
    return d_types.join(missing).join(present).join(unique_values).join(min_values).join(max_values)

#%%
mireporte = dqr(vehicles)
mireporte1 = dqr(accidents)
mireporte2 = dqr(casualties)
























