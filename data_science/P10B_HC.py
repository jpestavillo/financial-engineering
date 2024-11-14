# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:20:59 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc
import pandas as pd

#%% Leer los datos
data = pd.read_csv('../Data/creditcard.csv')

#%% Seleccionar los datos a analizar
data = data.drop(['Time','Class'],axis=1)

#%% Aplicar clustering jerarquico
Z = hierarchy.linkage(data.iloc[0:30000,:],metric='euclidean',method='complete')

#%% Criterio de grafica de codo
last = Z[-15:,2]
last_rev = last[::-1]
idx = np.arange(1,len(last_rev)+1)
plt.plot(idx,last_rev)
plt.xlabel('Num grupos')
plt.ylabel('Distancia')
plt.show()

#%% Clasificar los datos
grupos = hierarchy.fcluster(Z,3,criterion='maxclust')
















