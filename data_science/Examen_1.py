# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:13:08 2018

@author: Job
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%% Pregunta 2b
import pandas as pd

data=[[1,1,2,3,3],[50000.00,5000.50,5000.00,1000.00,10000.00],[100000.00,300000.00,259236.05,540689.00,200000.00]]

data = pd.DataFrame(data)
data = data.transpose()

vardummy=pd.get_dummies(data[0])
vardummy1=pd.get_dummies(data[1])
vardummy2=pd.get_dummies(data[2])

vardummyjoin = vardummy.join(vardummy1).join(vardummy2)

#%% Pregunta 3

#%% Descargar los Datos

dirty = pd.read_csv('C:/Users/jobch/Documents/ITESO/OneDrive - ITESO/ITESO/5to Semestre/Ciencia de Datos e Inteligencia de Datos/Data/Dirty_Datav2.csv',encoding='latin1')
dirty.columns = ['NombreCompleto','Edad','Semestre','NumExpediente','Telefono']

#%% Funciones para limpiar Datos

from mylib import mylib
    
#%% Limpiar Nombres

dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('¾','ñ'))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('RU1Z','RUIZ'))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('PEDRQ','PEDRO'))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('PEÑA HINOJOSA Ð Ð HERMELA','PEÑA HINOJOSA HERMELA'))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('1',''))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('?',' '))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('x0x0',''))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=(':0',''))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=(':P',''))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('0','O'))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=(' ­ ­ ',''))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.remove_digits)
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('_',' '))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('-',' '))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.replace_text,args=('&',' '))
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.remove_punctuation)
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.add_whitespace)
dirty['NombreCompleto'] = dirty['NombreCompleto'].apply(mylib.uppercase_text)      


#%% Limpiar Teléfono

dirty['Telefono'] = dirty['Telefono'].apply(mylib.remove_punctuation)
dirty['Telefono'] = dirty['Telefono'].apply(mylib.remove_whitespace)
dirty['Telefono'] = dirty['Telefono'].apply(mylib.missing_10)


#%% Limpiar Semestre

dirty['Semestre'] = dirty['Semestre'].apply(mylib.digits)

#%% Limpiar NumExpediente

dirty['NumExpediente'] = dirty['NumExpediente'].apply(mylib.missing_6)

#%% Pregunta 4

#%% Descargar Datos

diseases = dirty = pd.read_csv('C:/Users/jobch/Documents/ITESO/OneDrive - ITESO/ITESO/5to Semestre/Ciencia de Datos e Inteligencia de Datos/Data/Diseases.csv',encoding='latin1')
diseases.index = diseases['nombre']
diseases = diseases.iloc[:,1:]
years = diseases.iloc[:,0:]
yearstranspose = years.transpose()

diseases['10-11'] = ((diseases['2011']-diseases['2010'])/diseases['2010'])*100
diseases['11-12'] = ((diseases['2012']-diseases['2011'])/diseases['2011'])*100
diseases['12-13'] = ((diseases['2013']-diseases['2012'])/diseases['2012'])*100
diseases['13-14'] = ((diseases['2014']-diseases['2013'])/diseases['2013'])*100

changes = diseases.iloc[:,5:]
changestranspose = changes.transpose()

#%% Graficar

plt.figure(figsize=(10,10))
changestranspose.plot()
plt.title('Cambios Porcentuales de Enfermedades')
plt.xlabel('Años')
plt.ylabel('Cambio porcentual')
plt.grid(True)
plt.legend(('Casos de Dengue', 'Casos de Influenza A H1N1', 'Casos de VIH/SIDA','Egresos hospitalarios', 'Esperanza de vida al nacer','Muertes maternas'),loc='best')
plt.show()

#%% Medidas de Similitud

changessimilitud = sc.pdist(changes,'euclidean')
changessimlitud = pd.DataFrame(sc.squareform(changessimilitud))
changessimlitud.columns = ['Casos de Dengue', 'Casos de Influenza A H1N1', 'Casos de VIH/SIDA','Egresos hospitalarios', 'Esperanza de vida al nacer','Muertes maternas']
changessimlitud.index = ['Casos de Dengue', 'Casos de Influenza A H1N1', 'Casos de VIH/SIDA','Egresos hospitalarios', 'Esperanza de vida al nacer','Muertes maternas']
        
#%% Medidas de Similitud por Años

yearssimilitud = sc.pdist(yearstranspose,'euclidean')
yearssimilitud = pd.DataFrame(sc.squareform(yearssimilitud))
yearssimilitud.columns = ['2010','2011','2012','2013','2014']
yearssimilitud.index = ['2010','2011','2012','2013','2014']

#%%
    
    
    
    
    
    
    
    
    
    