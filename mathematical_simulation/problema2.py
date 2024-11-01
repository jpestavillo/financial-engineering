# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:47:01 2017

@author: juanp
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#%%
import matplotlib as mpl
label_size = 10
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 
#%%
r = .5
def poblacion(x, t):
    return -r * x *(1 - x)
#%%
x0 = .6
#va de 0 a 10 en 10 particiones, 
tt = np.linspace(2015, 2020, 10)
#integracion de diferencial
xx = odeint(poblacion, x0, tt)
plt.plot(tt, xx)
plt.xlabel('$t$', fontsize = 18)
plt.ylabel('$x$', fontsize = 18)
plt.show()