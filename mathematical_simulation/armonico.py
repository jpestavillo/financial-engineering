# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:51:27 2017

@author: juanp
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint 


a=1
b=1

def armonico (variables,t):
        x1,x2=variables
        return [a*x2, -b*x1]
inicial=[5,5] #vector de posicion inicial y velocidad inicial

#tiempo= nplinspace(0,15) #dominio temporal 0 de 15
tiempo=np.arange(0,50,.01)

resultado = odeint(armonico,inicial,tiempo)
# en este punto se usa odeint para integrar

xx,yy=resultado.T

import matplotlib as mpl 
label_size= 14
mpl.rcParams['xtick.labelsize']= label_size
mpl.rcParams['xtick.labelsize']= label_size 


plt.plot(tiempo,xx,c= 'b', label="romeo")
plt.plot(tiempo,yy,c='r',label="julieta")
plt.legend(loc='best',prop={'size':14})
plt.xlabel('',frontsize=14)
plt.show()
