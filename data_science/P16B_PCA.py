# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

#%% Importar los datos de digitos
digits = datasets.load_digits()

#%% Visualizar una muestra de las imagenes
ndig = 10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.imshow(digits.images[k],cmap=plt.cm.gray_r)
    plt.axis('off')
    plt.title('Digits: %i' % k)
plt.show()

#%% Aplicar el algoritmo PCA
data = digits.data
media = data.mean(axis=0)
data_m = data-media
M_cov = np.cov(data_m.transpose())
w,v = np.linalg.eig(M_cov)

#%% Proyectar los digitos en 1 dimension
componentes = w[0]
M_trans = np.reshape(v[:,0],(64,1))

data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))

#plt.scatter(data_new,0*data_new,c=digits.target)
plt.scatter(data_new,0*data_new,c=np.reshape(digits.target,(1797,1)))
plt.colorbar()
plt.grid()
plt.show()


#%% Proyectar los digitos en 2 dimensiones
componentes = w[0:2]
M_trans = v[:,0:2]

data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))

#plt.scatter(data_new,0*data_new,c=digits.target)
plt.scatter(data_new[:,0],data_new[:,1],c=digits.target)
plt.colorbar()
plt.grid()
plt.show()


#%% Proyectar los digitos en 3 dimensiones
componentes = w[0:3]
M_trans = v[:,0:3]

data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data_new[:,0],data_new[:,1],data_new[:,2],
           c=digits.target)

plt.grid()
plt.show()

#%% Criterio de reduccion de dimensiones
porcentaje = w/np.sum(w)
porcentaje_acum = np.cumsum(porcentaje)

plt.bar(np.arange(len(porcentaje)),porcentaje)
plt.show()
plt.bar(np.arange(len(porcentaje_acum)),porcentaje_acum)
plt.show()


#%% Aplicar criterio de la varianza para comparar
varianza = np.var(data,axis=0)
plt.bar(np.arange(len(varianza)),varianza)
plt.show()

#%% Seleccionar las variables o pixeles con mayor varianza
nivel_varianza = 5
idx = varianza>nivel_varianza

img_f = np.zeros((1,64))
img_f[0,idx] = 16
img_f = np.reshape(img_f,(8,8))
plt.imshow(img_f,cmap=plt.cm.gray_r)
plt.show()











