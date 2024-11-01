# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:31:08 2017

@author: juanp
"""
import numpy as np
import random 
muros=100
construidos=0
p=.97
q=.3
costo=25
simulacion=np.zeros((1001,1001))
dias=0


for i in range (1,1000,1):
      simulacion[i,0]=random.random()
      if construidos<muros:
          if simulacion[i,0]<p:
              construidos=construidos+1            
              dias=dias+1
          if simulacion[i,0]>p:
              construidos=construidos-1
              dias=dias+1
          
print ("tardaste",dias,"dias en construir",muros,"muros")
print("te costo: $",costo*25)