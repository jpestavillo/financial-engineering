# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:50:25 2017

@author: juanp
"""
import numpy as np
import matplotlib.pyplot as plt
import random
puntos=1000


juegopts=np.zeros((4,4))
juegocaos=np.zeros((puntos,4))


ax=2
ay=0
bx=3
by=1
cx=4
cy=0
dx=3
dy=-1

juegocaos[0,0]=ax
juegocaos[0,1]=ay
puntosderecha=1
puntosizquierda=0


for i in range (1,puntos):
    aleatorio=random.randrange(1,4)
    
    if aleatorio==1:
        juegocaos[i,0]=(juegocaos[i-1,0]+ax)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+ay)/2
        juegocaos[i,2]=1
    elif aleatorio==2:
        juegocaos[i,0]=(juegocaos[i-1,0]+bx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+by)/2
        juegocaos[i,2]=2
    elif aleatorio==3:
        juegocaos[i,0]=(juegocaos[i-1,0]+cx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+cy)/2
        juegocaos[i,2]=3
    elif aleatorio==4:
        juegocaos[i,0]=(juegocaos[i-1,0]+dx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+dy)/2
        juegocaos[i,2]=4
    if juegocaos[i,0]>2.75:
        puntosderecha=puntosderecha+1
    else:
        puntosizquierda=puntosizquierda+1
print("la linea que se va a usar es x=2.75, hay",puntosderecha,"puntos a la derecha de la linea, y",puntosizquierda,"puntos a la izquierda")       
plt.plot(juegocaos[:,0],juegocaos[:,1])

plt.xlabel('$x$',fontsize=11)
plt.ylabel('$y$',fontsize=11)
plt.show()