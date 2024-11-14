from mylib import mylib
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score)
import pickle # Nos sirve para evitar correr nuestro código y que tarde mucho
import matplotlib.pyplot as plt
#%% CARGAR DATA
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
data=data.dropna()
#%% Definir función
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     
data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
#%% Quitar los Nan's
data.lead_time[data.lead_time.isnull()]=0
#%%
X = data.iloc[:,:21]
X= (X-X.mean(axis=0))/X.std(axis=0)
Y= pd.DataFrame(data['went_on_backorder'])
del data
#%% Limpieza de Datos
dqr=mylib.dqr(X)
#%%
devoluciones=np.sum(Y)/len(Y) # Menos del 1% fue devoluciones
#%% Partir la base para hacer el análisis con una X y Y de entrenamiento y después
#proceder con la X y Y test
#Seleccionar la base de trains y test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25,
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
    Prec[ngrado-1]= precision_score(Y_train, Yhat,average='micro')
    Reca[ngrado-1] = recall_score(Y_train,Yhat, Yhat,average='micro')
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
#%% Grado óptimo
ngrado= 1
poly = PolynomialFeatures(ngrado)
Xa_train = poly.fit_transform(X_train)
modelo_rl= linear_model.LogisticRegression()
modelo_rl = modelo_rl.fit(Xa_train, Y_train)
Yhat_rl_train = modelo_rl.predict(Xa_train)

accuracy2=accuracy_score(Y_train, Yhat_rl_train)
precision2=precision_score(Y_train, Yhat_rl_train,average='micro')
recall2=recall_score(Y_train, Yhat_rl_train,average='micro')
resultss= pd.DataFrame(columns=['Accuracy','Precision','Recall'],index=['Method'])
resultss.loc['Method']=[accuracy2,precision2,recall2]
#%% Aplicarselo a toda la base
#%% CARGAR DATA
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
#%% Definir función
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     
data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
#%% Cambiar los Nan's por 0
data.lead_time[data.lead_time.isnull()]=0
#%%
X = data.iloc[:,:21]
X= (X-X.mean(axis=0))/X.std(axis=0)
Y= pd.DataFrame(data['went_on_backorder'])
del data
#%% Grado óptimo con la base completa
ngrado= 1
poly = PolynomialFeatures(ngrado)
Xa_definitive = poly.fit_transform(X)
modelo_rl= linear_model.LogisticRegression()
modelo_rl = modelo_rl.fit(Xa_definitive, Y)

Yhat_rl_definitive = modelo_rl.predict(Xa_definitive)
#%%
accuracy3=accuracy_score(Y, Yhat_rl_definitive)
precision3=precision_score(Y, Yhat_rl_definitive,average='micro')
recall3=recall_score(Y, Yhat_rl_definitive,average='micro')
resultsss= pd.DataFrame(columns=['Accuracy','Precision','Recall'],index=['Method'])
resultsss.loc['Method']=[accuracy3,precision3,recall3]
#%%
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
data=data.dropna()
#%%
from sklearn import svm
y=Y
x=X
modelo =svm.SVC(kernel='linear')
modelo.fit(x_norm,y)
yhat = modelo.predict(x_norm)

print(accuracy_score(y,yhat))
print(precision_score(y,yhat, average=None))
print(recall_score(y,yhat, average=None))
