# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 19:55:40 2017

@author: juanp
"""
import pandas as pd 
import random 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
#%%  excavacion
t1=0  #esta en horas

excavado=0
excavar=2000 #goal
pderrumbe=.10  
tierraregresa=random.randrange(45,65)
pde=72
pi=28

while excavado<excavar:
    aleatorio=random.random()
    if aleatorio<pderrumbe:
        excavado=excavado-tierraregresa
        t=t+1
    retiroxhora=random.randrange(17,23)  #20+-15%
    excavado=excavado+retiroxhora
    t1=t1+1
    
print("tardan",t1,"horas en terminar excavacion")

#%%   climentacion  
puntos=100

juegopts=np.zeros((4,4))
juegocaos=np.zeros((puntos,4))


ax=21
ay=59
bx=5
by=23
cx=14.5
cy=19
dx=43
dy=7

juegocaos[0,0]=20
juegocaos[0,1]=50
puntosderecha=0
l=18.32
puntosizquierda=0
t2=0
costo2=0

for i in range (1,puntos):
    aleatorio=random.randrange(1,5)
    
    if aleatorio==1:
        juegocaos[i,0]=(juegocaos[i-1,0]+ax)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+ay)/2
        juegocaos[i,2]=1
    elif aleatorio==2:
        juegocaos[i,0]=(juegocaos[i-1,0]+bx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+by)/2
        juegocaos[i,2]=2
    elif aleatorio==3:
        juegocaos[i,0]=(juegocaos[i-1,0]+cx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+cy)/2
        juegocaos[i,2]=3
    elif aleatorio==4:
        juegocaos[i,0]=(juegocaos[i-1,0]+dx)/2
        juegocaos[i,1]=(juegocaos[i-1,1]+dy)/2
        juegocaos[i,2]=4

for contador1 in range(0,pi):       
    chicloso=random.randrange(32500,44100)
    costo2=costo2+chicloso
    tiempochicloso=random.randrange(2,5)
    
    t2=t2+tiempochicloso
for contador2 in range(pi,100):
    firme=random.randrange(10000,17500)
    tiempofirme=random.randrange(1,3)
    t2=t2+tiempofirme
    #if juegocaos[i,0]>
        #puntosderecha=puntosderecha+1
    #else:
        #puntosizquierda=puntosizquierda+1
print( "hay",pde,"puntos a la derecha de la linea, y",pi,"puntos a la izquierda")       
print("tardan",t2,"dias en climatizar y les cuesta $",costo2)
plt.plot(juegocaos[:,0],juegocaos[:,1])

plt.xlabel('$x$',fontsize=11)
plt.ylabel('$y$',fontsize=11)
plt.show()


#%%
"simulacion montecarlo"
lim_i = 0
lim_s = math.pi
M =  17
n = 1000
ne = 0

precio1 = 59.39
precio2 = 44.62
precio3 = 29.76

for i in range (n):
    # valores en x
    x = lim_i+random.random()*(lim_s-lim_i)
    # valores en y
    y = random.random() * M
    # f(x) 
    fx = (np.exp(x)-np.sqrt(np.sin(x)**2+1))
    ##  y<f(x) ?
    if (fx) > (y):
        ne = ne + 1   
dias = ne*(lim_s-lim_i)*M/n
print ("tarda :", dias)
ct=4567436
costo = precio1*100 + precio2*400 + precio3*400
print ("el costo es de : ", costo)
 
t3=l
#%%
#%% Plomería externa.
import random as rd
días=0
for i in range(5):
    x=random.random()
    if x>.1:
        if x>.25:
            if x>.45:
                if x>0.8:
                    días+=5
                else:
                    días+=4
            else:
                días+=3
        else:
            días+=2
    else:
        días+=1
costo_plom=400*91.86
print ('dias',días)
print ('costo',costo_plom)

#%% Plomería interna.

gas=250
sim2=50
agua=100
avance=0
dias1=4/30
dias2=0.3
dias3=0.5
dias4=(7/30)+0.5
ins_tub=np.zeros((sim2,6))
for i in range (0,sim2):
    ins_tub[i,0]=random.random()
    if(ins_tub[i,0]<dias1):
        ins_tub[i,1]=avance+10
        ins_tub[i,4]=4/24
    if((ins_tub[i,0]>dias1)&(ins_tub[i,0]<dias2)):
        ins_tub[i,1]=avance+10
        ins_tub[i,4]=5/24
    if((ins_tub[i,0]>dias2)&(ins_tub[i,0]<dias3)):
        ins_tub[i,1]=avance+10
        ins_tub[i,4]=6/24    
    if((ins_tub[i,0]>dias3)&(ins_tub[i,0]<dias4)):
        ins_tub[i,1]=avance+10
        ins_tub[i,4]=7/24    
    if(ins_tub[i,0]>dias4):
        ins_tub[i,1]=avance+10
        ins_tub[i,4]=8/24
    ins_tub[i,2]=ins_tub[i,1]+ins_tub[i-1,2]
    if(ins_tub[i,2]>gas):
        ins_tub[i,0]=0
    if(ins_tub[i,0]>0):
        ins_tub[i,3]=ins_tub[i,4]*1
suma_ins_tub=ins_tub[:,3].sum()
cost_plo_in=40.32*agua+73.59*gas

print('dias',suma_ins_tub)
print('costo',cost_plo_in)

#%% Revestimiento exterior.

reves=500
sim3=50
pos10=.05 
pos9=0.15
pos8=0.3
pos7=0.5
pos6=0.75
pos5=0.85
pos4=0.93
pos3=0.96
pos2=0.98
pos1=0.99  
suma_reves=0
reves_in=np.zeros((sim3,5))
for j in range (0,sim3):
    reves_in[j,0]=random.random()
    if(reves_in[j,0]<pos10):
        reves_in[j,1]=10*(random.randrange(2,5))
    if((reves_in[j,0]>pos10)&(reves_in[j,0]<pos9)):
        reves_in[j,1]=9*(random.randrange(2,5))
    if((reves_in[j,0]>pos9)&(reves_in[j,0]<pos8)):
        reves_in[j,1]=8*(random.randrange(2,5))
    if((reves_in[j,0]>pos8)&(reves_in[j,0]<pos7)):
        reves_in[j,1]=7*(random.randrange(2,5))
    if((reves_in[j,0]>pos7)&(reves_in[j,0]<pos6)):
        reves_in[j,1]=6*(random.randrange(2,5))
    if((reves_in[j,0]>pos6)&(reves_in[j,0]<pos5)):
        reves_in[j,1]=5*(random.randrange(2,5))
    if((reves_in[j,0]>pos5)&(reves_in[j,0]<pos4)):
        reves_in[j,1]=4*(random.randrange(2,5))
    if((reves_in[j,0]>pos4)&(reves_in[j,0]<pos3)):
        reves_in[j,1]=3*(random.randrange(2,5))
    if((reves_in[j,0]>pos3)&(reves_in[j,0]<pos2)):
        reves_in[j,1]=2*(random.randrange(2,5))
    if((reves_in[j,0]>pos2)&(reves_in[j,0]<pos1)):
        reves_in[j,1]=1*(random.randrange(2,5))
    if(reves_in[j,0]>pos1):
        reves_in[j,1]=0
    
    reves_in[j,2]=reves_in[j,1]+reves_in[j-1,2]
    if(reves_in[j,2]>reves):
        reves_in[j,1]=0
    if(reves_in[j,1]>0):
        reves_in[j,3]=reves_in[j,1]/12
suma_reves=reves_in[:,3].sum()
costo_reves=reves*232.12

print('dias',suma_reves)
print('costo',costo_reves)

#%% Pintura exterior

pintura=1500
p_lluvia=0.15
sim4=1000
suma_pint_ext=0
pintu_ext=np.zeros((sim4,4))
for k in range (0,sim4):
    pintu_ext[k,0]=random.random()
    if(pintu_ext[k,0]>p_lluvia):
        pintu_ext[k,1]=random.randrange(10,15)
    if(pintu_ext[k,0]<p_lluvia):
        pintu_ext[k,1]=0
    pintu_ext[k,2]=pintu_ext[k,1]+pintu_ext[k-1,2]
    if(pintu_ext[k,2]>pintura):
        pintu_ext[k,0]=0
    if(pintu_ext[k,0]>0):
        pintu_ext[k,3]=pintu_ext[k,1]/12
suma_pint_ext=pintu_ext[:,3].sum()
costo_pintura=52.08*pintura
print('dias', suma_pint_ext)
print('costo', costo_pintura)

#%% Pintura interior.

pintura=1900
p_lluvia=0.05
sim4=1000
suma_pint_ext=0
pintu_ext=np.zeros((sim4,4))
for k in range (0,sim4):
    pintu_ext[k,0]=random.random()
    if(pintu_ext[k,0]>p_lluvia):
        pintu_ext[k,1]=random.randrange(10,15)
    if(pintu_ext[k,0]<p_lluvia):
        pintu_ext[k,1]=0
    pintu_ext[k,2]=pintu_ext[k,1]+pintu_ext[k-1,2]
    if(pintu_ext[k,2]>pintura):
        pintu_ext[k,0]=0
    if(pintu_ext[k,0]>0):
        pintu_ext[k,3]=pintu_ext[k,1]/12
suma_pint_ext=pintu_ext[:,3].sum()
costo_pintura=62.47*pintura
print('dias', suma_pint_ext)
print('costo', costo_pintura)
#%%
#instalacion electrica
t10=random.randrange(21,65)

#%%
r11=random.random()
if r11<.25:
    t11=random.randrange(21,30)
if r11<.55:
    t11=random.randrange(30,40)
if r11<.90:
    t11=random.randrange(40,50)
elif r11<1:
    t11=random.randrange(50,65)
    
print(t11,"dias tardaron en construir el wallboard")

#%%
#t12
t12=random.randrange(0,28)


#%%
#acabado de exteriores t13
t13=random.randrange(7,21)
 
#%%
#acabados de interiores t14
datos=pd.read_excel('C:/Users/juanp/Desktop/BD_Acabadosinteriores.xlsx',sheetname="Histórico de Cabados interiores",skiprows=1)
#se van a usar entre 1000 y 1200 metros cuadrados
#el costo promedio
pendiente=datos.sumxy[3]
ordenada=datos.sumy[3]
print("la ecuacion de la regresion lineal es y=",pendiente,"x+",ordenada)
#por lo tanto el costo va a ser de 20.50 por metro
construidointerior=random.randrange(1000,1200)
costo=costo+construidointerior*ordenada
#%%
#total

print("el costo total aproximado es de", ct,"se tardo la construiccion",t/7,"semanas")