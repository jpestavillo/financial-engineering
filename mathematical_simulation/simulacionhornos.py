import numpy as np
import random
repeticiones=100
dineroA=200
A= np.zeros((repeticiones,5))
B=np.zeros((repeticiones,5))
#%%
dineroA=200
dinerob=200
"a=jugador1"
"b=jugador2"

"1=color"
"2=apuesta"
"3=ganancia"
"4=dinero"
"5=total"
rojo=.5
apuesta=1


for i in range (1,repeticiones,1):
    A[i,1] =random.random()

    if A[i,1]<rojo:
        dinero=dineroA+1
    else: dinero=dineroA-1

for j in range (1,repeticiones,1):
    B[j,1] =random.random()
    if(B[j,1]<rojo):
        dinerob=dinerob+apuesta
        apuesta=1
    else:
        dinerob=dinerob-apuesta
        apuesta=apuesta*2
    'print' dinerob




print A
print B
print dineroA
print dinerob
