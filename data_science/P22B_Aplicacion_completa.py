# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score)
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

import pickle

#%% Importar los datos
data = pd.read_csv('..\Data\creditcard.csv')
X = data.iloc[:,1:30]
Y = data.iloc[:,30]

X['Amount'] = (X['Amount']-X['Amount'].mean())/X['Amount'].std()

del data

#%% Seleccionar la base de entrenamiento y prueba
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y,
                                             test_size=0.4,
                                             random_state=0)
del X,Y

#%% REGRESION LOGISTICA
modelo_rl = linear_model.LogisticRegression()
ngrado = 2
poly = PolynomialFeatures(ngrado)
Xa = poly.fit_transform(Xtrain)
modelo_rl.fit(Xa,Ytrain)
Yhat_train = modelo_rl.predict(Xa)
print(accuracy_score(Ytrain,Yhat_train))
print(precision_score(Ytrain,Yhat_train))
print(recall_score(Ytrain,Yhat_train))

#%% Probar el modelo con el base de prueba
Xa = poly.fit_transform(Xtest)
Yhat_test = modelo_rl.predict(Xa)
print(accuracy_score(Ytest,Yhat_test))
print(precision_score(Ytest,Yhat_test))
print(recall_score(Ytest,Yhat_test))


#%% SUPPORT VECTOR MACHINE
modelo_svm = svm.SVC(kernel='rbf')
modelo_svm.fit(Xtrain,Ytrain)
Yhat_svm = modelo_svm.predict(Xtrain)
print(accuracy_score(Ytrain,Yhat_svm))
print(precision_score(Ytrain,Yhat_svm))
print(recall_score(Ytrain,Yhat_svm))

#%% Probar el SVM en la base de prueba
Yhat_svm_test = modelo_svm.predict(Xtest)
print(accuracy_score(Ytest,Yhat_svm_test))
print(precision_score(Ytest,Yhat_svm_test))
print(recall_score(Ytest,Yhat_svm_test))


#%% Guardar los modelos realizados
pickle.dump(modelo_rl,open('modelo_rl.sav','wb'))
pickle.dump(modelo_svm,open('modelo_svm.sav','wb'))

#%% Tiempo despues usamos el modelo
modelo_rl = pickle.load(open('modelo_rl.sav','rb'))
modelo_svm = pickle.load(open('modelo_svm.sav','rb'))



#%% APLICAR CLUSTERING PARA OBTENER PERFILES DE CLIENTES
inercias = np.zeros(20)
for k in np.arange(len(inercias))+1:
    modelo_km = KMeans(n_clusters=k,init='k-means++')
    modelo_km = modelo_km.fit(Xtrain)
    inercias[k-1] = modelo_km.inertia_

plt.plot(np.arange(1,len(inercias)+1),inercias)
plt.xlabel('Num Grupos')
plt.ylabel('Inercia')
plt.grid()
plt.show()

#%% Crear el modelo 9 clusters
modelo_km = KMeans(n_clusters=9,init='k-means++')
modelo_km = modelo_km.fit(Xtrain)
grupos = modelo_km.predict(Xtrain)

pickle.dump(modelo_km,open('modelo_km.sav','wb'))
#%% Cargar modelo guardado
modelo_km = pickle.load(open('modelo_km.sav','rb'))


#%% Función para buscar el polinomio optimo
def graf_reglog(X,Y,grados):
    modelo = linear_model.LogisticRegression()
    Accu = np.zeros(grados.shape)
    Prec = np.zeros(grados.shape)
    Reca = np.zeros(grados.shape)
    for ngrado in grados:
        poly = PolynomialFeatures(ngrado)
        Xa = poly.fit_transform(X)
        modelo.fit(Xa,Y)
        Yhat = modelo.predict(Xa)
        Accu[ngrado-1] = accuracy_score(Y,Yhat)
        Prec[ngrado-1] = precision_score(Y,Yhat)
        Reca[ngrado-1] = recall_score(Y,Yhat)
    
    plt.plot(grados,Accu)
    plt.plot(grados,Prec)
    plt.plot(grados,Reca)
    plt.xlabel('Grado Polinomio')
    plt.ylabel('% Aciertos')
    plt.grid()
    plt.show()
    return Accu,Prec,Reca

#%% Verificar si hay unos o ceros
grupos_validos = np.ones(np.unique(grupos).shape)*-1
for k in np.unique(grupos):
    if len(pd.value_counts(Ytrain[grupos==k]))>1:
        grupos_validos[k] = k

#%% Calcular las regresiones
for k in np.unique(grupos_validos):
    if k > 0:
        graf_reglog(Xtrain[grupos==k],
                    Ytrain[grupos==k],
                    np.arange(1,4))

#%% Funcion de grafica de codo por cluster
def graf_for_clusters(X,Y,grupos,grupos_validos):
    for g in grupos_validos:
        g = int(g)
        if g>-1:
            print('Grafica de grupo %s'%g)
            graf_reglog(X[grupos==g],Y[grupos==g],np.arange(1,3))

#%% Crear todas las graficas de codo de los clusters
graf_for_clusters(Xtrain,Ytrain,grupos,grupos_validos)

#%% Funcion para crear el modelo deseado
def crear_modelo(X,Y,ngrado):
    modelo = linear_model.LogisticRegression()
    poly = PolynomialFeatures(ngrado)
    Xa = poly.fit_transform(X)
    modelo.fit(Xa,Y)
    Yhat = modelo.predict(Xa)
    print(accuracy_score(Y,Yhat))
    print(precision_score(Y,Yhat))
    print(recall_score(Y,Yhat))
    return modelo,Yhat

#%% Crear los modelos por cada cluster
modelo_g0,Yhat0 = crear_modelo(Xtrain[grupos==0],Ytrain[grupos==0],2)
modelo_g1,Yhat1 = crear_modelo(Xtrain[grupos==1],Ytrain[grupos==1],2)
modelo_g2,Yhat2 = crear_modelo(Xtrain[grupos==2],Ytrain[grupos==2],2)
modelo_g3,Yhat3 = crear_modelo(Xtrain[grupos==3],Ytrain[grupos==3],1)
modelo_g4,Yhat4 = crear_modelo(Xtrain[grupos==4],Ytrain[grupos==4],2)
modelo_g5,Yhat5 = crear_modelo(Xtrain[grupos==5],Ytrain[grupos==5],2)
modelo_g6,Yhat6 = crear_modelo(Xtrain[grupos==6],Ytrain[grupos==6],2)

#%% Ensamble de modelos
Yhat_clustering_train = np.zeros(Ytrain.shape)
Yhat_clustering_train[grupos==0]=Yhat0
Yhat_clustering_train[grupos==1]=Yhat1
Yhat_clustering_train[grupos==2]=Yhat2
Yhat_clustering_train[grupos==3]=Yhat3
Yhat_clustering_train[grupos==4]=Yhat4
Yhat_clustering_train[grupos==5]=Yhat5
Yhat_clustering_train[grupos==6]=Yhat6

print(accuracy_score(Ytrain,Yhat_clustering_train))
print(precision_score(Ytrain,Yhat_clustering_train))
print(recall_score(Ytrain,Yhat_clustering_train))


































