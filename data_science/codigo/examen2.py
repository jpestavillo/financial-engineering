# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:39:20 2018

@author: juanp
"""
import pandas as pd
import numpy as np 
from  scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs 
data=pd.read_csv('../data/ex2c_1_4.csv')
data=data.iloc[:,1:]
data=(data-data.mean(axis=0))/data.std(axis=0)
data_norm=data
semilla=69
#%% hierarchy 


Z= hierarchy.linkage(data,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
#%% decidiendo el numero en el cluster
inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init = 'random')
    model = model.fit(data_norm)
    inercias[k-1] = model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.title('KMeans')
plt.xlabel('Num de grupos')
plt.ylabel('Inercia global')
plt.show()
#%%
last = Z[-15:,2]
last_rev = last[::-1] #reordena al reves los valores (todas las filas, t columans,-1 al reves)
idx = np.arange(1,len(last_rev)+1)

plt.plot(idx,last_rev)
plt.title('Gráfica ')
plt.xlabel('Num de grupos')
plt.ylabel('Distancia o similaridad')
plt.grid()
plt.show()
#%% segunda pregunta 
data2=pd.read_csv('../data/ex2c_2_2.csv')
data2=data2.iloc[:,1:]
d= data.shape
medias=data2.mean(axis=0)
data_m=data2-medias
data_m=np.array(data_m)
plt.scatter(data_m[:,0],data_m[:,1])
plt.grid()
plt.show()
#paso 1 
data_cov=np.cov(data_m.transpose())  #transpose es porque quieres sacar varianza de las columnas 

#%% paso 2 y paso 3 Calcular vectores y valores propios 
w,v=np.linalg.eig(data_cov)
componentes= w[0]
M_trans= np.reshape(v[:,0],(3,1))
data_new= np.array(np.matrix(data_m)*np.matrix(M_trans))
data_new=np.array(data_new)
data2=np.array(data2)
plt.scatter(data_new,0*data_new,c=np.reshape(data_new,(2000,1)))
plt.colorbar()
plt.grid()
plt.show()


#%% 3
data3=pd.read_csv('../data/enfermedades.csv',index_col='nombre')
medias=data3.mean(axis=0)
data_m=data3-medias
data_m=np.array(data_m)
plt.scatter(data_m[:,0],data_m[:,1])
plt.grid()
plt.show()
data_cov=np.cov(data_m.transpose())  #transpose es porque quieres sacar varianza de las columnas 
w,v=np.linalg.eig(data_cov)
#%% paso 2 y paso 3 Calcular vectores y valores propios 
w,v=np.linalg.eig(data_cov)
#%% 4 
data4=pd.read_csv('../data/ex2c_4.csv')
data4=data4.iloc[:,1:]
data4_norm=(data4-data4.mean(axis=0))/data4.std(axis=0)
Z= hierarchy.linkage(data4,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init = 'random')
    model = model.fit(data4_norm)
    inercias[k-1] = model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.title('KMeans')
plt.xlabel('Num de grupos')
plt.ylabel('Inercia global')
plt.show()
#%% 4b 
d= data4.shape
medias=data4.mean(axis=0)
data_m=data4-medias
data_m=np.array(data_m)
plt.scatter(data_m[:,0],data_m[:,1])
plt.grid()
plt.show()
#paso 1 
data_cov=np.cov(data_m.transpose())  #transpose es porque quieres sacar varianza de las columnas 
 
w,v=np.linalg.eig(data_cov)
componentes= w[0]
M_trans= np.reshape(v[:,0],(4,1))
data_new= np.array(np.matrix(data_m)*np.matrix(M_trans))
data_new=np.array(data_new)
data2=np.array(data2)
plt.scatter(data_new,0*data_new,c=np.reshape(data_new,(150,1)))
plt.colorbar()
plt.grid()
plt.show()
porcentaje=w/np.sum(w)
plt.bar(np.arange(len(porcentaje)),porcentaje)
plt.show()
porcentaje_acum=np.cumsum(porcentaje)
plt.bar(np.arange(len(porcentaje_acum)),porcentaje_acum)
plt.show()
#%%
Z= hierarchy.linkage(data_new,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init = 'random')
    model = model.fit(data_new)
    inercias[k-1] = model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.title('KMeans')
plt.xlabel('Num de grupos')
plt.ylabel('Inercia global')
plt.show()