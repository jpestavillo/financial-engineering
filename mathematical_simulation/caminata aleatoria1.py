# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np 

import random

p=.6
q=.4
casa=25
avenida=0
borracho=10
simulacion=np.zeros((1000,5))
pasos=0
fin=0
muertes=0

for n in range(0,1001,1):
    casa=25
    avenida=0
    borracho=10
    simulacion=np.zeros((1000,5))
    pasos=0
    fin=0
    
    for i in range(0,1000,1):
        simulacion[i,0]=random.random()
        if simulacion[i,0]<p:
            borracho=borracho+1
        if simulacion[i,0]>p:
            borracho=borracho-1
        pasos=pasos+1
        
        if borracho==casa:
            fin=1
            break 
    
        if borracho==avenida: 
            fin=0
            muertes=muertes+1
            break  
           
    if fin==1:
        fin="llegar sano y salvo"
    if fin==0:
        fin="morir"
    print("tardaste",pasos,"pasos en",fin)
print("murio",muertes,"veces en",n,"simulaciones")        
        
