# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc
import sklearn.metrics as skm

#%% Generar datos
X = np.array([[2,3],[20,30],[-2,-3],[2,-3]])

plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.grid()
plt.show()

#%% Distancia Euclideana
D1 = sc.pdist(X,'euclidean')
D1 = sc.squareform(D1)

#%% Indice coseno
D2 = sc.pdist(X,'cosine')
D2 = sc.squareform(D2)

#%% Indice correlación
D3 = sc.pdist(X,'correlation')
D3 = sc.squareform(D3)
























