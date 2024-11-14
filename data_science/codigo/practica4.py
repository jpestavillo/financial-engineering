# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:02:28 2018

@author: if709274
"""

import pandas as pd
import numpy as np
import scipy.spatial.distance as sc
import sklearn.metrics as skm
import sklearn.datasets as datasets
import matplotlib.pyplot as plt

#%%
digits=datasets.load_digits()
#%%
ndig=10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.axis('off')
    plt.imshow(digits.images[k],cmap=plt.cm.gray_r)
    plt.title('digit: %i' % k)
plt.show()    

#%% seleccionar los datos que tenemos que analizar
#si tiene indices es un data frame
#si no tiene indices es un arreglo normal
data=digits.data
umbral=8
data[data<=umbral]=0
data[data>umbral]=1

datanew= pd.DataFrame(data)
    
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

