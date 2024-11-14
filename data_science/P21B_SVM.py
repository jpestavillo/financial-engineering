# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:16:50 2018

@author: riemannruiz
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,svm
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score)
import pandas as pd

#%% Importar los datos
data = pd.read_csv('../Data/ex2data2.txt',header=None)
X = data.iloc[:,0:2]
Y = data.iloc[:,2]

#%% Crear y entrenar el modelo SVM
#modelo = svm.SVC(kernel='linear')
#modelo = svm.SVC(kernel='poly',degree=2)
modelo = svm.SVC(kernel='rbf')
modelo.fit(X,Y)

Yhat_svm = modelo.predict(X)

accuracy_score(Y,Yhat_svm)















