from mylib import mylib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
from sklearn.cluster import KMeans 
#%%
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
#%%
datao=pd.read_csv('../data/Kaggle_Training_Dataset.csv')
#%%
data=data.dropna()   #quitamos los renglones que tenian valores faltantes. #%%
#%%
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     

data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
#%%
dqr=mylib.dqr(data)
#%% comprimir con PCA la información
media = data.mean(axis=0)
datam =  data-media
M_cov = np.cov(datam.transpose())
w,v = np.linalg.eig(M_cov)

#%% proyectar todos los digitos en una sola variable 
componentes = w[0:3]
M_trans = np.reshape(v[:,0:3],(22,3))
#transformar datos
data_new = np.array(np.matrix(datam)*np.matrix(M_trans))

plt.scatter(data_new,0*data_new,c=np.reshape(data_new,(1591716,3)))
plt.colorbar()
plt.grid()
plt.show()
#%% elegir el # de dimensiones en que puedo comprimir la info
porcentaje = w/np.sum(w)
porcentaje_acum = np.cumsum(porcentaje)

plt.bar(np.arange(len(porcentaje)),porcentaje)
plt.show()


plt.bar(np.arange(len(porcentaje_acum)),porcentaje_acum)
plt.show()
#%% normalizamos los datos comprimidos
datanorm = (data_new-data_new.mean())/data_new.std()

""" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77"""
#%%
datanorm=data_new.iloc[0:1000,:]
#datanorm=(datanorm-datanorm.mean())/datanorm.std()
Z= hierarchy.linkage(datanorm,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()

inercias = np.zeros(10)
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k,init = 'random')
    model = model.fit(datanorm)
    inercias[k-1] = model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.title('KMeans')
plt.xlabel('Num de grupos')
plt.ylabel('Inercia global')
plt.show()