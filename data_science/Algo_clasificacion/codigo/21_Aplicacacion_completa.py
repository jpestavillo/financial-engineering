import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score)
import pickle # Nos sirve para evitar correr nuestro código y que tarde mucho
#%%  Importar los datos
data = pd.read_csv('../DATA/creditcard.csv')

X= data.iloc[:,1:30]
Y= data.iloc[:,30]
del data
#%% Normalizar el amount 
X['Amount']=(X['Amount']-X['Amount'].mean())/X['Amount'].std()

fraudes= pd.value_counts(Y)/len(Y) # Menos del 1% fue fraude
#%% Seleccionar la base de trains y test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.5,
                                                    random_state=0) #Le dices que quieres partir en el argumento y de que tamaño
# Por dafault el test_size tiene 0.25

del X,Y
#%% Regresión logística (REVISAR EL POLINOMIO OPTIMO)
modelo_rl = linear_model.LogisticRegression()
grados = np.arange(1,3)
Accu = np.zeros(grados.shape)
Prec = np.zeros(grados.shape)
Reca = np.zeros(grados.shape)
Nvar = np.zeros(grados.shape)
#%% Entrenar memoria
for ngrado in grados:
    poly = PolynomialFeatures(ngrado)
    Xa  = poly.fit_transform(X_train)
    modelo_rl.fit(Xa, Y_train)
    Yhat = modelo_rl.predict(Xa)
    Accu[ngrado-1] =accuracy_score(Y_train, Yhat)
    Prec[ngrado-1]= precision_score(Y_train, Yhat)
    Reca[ngrado-1] = recall_score(Y_train,Yhat)
    Nvar[ngrado-1] = len(modelo_rl.coef_[0])
#%% Gráficar información 

plt.plot(grados, Accu)
plt.plot(grados, Prec)
plt.plot(grados, Reca)
plt.xlabel('Grado el polinomio')
plt.ylabel('% Aciertos')
plt.legend(('Accuracy','Precision','Recall'), loc='best')
plt.grid()
plt.show()
#%% Modelo definitivo 
#EL grado 2 es óptimo porque los criterios que lo miden son bastante buenos en ese grado
ngrado= 2
poly = PolynomialFeatures(ngrado)
Xa_train = poly.fit_transform(X_train)
modelo_rl= linear_model.LogisticRegression()
modelo_rl = modelo_rl.fit(Xa_train, Y_train)
Yhat_rl_train = modelo_rl.predict(Xa_train)

print(accuracy_score(Y_train, Yhat_rl_train))
print(precision_score(Y_train, Yhat_rl_train))
print(recall_score(Y_train, Yhat_rl_train))
#%%  Probar el modelo en los datos desconocidos
Xa_test= poly.fit_transform(X_test)
Ythat_rl_test= modelo_rl.predict(Xa_test)
print(accuracy_score(Y_test,Ythat_rl_test))
print(precision_score(Y_test,Ythat_rl_test))
print(recall_score(Y_test,Ythat_rl_test))
#%% Resolver el mismo problema con SVM (vector soporte)
modelo_sv= svm.SVC(kernel='rbf')
modelo_sv.fit(X_train,Y_train)
Yhat_sv_train= modelo_sv.predict(X_train)

print(accuracy_score(Y_train, Yhat_sv_train))
print(precision_score(Y_train, Yhat_sv_train))
print(recall_score(Y_train, Yhat_sv_train))

#%% Ahora calamos el modelo SVM pero con el test osea datos desconocidos

Ythat_sv_test= modelo_sv.predict(X_test)
#%%
print(accuracy_score(Y_test,Ythat_sv_test))
print(precision_score(Y_test,Ythat_sv_test))
print(recall_score(Y_test,Ythat_sv_test))

#%% Guardar los modelos resultantes
pickle.dump(modelo_rl,open('modelo_rl.sav','wb'))
#%% Para cargarlo
modelo_rl= pickle.load(open('modelo_rl.sav','rb'))

#%% APLICAR EL CLUSTERING PARA OBTENER PERFILES DE CREDITO
inercias= np.zeros(10)
for k in np.arange(10)+1:
    modelo_KM= KMeans(n_clusters=k, init='k-means++')
    modelo_KN= modelo_KM.fit(X_train)
    inercias[k-1] = modelo_KM.inertia_
plt.plot(np.arange(1,11), inercias) #Aquí debemos ve gráfica de codo
plt.xlabel('Num de Grupos')
plt.ylabel('Inercias')
plt.show()
#%% crear función
""" Fueron 3 grupos, por lo tanto, haremos el mismo proceso 
3 veces"""
def graf_reglog(X,Y,grados):
    modelo_rl = linear_model.LogisticRegression()
    Accu = np.zeros(grados.shape)
    Prec = np.zeros(grados.shape)
    Reca = np.zeros(grados.shape)
    Nvar = np.zeros(grados.shape)
    for ngrado in grados:
        poly = PolynomialFeatures(ngrado)
        Xa  = poly.fit_transform(X)
        modelo_rl.fit(Xa, Y)
        Yhat = modelo_rl.predict(Xa)
        Accu[ngrado-1] =accuracy_score(Y, Yhat)
        Prec[ngrado-1]= precision_score(Y, Yhat)
        Reca[ngrado-1] = recall_score(Y,Yhat)
        Nvar[ngrado-1] = len(modelo_rl.coef_[0])
    plt.plot(grados, Accu)
    plt.plot(grados, Prec)
    plt.plot(grados, Reca)
    plt.xlabel('Grado el polinomio')
    plt.ylabel('% Aciertos')
    plt.legend(('Accuracy','Precision','Recall'), loc='best')
    plt.grid()
    plt.show()
    return Accu, Prec, Reca, grados
#%% saber que datos pertenecen a cada grupo
modelo_KM =KMeans(n_clusters = 3, init='k-means++')
modelo_KM = modelo_KM.fit(X_train)
grupos = modelo_KM.predict(X_train)
#%% Obtener los modelos por grupo 
graf_reglog(X_train[grupos==0], Y_train[grupos==0], np.arange(1,3)) # Te regresa los índices de los que tienen 0
contar_Datos = pd.value_counts(graf_reglog)
#%% Grupo 1
graf_reglog(X_train[grupos==1], Y_train[grupos==1], np.arange(1,3)) # Te regresa los índices de los que tienen 0
contar_Datos = pd.value_counts(graf_reglog)
#%% Grupo 2
graf_reglog(X_train[grupos==2], Y_train[grupos==2], np.arange(1,3)) # Te regresa los índices de los que tienen 0
contar_Datos = pd.value_counts(graf_reglog)


""" Para los 3 con un grado dos se logra por encima del 90"""
#%% Habiendo decidido creamos el modelo definitivo para cda grupo 
ngrado = 2
poly = PolynomialFeatures(ngrado)
Xa= poly.fit_transform(X_train)

modelo_rl_g0 = linear_model.LogisticRegression()
modelo_rl_g0.fit(Xa[grupos==0], Y_train[grupos==0])


modelo_rl_g1 = linear_model.LogisticRegression()
modelo_rl_g1.fit(Xa[grupos==1], Y_train[grupos==1])

modelo_rl_g2 = linear_model.LogisticRegression()
modelo_rl_g2.fit(Xa[grupos==2], Y_train[grupos==2])
#%% Aplicar el modelo resultante del clustering

Yhat_g0 = modelo_rl_g0.predict(Xa[grupos==0])
Yhat_g1 = modelo_rl_g1.predict(Xa[grupos==1])
Yhat_g2 = modelo_rl_g2.predict(Xa[grupos==2])
Yhat_total = np.zeros(Y_train.shape)
Yhat_total[grupos==0] = Yhat_g0
Yhat_total[grupos==1] = Yhat_g1
Yhat_total[grupos==2] = Yhat_g2
#%%
print(accuracy_score(Y_test,Yhat_total))
print(precision_score(Y_test,Yhat_total))
print(recall_score(Y_test,Yhat_total))

#%% Probar los 3 modelos a la base de prueba
ngrado = 2
poly = PolynomialFeatures(ngrado)
Xa = poly.fit_transform(X_test)
grupos = modelo_KM.predict(X_test)

Yhat_g0 = modelo_rl_g0.predict(Xa[grupos==0])
Yhat_g1 = modelo_rl_g1.predict(Xa[grupos==1])
Yhat_g2 = modelo_rl_g2.predict(Xa[grupos==2])
Yhat_total = np.zeros(Y_test.shape)
Yhat_total[grupos==0] = Yhat_g0
Yhat_total[grupos==1] = Yhat_g1
Yhat_total[grupos==2] = Yhat_g2
print(accuracy_score(Y_test,Yhat_total))
print(precision_score(Y_test,Yhat_total))
print(recall_score(Y_test,Yhat_total))







""" Primer modelo regresión logisitca, segundo seleccionar varibales más importantes con varianza etc y hacer regresion 
logistica, 3 y 4 optimización de los dos primeros  y el 5 es SVM"""
## CONCLUSIONES ESPERADAS ES COMPARAR LOS RESULTADOS ESPERADOS Y CUÁL ES MÁS RÁPIDO 
# Y SI QUEREMOS IR MÁS ALLÁ HAHGAMOS LO QUE HICIMOS EN ESTA CLASE