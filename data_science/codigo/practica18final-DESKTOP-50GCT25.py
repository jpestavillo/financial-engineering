import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,precision_score,recall_score) #suma de 1 y 0 para saber el resultado del modelo 

#%%  importar los datos para el analisis
data= pd.read_csv('ex2data2.txt',header=None)
X= data.iloc[:,0:2]
Y=data.iloc[:,2]
plt.scatter(X[0],X[1],c=Y)
plt.show()
#%% preparar los datos
ngrado=7
poly=PolynomialFeatures(ngrado)
Xa=poly.fit_transform(X)
#%%
modelo= linear_model.LogisticRegression(C=1)
modelo.fit(Xa,Y)

Yhat=modelo.predict(Xa)
accuracy_score(Y,Yhat)
#%%

precision_score(Y,Yhat)
#%%
recall_score(Y,Yhat)
#%% opcional (dibujar la frontera)
h=.01 
xmin,xmax=X[0].min(),X[0].max()
ymin,ymax=X[1].min(),X[1].max()
xx,yy=np.meshgrid(np.arange(xmin,xmax,h),np.arange(ymin,ymax,h))

Xnew=pd.DataFrame(np.c_[xx.ravel(),yy.ravel()]) #c_ es para concatenar

Xam=poly.fit_transform(Xnew)
Z=modelo.predict(Xam)
Z=Z.reshape(xx.shape)
plt.contour(xx,yy,Z,cmap=plt.cm.Paired)
plt.scatter(X[0],X[1],c=Y,cmap=plt.cm.Paired)
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()

#%%
W=modelo.coef_
plt.bar(np.arange(len(W[0])),W[0])
plt.show()