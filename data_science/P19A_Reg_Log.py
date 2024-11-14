# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:50:00 2018

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

#%% Buscar el mejor polinomio
modelo = linear_model.LogisticRegression(C=1)
grados = np.arange(1,18)
Accu = np.zeros(grados.shape)
Prec = np.zeros(grados.shape)
Reca = np.zeros(grados.shape)
Nvar = np.zeros(grados.shape)

for ngrado in grados:
    poly = PolynomialFeatures(ngrado)
    Xa = poly.fit_transform(X)
    modelo.fit(Xa,Y)
    Yhat = modelo.predict(Xa)
    Accu[ngrado-1] = accuracy_score(Y,Yhat)
    Prec[ngrado-1] = precision_score(Y,Yhat)
    Reca[ngrado-1] = recall_score(Y,Yhat)
    Nvar[ngrado-1] = len(modelo.coef_[0])

#%% Dibujar la gráfica de codo
plt.plot(grados,Accu)
plt.plot(grados,Prec)
plt.plot(grados,Reca)
plt.xlabel('grado del polinomio')
plt.ylabel('% aciertos')
plt.legend(('Accuracy','Precision','Recall'),loc='best')
plt.grid()
plt.show()

plt.plot(grados,Nvar)
plt.xlabel('grado del polinomio')
plt.ylabel('Num. Parametros')
plt.grid()
plt.show()

#%% Optimización del modelo versión 1
ngrado = 6
poly = PolynomialFeatures(ngrado)
Xa = poly.fit_transform(X)
modelo = linear_model.LogisticRegression(C=1)
modelo.fit(Xa,Y)
Yhat = modelo.predict(Xa)
Yhat_prob = modelo.predict_proba(Xa)
recall_score(Y,Yhat)

#%%
W = modelo.coef_[0]
plt.bar(np.arange(len(W)),np.abs(W))
plt.show()
 
#%%
umbral = 0.6
indx = np.abs(W)>umbral
Xa_simplificada = Xa[:,indx]

modelo_simplificado = linear_model.LogisticRegression(C=1)
modelo_simplificado.fit(Xa_simplificada,Y)
Yhat_sim = modelo_simplificado.predict(Xa_simplificada)
recall_score(Y,Yhat_sim)

Ws = modelo_simplificado.coef_[0]
plt.bar(np.arange(len(Ws)),np.abs(Ws))
plt.show()


















