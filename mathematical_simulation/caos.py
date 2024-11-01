# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:50:25 2017

@author: juanp
"""
import numpy as np
import matplotlib.pyplot as mpl
import random
puntos=10000
ax=-1
bx=1
ay=-1
by=1

juegopts=np.zeros((4,4))
juegocaos=np.zeros((puntos,3))


ax=2
ay=0
bx=3
by=1
cx=4
cy=0
dx=3
dy=-1



for i in range (1,puntos):
    aleatorio=random.randrange(1,4)
    if aleatorio==1:
        juegocaos[i,0]=(juegocaos[i-1,0]+ax)/2
        juegocaos[i,1]=(juegocaos[i-1,0]+ay)/2
    elif aleatorio==2:
        juegocaos[i,0]=(juegocaos[i-1,0]+bx)
        juego
    elif aleatorio==3:
        