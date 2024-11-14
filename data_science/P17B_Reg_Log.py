# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs
import scipy.optimize as opt


#%% Generar los datos a clasificar
X,Y = make_blobs(n_samples=200,
                 centers=[[0,0],[3,3]],
                 cluster_std=0.5,
                 n_features=2)

plt.scatter(X[:,0],X[:,1],c=Y)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()


#%% Función Logística
def fun_log(X):
    return 1/(1+np.exp(-X))

#%% Función regresión logística
def reg_log(W,X,Y):
    V = np.matrix(X)*np.matrix(W).transpose()
    return np.array(fun_log(V))[:,0]

#%% Función la función de costo
def fun_cost(W,X,Y):
    Yhat = reg_log(W,X,Y)
    J = np.sum(-Y*np.log(Yhat)-(1-Y)*np.log(1-Yhat))/len(Y)
    return J


#%% Inicializar los cvaribales para la optimización
Xa = np.append(np.ones((len(Y),1)),X,axis=1)
m,n = np.shape(Xa)
W = np.zeros(n)

#Optimizacion
res = opt.minimize(fun_cost,W,args=(Xa,Y))
W = res.x

#%% Simular la regresión logistica obtenida
Yhat = np.round(reg_log(W,Xa,Y),0)


#%% Generar todas las posibles combinaciones entre x1 y x2
x = np.arange(-3,5,0.01)
y = np.arange(-3,5,0.01)
Xm,Ym = np.meshgrid(x,y)
m,n = np.shape(Xm)
Xmr = np.reshape(Xm,(m*n,1))
Ymr = np.reshape(Ym,(m*n,1))

Xtmp = np.append(Xmr,Ymr,axis=1)
Xtmp = np.append(np.ones((len(Xmr),1)),Xtmp,axis=1)
Ytmp = np.round(reg_log(W,Xtmp,Xmr),0)
#Ytmp = reg_log(W,Xtmp,Xmr)
Z = np.reshape(Ytmp,(m,n))

#%% Dibujar
plt.contour(Xm,Ym,Z)
plt.scatter(X[:,0],X[:,1],c=Y)
plt.show()






















