from mylib import mylib
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.metrics import (accuracy_score, precision_score, recall_score)
import pickle # Nos sirve para evitar correr nuestro código y que tarde mucho
import matplotlib.pyplot as plt
#%% CARGAR DATA
data=pd.read_csv('../data/Kaggle_Training_Dataset.csv',index_col = 'sku')
#%% Definir función
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x     
data = data.apply(replace_text,args=('No',0)).apply(replace_text,args=('Yes',1))
data=data.dropna()
#%%
x = data.iloc[:,:21]
x= (x-x.mean(axis=0))/x.std(axis=0)
y= pd.DataFrame(data['went_on_backorder'])

#%%

y=np.array(y)
y.shape=(1693050)
x=np.array(x)
x_norm=np.array(x)
modelo =svm.SVC(kernel='linear')
modelo.fit(x_norm,y)
yhat = modelo.predict(x_norm)

print(accuracy_score(y,yhat))
print(precision_score(y,yhat, average=None))
print(recall_score(y,yhat, average=None))
