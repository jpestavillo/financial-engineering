# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd
from mylib import mylib

#%%
data_dir = '../Data/Vehicles_2015.csv'
#data_dir = 'G:\CDIN_O18\Data\Vehicles_2015.csv'
#data_dir = 'Vehicles_2015.csv'
vehicles = pd.read_csv(data_dir)

data_dir = '../Data/Accidents_2015.csv'
accidents = pd.read_csv(data_dir)
data_dir = '../Data/Casualties_2015.csv'
casualties = pd.read_csv(data_dir)



#%% utilizar mi funcion
mireporte = mylib.dqr(vehicles)
mireporte1 = mylib.dqr(accidents)
mireporte2 = mylib.dqr(casualties)





















