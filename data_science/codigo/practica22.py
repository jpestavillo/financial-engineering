
"""
diseño de entrenamiento  
para diseñar tu entrenamiento tienes que quitar parte de los datos que ya conoces para que le modelo los modele. 
la forma en la que esto se divide es   de 80-20%  o  75%-25%  

"""


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures 
from sklearn import svm
from sklearn.cluster import KMeans 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,precision_score,recall_score)
import pickle
#%%
data=pd.read_csv('../data/creditcard.csv')
X= data.iloc[:,1:30]
Y= data.iloc[:,30]
del data 
#%% 
data_norm=X['Amount']-X['Amount'].mean()
data_norm=data_norm/X['Amount'].std()
#%%
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.5,
                                                random_state=0)
del X,Y
#%%
modelo_rl=linear_model.LogisticRegression()
grados= np.arange(1,3)
Accu=np.zeros(grados.shape)
Prec=np.zeros(grados.shape)
Reca=np.zeros(grados.shape)
Nvar=np.zeros(grados.shape)

for ngrado in grados:
    poly=PolynomialFeatures(ngrado)
    Xa=poly.fit_transform(X_train)
    modelo_rl.fit(Xa,Y_train)
    Yhat=modelo_rl.predict(Xa)
    Accu[ngrado-1]=accuracy_score(Y_train,Yhat)
    Prec[ngrado-1]=precision_score(Y_train,Yhat)
    Reca[ngrado-1]=recall_score(Y_train,Yhat)
    Nvar[ngrado-1]=len(modelo_rl.coef_[0])
#%%
plt.plot(grados,Accu)
plt.plot(grados,Prec)
plt.plot(grados,Reca)
plt.xlabel('Grado el polinomio')
plt.ylabel('aciertos')
plt.legend('Accuracy','Recall') #mejor localizacion de la grafica
plt.grid()
plt.show()
#%%
ngrado=2
poly=PolynomialFeatures(ngrado)
Xa_train=poly.fit_transform(X_train)
modelo_rl=linear_model.LogisticRegression()
modelo_rl=modelo_rl.fit(Xa_train,Y_train)
Yhat_rl_train=modelo_rl.predict(Xa_train)

accuracy_score(Y_train,Yhat_rl_train)
precision_score(Y_train,Yhat_rl_train)
recall_score(Y_train,Yhat_rl_train)
#%%
Xa_test=poly.fit_transform(X_test)
yhat_rl_train=modelo_rl.predict(Xa_test)
                                                         # esta parte no sirve 
print(accuracy_score(Y_train,yhat_rl_train))
print(precision_score(Y_train,yhat_rl_train))
print(recall_score(Y_train,yhat_rl_train))
#%%
Xa_test=poly.fit_transform(X_test)
Yhat_rl_test=modelo_rl.predict(Xa_test)

print(accuracy_score(Y_test,Yhat_rl_test))
print(precision_score(Y_test,Yhat_rl_test))
print(recall_score(Y_test,Yhat_rl_test))
#%%
modelo_sv=svm.SVC(kernel='rbf')
modelo_sv.fit(X_train,Y_train)
Yhat_sv_train=modelo_sv.predict(X_train)

print(accuracy_score(Y_train,Yhat_sv_train))
print(precision_score(Y_train,Yhat_sv_train))
print(recall_score(Y_train,Yhat_sv_train))
#%%
Yhat_sv_test=modelo_sv.predict(X_test)

print(accuracy_score(Y_test,Yhat_sv_test))
print(precision_score(Y_test,Yhat_sv_test))
print(recall_score(Y_test,Yhat_sv_test))
#%% guardar el modelo
pickle.dump(modelo_rl,open('modelo_rl.sav','wb')) #con esto guardas tu modelo  (wb es permiso de escritura )
#%% dias despues lo cargamos 
modelo_rl=pickle.load(open('modelo_rl.sav','rb'))
#%% aplicar el clustering para obtener perfiles 
inercias= np.zeros(10)
#kMeans es el mas rapido
for k in np.arange(10)+1:
    modelo_KM=KMeans(n_clusters=k,init='k-means++')  # kmeans++ es para iniciar los cluster pero muy alejados de los datos 
    modelo_KM=modelo_KM.fit(X_train)
    inercias[k-1]=modelo_KM.inertia_

plt.plot(np.arange(1,11),inercias)
plt.xlabel('Numero de grupos')
plt.ylabel('inercia')
plt.show()

#%% repetimos el proceso 
def graf_reglog(X,Y,grados):
    modelo_rl=linear_model.LogisticRegression()
   
    Accu=np.zeros(grados.shape)
    Prec=np.zeros(grados.shape)
    Reca=np.zeros(grados.shape)
    Nvar=np.zeros(grados.shape)
    
    for ngrado in grados:
        poly=PolynomialFeatures(ngrado)
        Xa=poly.fit_transform(X)
        modelo_rl.fit(Xa,Y)
        Yhat=modelo_rl.predict(Xa)
        Accu[ngrado-1]=accuracy_score(Y,Yhat)
        Prec[ngrado-1]=precision_score(Y,Yhat)
        Reca[ngrado-1]=recall_score(Y,Yhat)
        Nvar[ngrado-1]=len(modelo_rl.coef_[0])

    plt.plot(grados,Accu)
    plt.plot(grados,Prec)
    plt.plot(grados,Reca)
    plt.xlabel('Grado el polinomio')
    plt.ylabel('%aciertos')
    plt.legend(('Accuracy','Precision','Recall'),loc='Best') #mejor localizacion de la grafica
    plt.grid()
    plt.show()
    
    return grados,Accu,Prec,Reca
#%% 
modelo_KM= KMeans(n_clusters=3, init='k-means++')
modelo_KM= modelo_KM.fit(X_train)
grupos=modelo_KM.predict(X_train)
#%% obtener los modelos por grupo
graf_reglog(X_train[grupos==0],Y_train[grupos==0],np.arange(1,3))
graf_reglog(X_train[grupos==1],Y_train[grupos==1],np.arange(1,3))
graf_reglog(X_train[grupos==2],Y_train[grupos==2],np.arange(1,3))


#%% habiendo decidio, creamos el modelo definitivo para cada grupo 
ngrado=2
poly=PolynomialFeatures(ngrado)
Xa=poly.fit_transform(X_train)
modelo_rl_g0=linear_model.LogisticRegression()
modelo_rl_g0.fit(Xa[grupos==0],Y_train[grupos==0])
modelo_rl_g0=linear_model.LogisticRegression()
modelo_rl_g0.fit(Xa[grupos==1],Y_train[grupos==1])
modelo_rl_g0=linear_model.LogisticRegression()
modelo_rl_g0.fit(Xa[grupos==2],Y_train[grupos==2])

#%% APLICAR EL MODELO RESULTANTE DEL CLUSTERING
Yhat_g0=modelo_rl_g0.predict(Xa[grupos==0])
Yhat_g1=modelo_rl_g0.predict(Xa[grupos==1])
Yhat_g2=modelo_rl_g0.predict(Xa[grupos==2])
Yhat_total=np.zeros(Y_train.shape)
Yhat_total[grupos==0]=Yhat_g0
Yhat_total[grupos==1]=Yhat_g1
Yhat_total[grupos==2]=Yhat_g2

print(accuracy_score(Y_train,Yhat_total))
print(precision_score(Y_train,Yhat_total))
print(recall_score(Y_train,Yhat_total))