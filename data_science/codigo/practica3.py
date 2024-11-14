# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:02:28 2018

@author: if709274
"""

import pandas as pd
import numpy as np
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%%


#%%
colsel=np.arange(6,96,3)
#quiero arreglo empezando de 6 hasta la 96 con brinco de 3
names=list(data.columns.values[colsel])
#dame los nombres de las columnas que me interesan
datanew=data[names]
#datanew['Matrix'][datanew['Matrix']<=3]=0  para limpiar 

#%% cambiar a me gusta o no me gusta
for col in names:
    datanew[col][datanew[col]<=3]=0
    datanew[col][datanew[col]>3]=1
    datanew[col][datanew[col].isnull()]=0
    
    #de data limpia, toma cada columna y si tiene menos de 3 estrellas hazla 0, >3 =1
    
#%%
cfm=skm.confusion_matrix(datanew.iloc[0,:],datanew.iloc[1,:])
#de libreria skm hazme una matriz para comparar binario para ver que tanto se parecen los usuarios

#%%
sim_simple=(cfm[0,0]+cfm[1,1])/np.sum(cfm)
sim_simple_lib=skm.accuracy_score(datanew.iloc[0,:],datanew.iloc[1,:])
#jaccard
sim_jaccard=(cfm[1,1])/(np.sum(cfm)-cfm[0,0])

#%% calculo de distancias 
d1=sc.matching(datanew.iloc[0,:],datanew.iloc[1,:])  #debe ser el complemento

D1=sc.pdist(datanew,'matching')    #combinaciones posibles
D1=sc.squareform(D1)

D2=sc.squareform(sc.pdist(datanew,'jaccard'))
val_min=np.sort(D2)
val_min_ind=np.argsort(D2)

tmp=datanew.loc[38]
#sklearn
#scipy
#thensorflow

