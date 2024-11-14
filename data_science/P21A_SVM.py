# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:05:30 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score)

#%% Importar los datos para el análisis
data = pd.read_csv('..\Data\ex2data2.txt',
                   header=None)
X = data.iloc[:,0:2]
Y = data.iloc[:,2]

#%% Crear el modelo
#modelo = svm.SVC(kernel='linear')
#modelo = svm.SVC(kernel='poly',degree=2)
modelo = svm.SVC(kernel='rbf')
modelo.fit(X,Y)
Yhat = modelo.predict(X)

accuracy_score(Y,Yhat)








