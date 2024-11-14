# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from itertools import cycle 
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd
import numpy as np


N2=10000


f=lambda x: abs((3/2)*x)**2 if x<=1 and x>=1 else 0
#validacion
x=np.arange(-1,1,.001)
xi= lambda u: -(-2*u+1)**(1/3) if u<.5 else (2*u-1)**(1/3) 
#xi=lambda u:(3/2)*x**(1/3) if u<.5 else (2*u-1)**(1/3) 
xib= lambda u:np.abs((2*u-1)**(1/3))
u=np.random.rand(N2)
random_f=list(map(xi,u))
plt.hist(random_f,50,density=True)
#plt.hist(random_f,50,density=True)
plt.title('validación de la distribución creada')
plt.show()