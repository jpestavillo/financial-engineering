# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:11:04 2018

@author: riemannruiz
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#%% Importar la imagen
#img = mpimg.imread('..\Data\indice.png')
img = mpimg.imread('..\Data\images.png')
plt.imshow(img)


#%% Reordenar la imagen en una sola tabla
d = img.shape
img_col = np.reshape(img,(d[0]*d[1],d[2]))
#img_col = np.reshape(img,(209*241 , 4))


#%% Convertir los datos a media 0
medias = img_col.mean(axis=0)
img_m = img_col-medias

img_cov = np.cov(img_m.transpose())

w,v = np.linalg.eig(img_cov)


porcentaje = w/np.sum(w)

#%% Reducir la dimension de los datos
componentes = w[0:1]
M_trans = v[:,0:1]

img_new = np.matrix(img_m)*np.matrix(M_trans)

#%% Recuperar la imagen y compararla con la original
img_recuperada = np.matrix(img_new)*np.matrix(M_trans.transpose())
img_recuperada = img_recuperada+medias

img_r = img.copy()
img_r[:,:,0] = img_recuperada[:,0].reshape((d[0],d[1]))
img_r[:,:,1] = img_recuperada[:,1].reshape((d[0],d[1]))
img_r[:,:,2] = img_recuperada[:,2].reshape((d[0],d[1]))
img_r[:,:,3] = img_recuperada[:,3].reshape((d[0],d[1]))
img_r[img_r<0]=0

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_r)













