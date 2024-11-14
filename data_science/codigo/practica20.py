import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm  #maquina de vector soporte 
#%%  crear los datos para analisis 
np.random.seed(0)
X=np.r_[np.random.randn(20,2)-[2,2],np.random.randn(20,2)+[2,2]]
Y=[0]*20+[1]*20
#%%
modelo=svm.SVC(kernel='linear')
modelo.fit(X,Y)
#%% visualizar los resultados 
w= modelo.coef_[0]
m=-w[0]/w[1]
b= -modelo.intercept_[0]/w[1]
xx=np.linspace(-5,5)
yy=m*xx+b


vs=modelo.support_vectors_ #vectores soporte 
gamma=modelo.support_vectors_[0]
yy_1=m*xx+(gamma[1]-m*gamma[0])    #### falta la linea de abajo 
gamma=modelo.support_vectors_[-1]
yy_2=m*xx+(gamma[1]-m*gamma[0])


yy_1=m*xx+(gamma[1]-m*gamma[0])   #linea que pase por gama
plt.scatter(X[:,0],X[:,1],c=Y) #le das el color dependiendo del grupo en el que se encuentren 
plt.plot(xx,yy,'k-')
plt.scatter(vs[:,0],vs[:,1],s=80,facecolor='k')  #s es de tamaño, facecolor es para colores  

plt.plot(xx,yy_2,'k--')
plt.plot(xx,yy_1,'k--')
plt.show()

