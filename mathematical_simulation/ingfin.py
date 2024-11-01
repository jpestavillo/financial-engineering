# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:05:35 2017

@author: juanp
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
datos=pd.read_excel('C:/Users/juanp/Desktop/TIIE.xlsx')
t=np.zeros((80,3))
trimestral=np.zeros((60,1))
tasa=datos.TIIE
#for contador in range(58):
index=np.zeros(60)
for j in range(58):
    index[j]=j

for i in range(172):
    x1=i*3
    x2=i*3+1
    x3=i*3+2
    d1=tasa[x1]
    d2=tasa[x2]
    d3=tasa[x3]
    trimestral[i,0]=(d1+d2+d3)/3
    
    
mpl.plot(datos.index,trimestral)
mpl.show()