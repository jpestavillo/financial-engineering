# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:26:10 2017

@author: juanp
"""
import random
import numpy as np
import matplotlib.pyplot as plt

"se vaa modelar el movimientode una particula con tiempo t el cual tiene un movimiento lineal . "
posicion=20
cambio=2.7
p=.5
q=.5
simulacion= np.zeros((1000,3))
for n in range(1,10,1):
    posicion=posicion
    for i in range (1,11):
        simulacion[1,0]=posicion
        simulacion[i,0]=random.random()
        if simulacion[i,0]<.5:
            simulacion[i,1]=simulacion[i-1,1]+cambio
        if simulacion[i,0]>.5:
            simulacion[i,1]=simulacion[i,1,-1]-cambio
    
        print (posicion,"de",n)
    print("---------------")    


plt.plot    