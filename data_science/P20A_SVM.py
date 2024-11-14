# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

#%% Crear los datos para análisis
np.random.seed(0)
X = np.r_[np.random.randn(20,2)-[2,2],np.random.randn(20,2)+[2,2]]
Y = [0]*20+[1]*20

#%% Crear el modelo SVM
modelo = svm.SVC(kernel='linear')
modelo.fit(X,Y)
Yhat = modelo.predict(X)

#%% Visualizar los resultados
w = modelo.coef_[0]
m = -w[0]/w[1]
b = -modelo.intercept_[0]/w[1]
xx = np.linspace(-5,5)
yy = m*xx+b


vs = modelo.support_vectors_

gamma = modelo.support_vectors_[0]
yy_1 = m*xx+(gamma[1]-m*gamma[0])
gamma = modelo.support_vectors_[-1]
yy_2 = m*xx+(gamma[1]-m*gamma[0])



plt.scatter(X[:,0],X[:,1],c=Y)
plt.plot(xx,yy,'k-')
plt.scatter(vs[:,0],vs[:,1],s=80,
            facecolor='k')
plt.plot(xx,yy_1,'k--')
plt.plot(xx,yy_2,'k--')
plt.show()
















