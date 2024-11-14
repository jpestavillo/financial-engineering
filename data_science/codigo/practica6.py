# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc

#%%
x=np.array([[-5,-5],[5,5],[25,25],[5,-5]])

plt.figure()
plt.scatter(x[:,0],x[:,1])
plt.hlines(0,-5,25)
plt.vlines(0,-5,25)
plt.grid()
plt.show()
#%%
D1=sc.pdist(x,'euclidean')
D1=sc.squareform(D1)
#%% indice coseno
D2=sc.pdist(x,'cosine')
D2=sc.pdist(x,'cosine')
#%%
D3=sc.pdist(x,'correlation')
D3=sc.squareform(D3)
#%%
data=pd.read_excel('../data/datos_2015.xlsx')