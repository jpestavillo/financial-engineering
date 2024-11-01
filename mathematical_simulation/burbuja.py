# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:56:10 2017

@author: juanp
"""

#%%
#def ordenamientoBurbuja(lista,tam):
 #   for i in range(1,tam):
  #      for j in range(0,tam-i):
   #         if(lista[j] > lista[j+1]):
    #            k = lista[j+1]
     #           lista[j+1] = lista[j]
      #          lista[j] = k
def burbujas():
    for k in range(1,n):
        for j in range(0,n-1):
            if a[j,0]<a[j+1,0]:
                temporal=a[j,0]
                a[j,0]=a[j+1,0]
                a[j+1,0]=temporal 