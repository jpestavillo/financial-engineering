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

#%% Generar los datos para clasificarlos
X,Y = make_blobs(n_samples=200,
                 centers=[[0,0],[3,3]],
                 cluster_std=1,
                 n_features=2)

plt.scatter(X[:,0],X[:,1],c=Y)
plt.xlabel('x0')
plt.ylabel('x1')
plt.show()

#%% Función de la regresión logística
def reg_log(W,X,Y):
    V = np.matrix(X)*np.matrix(W).transpose()
    return np.array(fun_log(V))[:,0]

#%% Función logística
def fun_log(X):
    return 1/(1+np.exp(-X))

#%% Función de costo
def fun_cost(W,X,Y):
    Yg = reg_log(W,X,Y)
    return np.sum(-Y*np.log(Yg)-(1-Y)*np.log(1-Yg))/len(Y)

#%% Inicalizar los valores para la optimización
Xa = np.append(np.ones((len(Y),1)),X,axis=1)
m,n = np.shape(Xa)
W = np.zeros(n)

#%% Optimizar J
res = opt.minimize(fun_cost,W,args=(Xa,Y))
W = res.x

#%% Simular el modelo logístico
Yg = reg_log(W,Xa,Y)

#%% Graficar la frontera de decisión
x0 = np.arange(-2,5,0.01)
x1 = np.arange(-2,5,0.01)
X0, X1 = np.meshgrid(x0,x1)
m,n = np.shape(X0)
X0r = np.reshape(X0,(m*n,1))
X1r = np.reshape(X1,(m*n,1))
Xr = np.append(X0r,X1r,axis=1)
Xr = np.append(np.ones((m*n,1)),Xr,axis=1)

Yf = reg_log(W,Xr,X0r)
Z = np.reshape(Yf,(m,n))

# Dibujar
plt.contour(X0,X1,Z)
plt.scatter(X[:,0],X[:,1],c=Y)
plt.show()


















