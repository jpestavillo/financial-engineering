# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 08:27:41 2018

@author: juanp
"""
import pandas as pd
from mylib import mylib
import scipy.spatial.distance  as sc 
import time 
t0=time.time()  #solo para saber cuanto tarda mi compu en correr la tarea
#%%  inciso 1 
atemajac=pd.read_excel('../data/datos_2015.xlsx',sheetname='Atemajac').iloc[:,1:7]
centro  =pd.read_excel('../data/datos_2015.xlsx',sheetname='Centro').iloc[:,1:7]
oblatos=pd.read_excel('../data/datos_2015.xlsx',sheetname='Oblatos').iloc[:,1:7]
miravalle=pd.read_excel('../data/datos_2015.xlsx',sheetname='Miravalle').iloc[:,1:7]
#%% inciso 2
rep_atemajac=mylib.dqr(atemajac)
rep_centro=mylib.dqr(centro)
rep_oblatos=mylib.dqr(oblatos)
rep_miravalle=mylib.dqr(miravalle)
#%% inciso 3
def comp_similar(data):
    data=data.iloc[:,[-3,-2]]
    data_norm=(data-data.mean(axis=0))/data.std(axis=0)
    D2=sc.pdist(data_norm,'cosine')
    D2=sc.squareform(D2)
    return D2
dist_atemajac=comp_similar(atemajac)
dist_centro=comp_similar(centro)
dist_oblatos=comp_similar(oblatos)
dist_miravalle=comp_similar(miravalle)
print("realmente, utilizando el indice de similitud de coseno se encontro que",
      "no existe una similitud grande debido a que en repetidas veces aparecieron",
      "valores que representan muy baja similitud")

#%% inciso4
print("durante esta actividad aprendi a utilizar las medidas de similitud para",
      "bases de datos y poder saber como se comportan de una manera mas simple, ademas de reforzar el como realizar funciones")
t=time.time()-t0
del t0