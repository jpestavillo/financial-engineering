# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

#%% Cargar los datos
digits = datasets.load_digits()
data = digits.data

#%% Visualizar una muestra de los digitos
ndig = 10
for k in np.arange(ndig):
    plt.subplot(2,ndig/2,k+1)
    plt.axis('off')
    plt.imshow(digits.images[k],cmap=plt.cm.gray_r)
    plt.title('Digit: %d' % k)
plt.show()

#%% Aplicando el PCA para comprimir la información
media = data.mean(axis=0)
datam = data - media
M_cov = np.cov(datam.transpose())
w,v = np.linalg.eig(M_cov)

#%% Proyectar todos los digitos en una sola variable
componentes = w[0]
M_trans = np.reshape(v[:,0],(64,1))

#transformar datos
data_new = np.array(np.matrix(datam)*np.matrix(M_trans))

plt.scatter(data_new,0*data_new,c=np.reshape(digits.target,(1797,1)))
plt.colorbar()
plt.grid()
plt.show()

#%% Proyectar todos los digitos en dos variables
componentes = w[0:2]
M_trans = v[:,0:2]

#transformar datos
data_new = np.array(np.matrix(datam)*np.matrix(M_trans))

plt.scatter(data_new[:,0],data_new[:,1],c=digits.target)
plt.colorbar()
plt.grid()
plt.show()

#%% Elegir el numero de dimensiones en que puedo comprimir la información
porcentaje = w/np.sum(w)
porcentaje_acum = np.cumsum(porcentaje)

plt.bar(np.arange(len(porcentaje)),porcentaje)
plt.show()
plt.bar(np.arange(len(porcentaje_acum)),porcentaje_acum)
plt.show()

#%% Criterio de la varianza para seleccionar variables

varianza = np.var(data,axis=0)
plt.bar(np.arange(len(varianza)),varianza)
plt.show()

# Seleccionar el nivel aceptable de varianza
nivel_var = 15
indx = varianza>nivel_var

#Crear una imagen ficticia solo ver el area seleccionada
img_cero = np.zeros((1,64))
img_cero[0,indx]=16
img_cero = np.reshape(img_cero,(8,8))

plt.imshow(img_cero,cmap=plt.cm.gray_r)
plt.show()













