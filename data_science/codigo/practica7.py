# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:59:16 2018

@author: if709274
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy.spatial.distance  as sc 

#%%
data=pd.read_excel('../data/datos_2015.xlsx', sheetname='Atemajac')
data=data.iloc[:,2:7].dropna()
#%%

#?plt.scatter()
plt.scatter(data['CO'],data['NO2'])
plt.xlabel('CO')
plt.ylabel('NO2')
plt.axis('square')
plt.show()

plt.scatter(data['CO'],data['PM10'])
plt.xlabel('CO')
plt.ylabel('PM10')
plt.axis('square')
plt.show()

#%%  normalizar datos   #usamos e**-((x-miu)/desviacion)**2
data_norm=(data-data.mean(axis=0))/data.std(axis=0)
#el axis es para que te de la media por el que quieres aplicar la operacion.  
#0 =columnas
#1= filas
plt.scatter(data_norm['CO'],data_norm['NO2'])
plt.xlabel('CO')
plt.ylabel('NO2')
plt.axis('square')
plt.show()
#%%
D1=sc.pdist(data_norm,'euclidean')
D1=sc.squareform(D1)

D2=sc.pdist(data_norm.transpose(),'euclidean')
D2=sc.squareform(D2)
#%% medir tiempo de ejecucion
import time 
t0=time.time()
D1=sc.pdist(data_norm,'cosine')
D1=sc.squareform(D1)
time.time()-t0