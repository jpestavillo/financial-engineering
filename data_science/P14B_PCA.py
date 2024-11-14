# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:10:16 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Datos originales generados
data = np.array([[2.5,2.4],
                 [0.5,0.6],
                 [3.0,3.1],
                 [2.5,2.2],
                 [1.5,1.2],
                 [0.2,0.4],
                 [4.5,4.7],
                 [1.7,1.2],
                 [3.7,3.8],
                 [2.1,1.9]])

plt.scatter(data[:,0],data[:,1])
plt.grid()
plt.show()

#%% Convertir los datos a un conjunto de media 0
medias = data.mean(axis=0)
data_m = data-medias

plt.scatter(data_m[:,0],data_m[:,1])
plt.grid()
plt.show()

#%% Paso 1. Obtener la matriz de covarianzas
data_cov = np.cov(data_m.transpose())

#%% Paso 2. Obtener valores y vectores propios
w,v = np.linalg.eig(data_cov)

#%% Visualizar las direcciones de los vectores propios
x = np.arange(-2,3,0.1)
plt.scatter(data_m[:,0],data_m[:,1])
plt.plot(x,(v[1,0]/v[0,0])*x,'b--')
plt.plot(x,(v[1,1]/v[0,1])*x,'g--')
plt.axis('square')
plt.grid()
plt.show()


#%% Paso 3. Transformación de los datos los nuevos ejes
componentes = w[[1,0]]
M_trans = v[:,[1,0]]

data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))


plt.subplot(121)
plt.scatter(data_m[:,0],data_m[:,1])
plt.plot(x,(v[1,0]/v[0,0])*x,'b--')
plt.plot(x,(v[1,1]/v[0,1])*x,'g--')
plt.axis('square')
plt.grid()

plt.subplot(122)
plt.scatter(data_new[:,0],data_new[:,1])
plt.hlines(0,-3,3,'g')
plt.vlines(0,-3,3,'b')
plt.grid()
plt.show()

#%% Reduciendo la dimensionde los datos
componentes = w[1]
M_trans = np.reshape(v[:,1],[2,1])

data_new = np.array(np.matrix(data_m)*np.matrix(M_trans))

#%% Recuperar infromación inicial
data_r = np.array(np.matrix(data_new)*np.matrix(M_trans.transpose()))

plt.scatter(data_r[:,0],data_r[:,1])
plt.grid()
plt.show()











