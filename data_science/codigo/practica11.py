import  numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
#%% Generar los datos para clasificarlos
semilla = 757
X, Y = make_blobs(n_samples=1000, random_state= semilla)
# make_blobs genera muchos puntos. El primer valor es el número de datos. El segundo es el valor donde empieza la aletoriedad.

plt.scatter(X[:,0],X[:,1])
plt.show()
#%%  Aplicar ek akgoritmo de K-means (Centroides)
## La cantidad de iteraciones pueden ser : Las que tu decidas, Si después que iteras ya no está cambiando paralo!, por tiempo.
model = KMeans(n_clusters=5, random_state=semilla, init='random') #Random la manera en que inicializan los centroides

model= model.fit(X) # fit ejecuta todo el algoritmo. El de las iteraciones.
centroides = model.cluster_centers_ ## Para ver donde están los centroides. Te da las coordenadas 
Ypredict = model.predict(X) #predict te dice que dato pertence a que grupo.

#El número de variables es el número de dimensiones
#?KMeans
plt.scatter(X[:,0],X[:,1], c= Ypredict)
plt.plot(centroides[:,0] , centroides[:,1], 'x') # Te va a dibujar una x en el centroide
plt.show()

J = model.inertia_ # Promedio de la distancia euclidiana.
#%% Criterio de desicioón el n´mero de clusters
inersias = np.zeros(10) # crea un arreglo de 10 espacios
for k in np.arange(10)+1:
    model = KMeans(n_clusters=k, random_state=semilla, init='random')
    model= model.fit(X)
    inersias[k-1]=model.inertia_
    
plt.plot(np.arange(1,11),inersias)
plt.xlabel('num grupos')
plt.ylabel('incercia global')
plt.show()
