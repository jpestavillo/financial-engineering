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

#%%
"datos problema"
pr0=.1
pr1=.2
pr2=.45
pr3=.75
pr4=1

prd1=.4
prd2=.75
prd3=.9
prd4=1

#%%
"estructura"
"columna0=aleatorionumero"
"columna1=numerorent"
"columna2= rentados  se usa for de columna 31-46"
"columna= total a rentar"

"columna2=disponible = k-rentados"
"columna3=ganancia"

"columna4=necesidad"
"columna10=ganancia"
"columna11-27 existencia carros  (usamos for para llenar esos espacios) "
"columna31-46  disponibilidad carros    "
"columna 51-66 aleatorios dias "
"columna 71-86 numero de dias"
"columna 91-106 dias restantes"
"columna 111-127 ganancia"
#%%

"declaramos variables"
"k=numero de coches"
"day=numero de dia corriendo"
simulacion=np.zeros((365,127,17))
for k in range (1,16,1): 
    columna11=k+10
    for i in range (0,365,1):
        simulacion[i,0,k]=random.random()
        if  simulacion[i,0,k]<pr0:
            simulacion[i,1,k]=0
        elif simulacion[i,0,k]<pr1:
            simulacion[i,1,k]=1
        elif simulacion[i,0,k]<pr2:
            simulacion[i,1,k]=2   
        elif simulacion[i,0,k]<pr3:
            simulacion[i,1,k]=3
        elif simulacion[i,0,k]<pr4:
            simulacion[i,1,k]=4
        for contador in range (0,k,1):
            simulacion[i,(columna11)+contador,k]=1
"for k in range(1,16,1):   ciclo para cuando casi termine"
#%%


"if total a rentar[3,dia]>disponibles:"
"A[127,dia]= A[127,dia]-(200*(total a rentar-disponibles))"

"for contadorganancia in range (1,365,1):"
"gananciatotal=ganancia total +ganancia[i,3]"
    
"print (ganancia en k=, k, gananciatotal)"
" ganancia total=0  "


    

#%%
"prints"
"gananciatotal"
