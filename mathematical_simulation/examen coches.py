# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:12:52 2017

@author: juanp
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:36:29 2017

@author: Gabriel y juan pablo 
"""

 
import numpy as np

import random

"par0=.1"
"par1=.1"
"par2=.25"
"par3=.3"
"par4=.25"
"prd1=.4"
"prd2=.35"
"prd3=.15"
"prd4=.1"
"columna0=aleatorios"
"columna1=numerodecoches"
"columna2=diasderenta por coche"


autos=np.zeros((500,5))
numeroautos=np.zeros((500,5))
tests=365
par0=.1
par1=.2
par2=.45
par3=.75
par4=1

prd1=.4
prd2=.75
prd3=.9
prd4=1


necesiad=0
necesidad=0
renta=350
nocar=200
costoauto=75000
autos[2,2]=2

#%%
for i in range (0,tests,1):
    autos[i,0]= random.random()
    
    if autos [i,0]<=par0:
        autos[i,1]=0
        if autos[i,0]>necesidad:
            necesidad=autos[i,0]
        print (necesidad)
    elif autos [i,0]<=par1:
        autos[i,1]=1
        if autos[i,0]>necesidad:
            necesidad=autos[i,0]
        print (necesidad)
    elif autos [i,0]<=par2:
        autos[i,1]=2
        if autos[i,0]>necesidad:
            necesidad=autos[i,0]
        print (necesidad)
    elif autos [i,0]<=par3:
        autos[i,1]=3
        if autos[i,0]>necesidad:
            necesidad=autos[i,0]
        print (necesidad)
    elif autos [i,0]<=par4:
        if autos[i,0]>necesidad:
            necesidad=autos[i,0]
        print (necesidad)
 
for j in range (0,tests,1):
    numeroautos[j,0]= random.random()
    if numeroautos[j,0]<= prd1:
        numeroautos[j,1]=1
    if numeroautos[j,0]<= prd2:
        numeroautos[j,1]=2
    if numeroautos[j,0]<= prd3:
        numeroautos[j,1]=3
    if numeroautos[j,0]<= prd4:
        numeroautos[j,1]=4    
        
 

#%%
k=1






#%%
k2=2

#%%
k3=3


#%%
k=4
#%%
k=5
#%%
k=6
#%%
k=7

#%%
k=8
#%%
k=9

#%%
k=10 
#%%
k=11
#%%
k=12
#%%
k=13
#%%
k=14
#%%
k=15
#%%
k=16
#%%

