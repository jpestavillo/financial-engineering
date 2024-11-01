# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:03:36 2017


@author: estavillo y emanuel
"""

#funcion 230,000x-900x**2+x**3-15,000,000
import random 
import numpy as np


#%%
n=8  #cada columna es un experimento
a=np.zeros((n,10))  #los 8
b=np.zeros((n,10))  #maximizacion
c=np.zeros((n,10))  #delta
d=np.zeros((n,10))  #maximizacion ordenada
bi=np.zeros((n,21)) #numeros en binario


       
#%%   
for g in range(n):
    a[i,0]=random.randrange(1,1024)
def inicio():
    for i in range(n):
        
        x=a[i,columna]
        b[i,columna]=230000*x-900*(x**2)+(x**3)-15000000
        c[i,columna]=a[i,columna]
        d[i,columna]=b[i,columna]
        
def burbujas():
    for k in range(1,n):
        for j in range(0,n-1):
            if d[j,columna]<d[j+1,columna]:
                temporal=d[j,columna]
                d[j,columna]=d[j+1,columna]
                d[j+1,columna]=temporal
    may1=d[0,columna]
    may2=d[1,columna]
    may3=d[2,columna]
    may4=d[3,columna]
    for cont in range(n):
        if a[cont,columna]==may1:
            a[cont,columna+1]=may1
        if a[cont,columna]==may2:
            a[cont,columna+1]=may2
        if a[cont,columna]==may3:
            a[cont,columna+1]=may3
        if a[cont,columna]==may4:
            a[cont,columna+1]=may4
    transformacion1=bi[cont,0]*32+bi[cont,1]*16+bi[cont,2]*8+bi[cont,3]*4+bi[cont,4]*2+bi[cont,5]+bi[cont,6]*512+bi[cont,7]*256+bi[cont,8]*128+bi[cont,9]*64        
            
def imprimir():
    print("experimento numero",columna+1)
    for contadorimprimir in range(n):
        print(a[contadorimprimir,columna])
    
def mejores():
        

def convertirbinario():
    for contadorbinario in range(n):
        if c[contadorbinario,columna]>=512:
            bi[contadorbinario,columna]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-512
        if c[contadorbinario,columna]>=256:
            bi[contadorbinario,columna+1]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-256
        if c[contadorbinario,columna]>=128:
            bi[contadorbinario,columna+2]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-128
        if c[contadorbinario,columna]>=64:
            bi[contadorbinario,columna+3]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-64
        if c[contadorbinario,columna]>=32:
            bi[contadorbinario,columna+4]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-32
        if c[contadorbinario,columna]>=16:
            bi[contadorbinario,columna+5]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-16
        if c[contadorbinario,columna]>=8:
            bi[contadorbinario,columna+6]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-8
        if c[contadorbinario,columna]>=4:
            bi[contadorbinario,columna+7]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-4
        if c[contadorbinario,columna]>=2:
            bi[contadorbinario,columna+8]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-2
        if c[contadorbinario,columna]==1:
            bi[contadorbinario,columna+9]=1
            c[contadorbinario,columna]=c[contadorbinario,columna]-1
        bi[contadorbinario,columna+10]=(bi[contadorbinario,0]*512)+(bi[contadorbinario,1]*256)+(bi[contadorbinario,2]*128)+(bi[contadorbinario,3]*64)+(bi[contadorbinario,4]*32)+(bi[contadorbinario,5]*16)+(bi[contadorbinario,6]*8)+(bi[contadorbinario,7]*4)+(bi[contadorbinario,8]*2)+(bi[contadorbinario,9]*1)
        #codigo hecho por estavillo
    
def colocacion():
    cont=0
    mayor1=0
    mayor2=0
    mayor3=0
    mayor4=0
    transformacion1=0
    transformacion2=0
    transformacion3=0
    transformacion4=0
    
    for cont in range(n):
        if b[cont,columna]>mayor4:
                 if b[cont,columna]>mayor3:
                     if b[cont,columna]>mayor2:
                         if b[cont,columna]>mayor1:
                             mayor4=mayor3
                             mayor3=mayor2
                             mayor2=mayor1
                             mayor1=b[cont,columna]
                             a[cont,columna+1]=bi[cont,columna+10]
                             transformacion1=bi[cont,0]*32+bi[cont,1]*16+bi[cont,2]*8+bi[cont,3]*4+bi[cont,4]*2+bi[cont,5]+bi[cont,6]*512+bi[cont,7]*256+bi[cont,8]*128+bi[cont,9]*64
                         elif  b[cont,columna]<mayor1:
                             mayor4=mayor3
                             mayor3=mayor2
                             mayor2=b[cont,columna]
                             a[cont,columna+1]=bi[cont,columna+10]
                             transformacion2=bi[cont,0]*32+bi[cont,1]*16+bi[cont,2]*8+bi[cont,3]*4+bi[cont,4]*2+bi[cont,5]+bi[cont,6]*512+bi[cont,7]*256+bi[cont,8]*128+bi[cont,9]*64
                     elif  b[cont,columna]<mayor2:
                         mayor4=mayor3
                         mayor3=b[cont,columna]
                         a[cont,columna+1]=bi[cont,columna+10]
                         transformacion3=bi[cont,0]*32+bi[cont,1]*16+bi[cont,2]*8+bi[cont,3]*4+bi[cont,4]*2+bi[cont,5]+bi[cont,6]*512+bi[cont,7]*256+bi[cont,8]*128+bi[cont,9]*64
                 elif b[cont,columna]<mayor3:
                     mayor4=b[cont,columna]
                     a[cont,columna+1]=bi[cont,columna+10]
                     transformacion4=bi[cont,0]*32+bi[cont,1]*16+bi[cont,2]*8+bi[cont,3]*4+bi[cont,4]*2+bi[cont,5]+bi[cont,6]*512+bi[cont,7]*256+bi[cont,8]*128+bi[cont,9]*64
    if transformacion3==0:
        transformacion3=(transformacion1+transformacion2)/2  
    if transformacion4==0:
        transformacion4=(transformacion3+transformacion1)/2
              

        
   
    #codigo hecho por estavillo
    for c12 in range(n):
        if a[c12,columna+1]==0:
            if transformacion1>0:
                a[c12,columna+1]=transformacion1
                transformacion1=0
            elif transformacion2>0:
                if a[c12,columna+1]==0:
                    a[c12,columna+1]=transformacion2
                    transformacion2=0
            elif transformacion3>0:
                if a[c12,columna+1]==0:
                    a[c12,columna+1]=transformacion3
                    transformacion3=0
            elif transformacion4>0:
                if a[c12,columna+1]==0:
                    a[c12,columna+1]=transformacion4
                    transformacion4=0
             
    
            
        
columna=0         
while columna<9:                   
    inicio()
    convertirbinario()
    burbujas()
    colocacion() 
    imprimir()           
    columna=columna+1
print("********* despues de 9 pruebas, estos 8 son los mejores*********")
print("codigo propiedad de estavillo")


    
#%%
    #def ordenamientoBurbuja(lista,tam):
 #   for i in range(1,tam):
  #      for j in range(0,tam-i):
   #         if(lista[j] > lista[j+1]):
    #            k = lista[j+1]
     #           lista[j+1] = lista[j]
      #          lista[j] = k
 
    
        