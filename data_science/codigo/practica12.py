
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

data=pd.read_csv('../data/creditcard.csv')

clasificacion= data.Class
data=data.drop(['Class','Time'],axis=1)

#%%
inercias=np.zeros(10)
for k in np.arange(10)+1:
    model=KMeans(n_clusters=k,init='random')
    model=model.fit(data)
    inercias[k-1]=model.inertia_
    
plt.plot(np.arange(1,11),inercias)
plt.xlabel('num grupos')
plt.ylabel('Inercia global')
plt.show()
#%%
model=KMeans(n_clusters=3,init='random')
model=model.fit(data)
#%% ver los resultados predice sus datos. 
Ypredict=pd.DataFrame(model.predict(data))

datos_grupo0=data.loc[Ypredict[0]==0]
datos_grupo0.transpose().plot()
#%% graficar los centroides
centroides=model.cluster_centersc
plt.plot(centroides.transpose())

#%%
