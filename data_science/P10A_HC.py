# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:23:42 2018

@author: riemannruiz
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc
import numpy as np

#%% Leer los datos
data = pd.read_csv('../Data/creditcard.csv')

#%% Seleccionar los datos a analizar
data = data.drop(['Class','Time'],axis=1)

#%% Aplicar clustering jerarquico
Z = hierarchy.linkage(data.iloc[0:30000,:],metric='euclidean',method='complete')