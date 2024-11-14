# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:55:38 2018

@author: if709274
"""
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.metrics import (accuracy_score, precision_score, recall_score)
import pickle # Nos sirve para evitar correr nuestro código y que tarde mucho
import matplotlib.pyplot as plt
#%% CARGAR DATA
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
#%% Definir función
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     
data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
data=data.dropna()
y=data.iloc[:,-1]
#%%
media = 0
datam =  data
M_cov = np.cov(datam.transpose())
w,v = np.linalg.eig(M_cov)

#%% Verificar le porcentaje
porcentaje = w/np.sum(w)
porcentaje_acum = np.cumsum(porcentaje)
#%% proyectar todos los digitos en una sola variable 
componentes = w[0:5]
M_trans = np.reshape(v[:,0:5],(22,5))
#%% transformar datos
data_new = np.array(np.matrix(datam)*np.matrix(M_trans))
#%%
data=data_new
#%%
x_norm = data
x=x_norm


#%%

y=np.array(y)
y.shape=(len(y))
x=np.array(x)
x_norm=np.array(x)
modelo =svm.SVC(kernel='linear')



modelo.fit(x_norm,y)
yhat = modelo.predict(x_norm)

print(accuracy_score(y,yhat))
print(precision_score(y,yhat, average=None))
print(recall_score(y,yhat, average=None))


