# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:02:45 2017

@author: juanp
"""

"21 black jack"
import numpy as np
import random
J=10
Q=10
K=10
A=14
ctrebol=.25
ccorazon=.50
cdiamante=.75
cespada=1
cartas=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
manoinicial=0

juego=np.zeros((100,100))

#%%
for i in range (0,100,1):
    juego[i,0]=random.randrange(1,52,1)
    if juego[i,0]<14:
        palo="trebol"
        carta=juego[i,0]
    elif juego[i,0]<27:
        palo="corazon"
        carta=juego[i,0]-13
    elif juego[i,0]<40:
        palo="diamante"
        carta=juego[i,0]-26
    elif juego[i,0]>40:
        palo="espada"
        carta=juego[i,0]-39
    if juego[i,0]>10:
        
    manoinicial=manoinicial+juego[i,0]
    print("tu carta",i, "es",carta,"de",palo)     
    
    
   
        
        