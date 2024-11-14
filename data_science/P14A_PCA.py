# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Datos Originales
data = np.array([[2.5,2.4],
                 [0.5,0.7],
                 [2.2,2.9],
                 [1.9,2.2],
                 [3.1,3.0],
                 [1.8,2.1],
                 [1.0,1.1],
                 [1.5,1.6],
                 [1.1,0.9],
                 [4.0,4.1]])

plt.scatter(data[:,0],data[:,1])
plt.grid()
plt.show()


#%% Convertir los datos a un conjunto con media 0
medias = data.mean(axis=0)
data_m = data-medias
plt.scatter(data_m[:,0],data_m[:,1])
plt.grid()
plt.show()

#%% Paso 1. Calcular la matriz de covarianzas del conjunto de datos
data_cov = np.cov(data_m.transpose())

#%% Paso 2 y Paso 3. calcular vectores y valores propios
w,v = np.linalg.eig(data_cov)


#%% Dibujar los vectores propios como direcciones
x = np.arange(-1.5,2,0.1)
plt.scatter(data_m[:,0],data_m[:,1])
plt.plot(x,(v[1,0]/v[0,0])*x,'b--')
plt.plot(x,(v[1,1]/v[0,1])*x,'g--')
plt.axis('square')
plt.show()

#%% Paso 4. Seleccionar la matriz de transformación
M_trans = v[:,[1,0]]
componentes = w[[1,0]]

# Transformar los datos a los nuevos ejes
data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))

plt.scatter(data_new[:,0],data_new[:,1])
plt.hlines(0,-3,2,'g')
plt.vlines(0,-0.5,0.5,'b')
plt.grid()
plt.show()

#%% Comprimir los datos o reducir la dimension de los datos
componentes = w[1]
M_trans = v[:,1]
M_trans = np.reshape(M_trans,[2,1])

data_new = np.matrix(data_m)*np.matrix(M_trans)

data_r = np.array(np.matrix(data_new)*np.matrix(M_trans.transpose()))

plt.scatter(data_r[:,0],data_r[:,1])
plt.grid()
plt.show()


















