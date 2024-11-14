# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:10:18 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,precision_score,recall_score)

#%% Importar los datos para el análisis
data = pd.read_csv('..\Data\ex2data2.txt',header=None)
X = data.iloc[:,0:2]
Y = data.iloc[:,2]
plt.scatter(X[0],X[1],c=Y)
plt.show()

#%% Preparar los datos (crear el polinomio deseado)
ngrado = 7
poly = PolynomialFeatures(ngrado)
Xa = poly.fit_transform(X)

#%% Crear y entrenar la regresión logistica
modelo = linear_model.LogisticRegression(C=1e20)
modelo.fit(Xa,Y)

Yhat = modelo.predict(Xa)
#%%
accuracy_score(Y,Yhat)
#%%
precision_score(Y,Yhat)
#%%
recall_score(Y,Yhat)

#%% Opcional (Dibujar la frontera)
h = 0.01
xmin,xmax = X[0].min(),X[0].max()
ymin,ymax = X[1].min(),X[1].max()
xx,yy = np.meshgrid(np.arange(xmin,xmax,h),np.arange(ymin,ymax,h))
Xnew = pd.DataFrame(np.c_[xx.ravel(),yy.ravel()])

Xam = poly.fit_transform(Xnew)
Z = modelo.predict(Xam)
Z = Z.reshape(xx.shape)

plt.contour(xx,yy,Z,cmap=plt.cm.Paired)
plt.scatter(X[0],X[1],c=Y,cmap=plt.cm.Paired)
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()


#%% Identificar el overfitting
W = modelo.coef_
plt.bar(np.arange(len(W[0])),W[0])
plt.show()













