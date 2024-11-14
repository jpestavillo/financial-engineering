import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy
import scipy.spatial.distance as sc
from sklearn.cluster import KMeans
#%% importamos datos 
data=pd.read_csv('../data/dataset_t4_1.csv')
#%% random seed
np.random.seed(seed=69)
semilla=69
#%% clustering using eucliean
Z= hierarchy.linkage(data,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z)
plt.show()
#%% decidiendo el numero en el cluster
inersias = np.zeros(20) # crea un arreglo de 10 espacios
for k in np.arange(20)+1:
    model = KMeans(n_clusters=k, random_state=semilla, init='random')
    model= model.fit(data)
    inersias[k-1]=model.inertia_
    
plt.plot(np.arange(1,21),inersias)
plt.xlabel('num grupos')
plt.ylabel('incercia global')
plt.show()
#%%
n_optimo=5
#%% clustering with kMeans 
model = KMeans(n_clusters=n_optimo, random_state=69, init='random') #Random la manera en que inicializan los centroides

model= model.fit(data) # fit ejecuta todo el algoritmo. El de las iteraciones.
centroides = model.cluster_centers_ ## Para ver donde están los centroides. Te da las coordenadas 
Ypredict = model.predict(data) #predict te dice que dato pertence a que grupo.
#El número de variables es el número de dimensiones
#?KMeans
plt.scatter(Z[:,0],Z[:,1], c= Ypredict)
plt.show()
J = model.inertia_ # Promedio de la distancia euclidiana.
#%% Criterio de desicioón el n´mero de clusters
inersias = np.zeros(10) # crea un arreglo de 10 espacios
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k, random_state=69, init='random')
    model= model.fit(data)
    inersias[k-1]=model.inertia_
    
plt.plot(np.arange(1,11),inersias)
plt.xlabel('num grupos')
plt.ylabel('incercia global')
plt.show()