# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:08:45 2018

@author: if709274
"""

import numpy as np 
import matplotlib.pyplot as plt
from sklearn import svm 
import pandas as pd 
from sklearn.metrics import (accuracy_score,precision_score,recall_score)
#%% importar los datos para el analisis
data=pd.read_csv('../data/ex2data2.txt',header=None)
X=data.iloc[:,0:2]
Y=data.iloc[:,2]
#%% crear el modelo
#modelo=svm.XVC(kernel='linear')
modelo=svm.SVC(kernel='poly',degree=2)
#modelo=svm.SVC(kernel='rbf')
modelo.fit(X,Y)
Yhat=modelo.predict(X)

accuracy_score(Y,Yhat)