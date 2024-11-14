# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:05:55 2018

@author: juanp
"""
import pandas as pd
import string
import matplotlib.pyplot as plt
import scipy.spatial.distance  as sc 
data=pd.read_csv('../data/dirty_Info_Alumnos_v1.csv',encoding ='latin1')

#%% funciones para limpiar datos 
def remove_punctuation(x):
    try:
        x=''.join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x

#%% remover numeros del texto 
def remove_digits(x):
    try:
        x=''.join(ch for ch in x if ch not in string.digits)
    except:
        pass
    return x
#%% remover espacios en blanco
def remove_whitespaces(x):
    try:
        x=''.join(x.split())
    except:
        pass
    return x
#%% convertir todo a mayusculas 
def uppercase_text(x):
    try:
        x=x.upper()
    except:
        pass
    return x

#%% convertir todo a minúsculas 
def lower_case(x):
    try: 
        x=x.lower()
    except: 
        pass
    return x 
#%%
def remove_exceptdigits(x):
    try:
        x=''.join(ch for ch in x if ch in string.digits)
    except:
        pass
    return x

#%%
def replace_text(x,to_replace,replacement):
    try:
        x=x.replace(to_replace,replacement)
    except:
        pass
    return x

#%% ahora si limpiamos 
#primero la primera columna
data.columns=['Nombre Completo','Edad','Telefono','Semestre','Num expediente']

data['Nombre Completo']=data['Nombre Completo'].apply(replace_text,args=('x0x0','')).apply(replace_text,args=('-',' ')).apply(replace_text,args=('%',' ')).apply(replace_text,args=('¥','Ñ')).apply(replace_text,args=(':p',' ')).apply(replace_text,args=('0','O')).apply(replace_text,args=('&',' ')).apply(replace_text,args=('_',' ')).apply(uppercase_text).apply(remove_digits).apply(remove_punctuation).apply(replace_text,args=('PEDRQ','PEDRO')).apply(replace_text,args=('  ',' '))
data['Telefono']=data['Telefono'].apply(remove_punctuation).apply(remove_whitespaces)
data.Semestre=data.Semestre.apply(remove_exceptdigits)
for k in range(0,48):
    if len(data.Telefono[k])<10:
        data.Telefono[k]= 'Missing'
    
    else:
        pass
for k in range(0,48):
    if len(str(data['Num expediente'][k]))<6:
        data['Num expediente'][k]= 'Missing'
    
    else:
        pass
#%% importamos el nuevo archivo 
enfermedades=pd.read_csv('../data/enfermedades.csv')
#enfermedades=enfermedades.iloc[:,1:]

enfermedades['1']=(enfermedades['2011']-enfermedades['2010'])/enfermedades['2010']*100
enfermedades['2']=(enfermedades['2012']-enfermedades['2011'])/enfermedades['2011']*100
enfermedades['3']=(enfermedades['2013']-enfermedades['2012'])/enfermedades['2012']*100
enfermedades['4']=(enfermedades['2014']-enfermedades['2013'])/enfermedades['2013']*100
#%% aqui graficamos 
crecimiento=enfermedades.iloc[:,-4:]
crecimiento=crecimiento.transpose()
plt.figure(figsize=(15,15,))
crecimiento.plot()
plt.xlabel('años')
plt.ylabel('crecimiento %')
plt.grid()
plt.legend(('Casos de Dengue', 'Casos de Influenza A H1N1', 'Casos de VIH/SIDA','Egresos hospitalarios', 'Esperanza de vida al nacer','Muertes maternas'),loc='best')
plt.show()

#%% distancias 

crecimiento_norm=(crecimiento-crecimiento.mean(axis=0))/crecimiento.std(axis=0)
D1=sc.pdist(crecimiento_norm,'euclidean')
D1=sc.squareform(D1)
D2=sc.pdist(crecimiento_norm,'cosine')
D2=sc.squareform(D2)
