# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:24:40 2018

@author: if709274
"""

"""seleccion de características
Criterio deVarianza
Eliminar variables con var menor var deseada 
Proponer var deseada
Dependencia a la escala de los datos 
Aplicarlo cuando escalas de las variables son comparables 
2 Criterio Correlacion 
Mantener al menos una d elas variables correlacionadas
Proponer correlacion umbral  (si tienes muchas variables con un rango de .8 a .9,
y te vas a quedar con 1)
PCA o analisis de componentes principales 
Proponer # dimensiones da proeyctar 2"""
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

#%% importar la imagen a analizar 
im=mpimg.imread('..\data\images.png')
plt.imshow(im)
plt.show()
#%% reordenar los datos 
d= im.shape
im_reordenada=np.reshape(im,(d[0]*d[1],d[2]))
#%% 
varianzas =np.var(im_reordenada,axis=0)
#%% convertir los datos a media cero
medias= im_reordenada.mean(axis=0)
im_m= im_reordenada-medias

#%% paso 1 matriz de covarianzas 
im_cov= np.cov(im_m.transpose())
#%% paso 2 y 3 Obtener los valores propios y vectores propios 
w,v= np.linalg.eig(im_cov)
#porcentaje=w/np.sum(w)
#%% paso 4. Reducir la dimension de los datos 
componentes= w[0:3]
M_Trans=v[:,0:3]

im_new= np.matrix(im_m)*np.matrix(M_Trans)
#%%
im_recuperada=np.matrix(im_new)*np.matrix(M_Trans.transpose())+medias
img_r=im.copy()
img_r[:,:,0]=im_recuperada[:,0].reshape((d[0],d[1]))
img_r[:,:,1]=im_recuperada[:,1].reshape((d[0],d[1]))
img_r[:,:,2]=im_recuperada[:,2].reshape((d[0],d[1]))
img_r[:,:,3]=im_recuperada[:,3].reshape((d[0],d[1]))

plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(img_r)