# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:24:56 2018

@author: if709274
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import scipy.spatial.distance as sc
import numpy as np
#%% leer los datos
data=pd.read_csv('../data/creditcard.csv')
#%%
data=data.drop(['Class','Time'],axis=1  )

#%%
Z=hierarchy.linkage(data.iloc[0:100000,:],metric='euclidean',method='complete')
