# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:02:56 2018

@author: juanp
"""
import pandas as pd
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
from sklearn.cluster import KMeans
import numpy as np
import scipy.optimize as opt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures 
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,precision_score,recall_score)
import pickle
#%%
data3=pd.read_csv('../data/dataset_4.csv',header=None)
data3=data3.iloc[:-1,:3]
X=data3.iloc[:,:2]
X=(X-X.mean())/X.std()
Y=data3.iloc[:,2]
data_norm=data3
#%%
def reg_log(W,X,Y):
    V=np.matrix(X)*np.matrix(W).transpose()
    return np.array(fun_log(V))[:,0]

def fun_log(X):
    return 1/(1+np.exp(-X))

def fun_cost(W,X,Y):
    Yg=reg_log(W,X,Y)
    return np.sum(-Y*np.log(Yg)-(1-Y)*np.log(1-Yg))/len(Yg)
#%%
X_train,X_test,Y_train,Y_test = train_test_split(X,
                                                 Y,
                                                 test_size=0.5,
                                                 random_state=0)
del X,Y

#%% REGRESION LOGISTICA (REEVISAR EL POLINOMIO OPTIMO)
modelo_rl = linear_model.LogisticRegression()
grados = np.arange(1,3)
Accu = np.zeros(grados.shape)
Prec = np.zeros(grados.shape)
Reca = np.zeros(grados.shape)
Nvar = np.zeros(grados.shape)

for ngrado in grados:
    poly = PolynomialFeatures(ngrado)
    Xa = poly.fit_transform(X_train)
    modelo_rl.fit(Xa,Y_train)
    Yhat = modelo_rl.predict(Xa)
    Accu[ngrado-1] = accuracy_score(Y_train,Yhat)
    Prec[ngrado-1] = precision_score(Y_train,Yhat,average=None)
    Reca[ngrado-1] = recall_score(Y_train,Yhat,average=None)
    Nvar[ngrado-1] = len(modelo_rl.coef_[0])

#%% Graficar
plt.plot(grados,Accu)
plt.plot(grados,Prec)
plt.plot(grados,Reca)
plt.xlabel('Grado el polinomio')
plt.ylabel('% Aciertos')
plt.legend(('Accuracy','Precision','Recall'),
           loc='best')
plt.grid()
plt.show()

#%% Modelo definitivo
ngrado = 2
poly = PolynomialFeatures(ngrado)
Xa_train = poly.fit_transform(X_train)
modelo_rl = linear_model.LogisticRegression()
modelo_rl = modelo_rl.fit(Xa_train,Y_train)
#%%
Yhat_rl_train = modelo_rl.predict(Xa_train)

print(accuracy_score(Y_train,Yhat_rl_train))
print(precision_score(Y_train,Yhat_rl_train))
print(recall_score(Y_train,Yhat_rl_train))
#%% inicializar los valores para la optimizacion
Xa= np.append(np.ones((len(Y),1)),X,axis=1)
m,n=np.shape(Xa)
W=np.zeros(n)
#%% optimizar J
res=opt.minimize(fun_cost,W,args=(Xa,1))
W=res.x
#%% simular el modelo logistico
Yg=reg_log(W,Xa,Y)
#%% graficar la frontera de decision 
x0= np.arange(-2,5,.01)
x1= np.arange(-2,5,.01)
#%%
X0,X1=np.meshgrid(x0,x1)
m,n=np.shape(X0)
#%%
X0r=np.reshape(X0,(m*n,1))
X1r=np.reshape(X1,(m*n,1))
Xr=np.append(X0r,X1r,axis=1)
Xr=np.append(np.ones((m*n,1)),Xr,axis=1)

Yf=reg_log(W,Xr,X0r)
Z= np.reshape(Yf,(m,n))
#%% dibujar
plt.contour(X0,X1,Z)
plt.scatter(X[:,0],X[:,1],c=Y)
plt.show()
