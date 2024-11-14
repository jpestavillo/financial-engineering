# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:03:56 2018

@author: Mario Abel García
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
#%%
data = pd.read_csv('../Data/dataset_2.csv')

x = data.iloc[:,0:2]
y = data.iloc[:,2:]
#%% cambiar Y Malo*0, Regular*1, Bueno *2
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     

y= y.apply(replace_text,args=('Malo',0)).apply(replace_text,args=('Regular',1)).apply(replace_text,args=('Bueno',2))
#%%

















#%% normalizar o estandarizar datos
x_norm = (x-x.mean(axis=0))/x.std(axis=0)
x_norm = np.array(x_norm)
y = np.array(y)
#%%
modelo =svm.SVC(kernel='linear')
modelo.fit(x_norm,y)
yhat = modelo.predict(x_norm)

#%% visulaizar los resultados
w = modelo.coef_[0]
m = -w[0]/w[1]
b = -modelo.intercept_[0]/w[1]
xx = np.linspace(-5,5)
yy = m*xx+b

vs = modelo.support_vectors_

gamma = modelo.support_vectors_[0]
yy_1 = m*xx+(gamma[1]-m*gamma[0])
gamma = modelo.support_vectors_[-1]
yy_2 = m*xx+(gamma[1]-m*gamma[0])

plt.scatter(x_norm[:,0],x_norm[:,1])
plt.plot(xx,yy,'k-')
plt.scatter(vs[:,0],vs[:,1],s=80,facecolor='k')
plt.plot(xx,yy_1,'k--')
plt.plot(xx,yy_2,'k--')
plt.show()

