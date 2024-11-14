# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import numpy as np

dir_file = '../data/coches.csv'
#dir_file = 'C:\Users\sacel\Desktop\CDIN\DATA\Vehicles_2015.csv'
#dir_file = 'Vehicles_2015.csv'
vehicles= pd.read_csv(dir_file)

dir_file = '../data/Accidentes.csv'
accidentes = pd.read_csv(dir_file)

dir_file = '../data/Casualties.csv'
casualities = pd.read_csv(dir_file)



def dqr(data):

    #%% Lista de variable de datos
    columns = pd.DataFrame(list(data.columns.values))
    
    #%% Listra de los tipos de la variable
    d_types = pd.DataFrame(data.dtypes,columns=['D_types'])
    
    #%%  Lista con los datos faltantes
    
    missing = pd.DataFrame(data.isnull().sum(), columns= ['mising_values'])
     
    #%% Lista de datos presentes
    
    present = pd.DataFrame(data.count(), columns=['present_values']) 
    #%% table de valores únicos 
    unique_values = pd.DataFrame(columns= ['Unique_Values'])
    for col in list(data.columns.values):
        unique_values.loc[col] = [data[col].nunique()] 
        
    #%% Lista de Valores mínimos
    min_values = pd.DataFrame(columns = ['Min'])
    for col in list(data.columns.values):
        try:
            min_values.loc[col] = [data[col].min()]
        except:
            pass
    #%% valores máximos
    max_values = pd.DataFrame(columns = ['Max'])
    for col in list(data.columns.values):
        try:
            max_values.loc[col] = [data[col].max()]
        except:
            pass
        
    #%% crear reporte de calidad de los datos(data quality report)
    
    return d_types.join(missing).join(present).join(unique_values).join(min_values).join(max_values)

#%%
mireporte = dqr(vehicles)
mi1reporte = dqr(accidentes)
mi2reporte = dqr(casualities) 


 






















