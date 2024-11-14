# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:02:11 2018

@author: juanp
"""

#%%  pregunta 2 
import numpy as np
from sklearn import svm
import pandas as pd
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score)

data = pd.read_csv('../data/dataset_2.csv')


x = data.iloc[:,0:2]
y = data.iloc[:,2:]
#%% cambiamos el texto a numeros 
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     

y= y.apply(replace_text,args=('Malo',0)).apply(replace_text,args=('Regular',1)).apply(replace_text,args=('Bueno',2))
#%% normalizar o estandarizar datos
x_norm = (x-x.mean(axis=0))/x.std(axis=0)
x_norm = np.array(x_norm)
y = np.array(y)
#%%
modelo =svm.SVC(kernel='linear')
modelo.fit(x_norm,y)
yhat = modelo.predict(x_norm)

print(accuracy_score(y,yhat))
print(precision_score(y,yhat, average=None))
print(recall_score(y,yhat, average=None))
#%%




