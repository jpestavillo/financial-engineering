

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,precision_score,recall_score) #suma de 1 y 0 para saber el resultado del modelo 

#%%  importar los datos para el analisis
data= pd.read_csv('ex2data2.txt',header=None)
X= data.iloc[:,0:2]
Y=data.iloc[:,2]
plt.scatter(X[0],X[1],c=Y)
plt.show()
#%% buscar el mejor polinomio 
modelo=linear_model.LogisticRegression(C=1) ##  para que tengan la misma importancia debe ser 1. 
grados=np.arange(1,18)
accu=np.zeros(grados.shape)
prec=np.zeros(grados.shape)
reca=np.zeros(grados.shape)
nvar=np.zeros(grados.shape)
for ngrado in grados:
    poly=PolynomialFeatures(ngrado)
    Xa=poly.fit_transform(X)
    modelo.fit(Xa,Y)
    Yhat=modelo.predict(Xa)
    accu[ngrado-1]=accuracy_score(Y,Yhat)
    prec[ngrado-1]=precision_score(Y,Yhat)
    reca[ngrado-1]=recall_score(Y,Yhat)
    nvar[ngrado-1]=len(modelo.coef_[0])
    
#%%} dibujar la grafica de codo
plt.plot(grados,accu)
plt.plot(grados,prec)
plt.plot(grados,reca)
plt.xlabel('grado del polinomio')
plt.ylabel('% aciertos')
plt.legend(('Accuracy','Presicion','recall'),loc='best')
plt.grid()
plt.show()

plt.plot(grados, nvar)
plt.xlabel('grado del polinomio')
plt.ylabel('% aciertos')
plt.grid()
plt.show()
#%% optimizacion del modelo version 1 
ngrado=6
poly= PolynomialFeatures(ngrado)
Xa= poly.fit_transform(X)
modelo=linear_model.LogisticRegression(C=1)
modelo.fit(Xa,Y)
Yhat= modelo.predict(Xa)
recall_score(Y,Yhat)

W= modelo.coef_[0]
plt.bar(np.arange(len(W)),np.abs(W))
plt.show()

umbral=.25
indx=np.abs(W)>umbral 
Xa_simplificada=Xa[:,indx]  #aqui le estas diciendo que cualquier variable que tenga menos de .25 de coeficiente se elimina

modelo_simplificado=linear_model.LogisticRegression(C=1)
modelo_simplificado.fit(Xa_simplificada,Y)
Yhat_sim=modelo_simplificado.predict(Xa_simplificada)
recall_score(Y,Yhat_sim)

