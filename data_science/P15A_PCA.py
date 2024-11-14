# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:37:53 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#%% Importar la imagen a analizar
#im = mpimg.imread('..\Data\indice.png')
im = mpimg.imread('..\Data\images.png')
plt.imshow(im)
plt.show()

#%% Reordenar los datos
d = im.shape
im_reordenada = np.reshape(im,(d[0]*d[1],d[2]))
#im_reordenada = np.reshape(im,(209*241,4))

#%% Criterio de varianza
varianzas = np.var(im_reordenada,axis=0)

#%% Convertir los datos a media cero
medias = im_reordenada.mean(axis=0)
im_m = im_reordenada-medias

#%% Paso 1. Matriz de covarianzas
im_cov = np.cov(im_m.transpose())

#%% Paso 2 y 3. Obtener los valores propios y vectores propios
w,v = np.linalg.eig(im_cov)

porcentaje = w/np.sum(w)

#%%Paso 4. Reducir la dimension de los datos
componentes = w[0:1]
M_trans = v[:,0:1]

im_new = np.matrix(im_m)*np.matrix(M_trans)


#%% Recuperar los datos y volverlos a graficar para comparar
im_recuperada = np.matrix(im_new)*np.matrix(M_trans.transpose())+medias

img_r = im.copy()
img_r[:,:,0] = im_recuperada[:,0].reshape((d[0],d[1]))
img_r[:,:,1] = im_recuperada[:,1].reshape((d[0],d[1]))
img_r[:,:,2] = im_recuperada[:,2].reshape((d[0],d[1]))
img_r[:,:,3] = im_recuperada[:,3].reshape((d[0],d[1]))

plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(img_r)












