# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd

#%%
data_dir = '../Data/Vehicles_2015.csv'
#data_dir = 'G:\CDIN_O18\Data\Vehicles_2015.csv'
#data_dir = 'Vehicles_2015.csv'
vehicles = pd.read_csv(data_dir)

data_dir = '../Data/Accidents_2015.csv'
accidents = pd.read_csv(data_dir)
data_dir = '../Data/Casualties_2015.csv'
casualties = pd.read_csv(data_dir)

def dqr(data):
    #%% Lista de variables de la base de datos
    columns = pd.DataFrame(list(data.columns.values),
                           columns=['Nombres'],
                           index=list(data.columns.values))
    
    #%% lista de tipos de datos
    data_types = pd.DataFrame(data.dtypes,columns=['Data_Types'])
    
    #%% lista de datos perdidos
    missing_values = pd.DataFrame(data.isnull().sum(),
                                  columns=['Missing_Values'])
    
    #%% Lista de los datos presentes
    present_values = pd.DataFrame(data.count(),
                                  columns=['Present_Values'])
    
    #%% Lista de valores unicos
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
    #%% Juntar todas las tablas
    return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)

#%% utilizar mi funcion
mireporte = dqr(vehicles)
mireporte1 = dqr(accidents)
mireporte2 = dqr(casualties)





















