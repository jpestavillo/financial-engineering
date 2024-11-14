from mylib import mylib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
from sklearn.cluster import KMeans 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score)
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
#%% Cargar Datos y definir funuciones 
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
data=data.dropna()
datao=data[::]
data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
#%%
data= data.apply(replace_text,args=(0.0,int(0))).apply(replace_text,args=(1.0,int(1)))
#%% Tomar nuestra base
class1= data.iloc[:,-1]
data = data.iloc[:,:-1]
#%% comprimir con PCA la información


plt.scatter(data_new,0*data_new,c=np.reshape(data_new,(len(data),14)))
plt.colorbar()
plt.grid()
plt.show()
#%% elegir el # de dimensiones en que puedo comprimir la info
plt.bar(np.arange(len(porcentaje)),porcentaje)
plt.show()


plt.bar(np.arange(len(porcentaje_acum)),porcentaje_acum)
plt.show()
#%% normalizamos los datos comprimidos y procedemos a realizar la regresión logística
# con las variables seleccionadas
datanorm = (data_new-data_new.mean())/data_new.std()
#%%
X =data_new
Y= class1
#%% Partir la base para hacer el análisis con una X y Y de entrenamiento y después
#proceder con la X y Y test
#Seleccionar la base de trains y test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.05,
                                                    random_state=0) #Le dices que quieres partir en el argumento y de que tamaño
# Por dafault el test_size tiene 0.25

del X,Y
#%% Regresión logística (REVISAR EL POLINOMIO OPTIMO)
modelo_rl = linear_model.LogisticRegression()
grados = np.arange(1,4)
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
ngrado= 2
poly = PolynomialFeatures(ngrado)
Xa_train = poly.fit_transform(X_train)
modelo_rl= linear_model.LogisticRegression()
modelo_rl = modelo_rl.fit(Xa_train, Y_train)
Yhat_rl_train = modelo_rl.predict(Xa_train)
#%% Midiendo 
accuracy2=accuracy_score(Y_train, Yhat_rl_train)
precision2=precision_score(Y_train, Yhat_rl_train)
recall2=recall_score(Y_train, Yhat_rl_train)
#%%
resultss= pd.DataFrame(columns=['Accuracy','Precision','Recall'],index=['Method'])
resultss.loc['Method']=[accuracy2,precision2,recall2]