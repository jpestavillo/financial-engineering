# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:03:36 2017

@author: if709274
"""

#funcion 230,000x-900x**2+x**3-15,000,000
import random 
import numpy as np


#%%
n=8
a=np.zeros((8,3))
binario=np.zeros((n,10))
for i in range(n):
    a[i,0]=random.randrange(1,1024)
#%%

  
 
#%%


#a[:,1].sort()

#%%
#aqui agarramos los aptos para la pelea

def convertirbinario():
    for c3 in range(n):
       
        if a[c3,0]>512:
            binario[c3,0]=1
            a[c3,0]=a[c3,0]-512
        if a[c3,0]>256:
            binario[c3,1]=1
            a[c3,0]=a[c3,0]-256
        if a[c3,0]>128:
            binario[c3,2]=1
            a[c3,0]-128
        if a[c3,0]>64:
            binario[c3,3]=1
            a[c3,0]=a[c3,0]-64
        if a[c3,0]>32:
            binario[c3,4]=1
            a[c3,0]=a[c3,0]-32
        if a[c3,0]>16:
            binario[c3,5]=1
            a[c3,0]=a[c3,0]-16
        if a[c3,0]>8:
            binario[c3,6]=1
            a[c3,0]=a[c3,0]-8
        if a[c3,0]>4:
            binario[c3,7]=1
            a[c3,0]=a[c3,0]-4
        if a[c3,0]>2:
            binario[c3,8]=1
            a[c3,0]=a[c3,0]-2
        if a[c3,0]>1:
            binario[c3,9]=1
            a[c3,0]=a[c3,0]-1

def novias():
 for c2
#%%
for c2 in range(0,n):
    x=a[c2,0]
    a[c2,1]=230000*x-900*(x**2)+(x**3)-15000000
    print("novia",c2+1,"=  ",a[c2,1])
    convertirbinario()