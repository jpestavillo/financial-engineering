#tarea1
#tarea1=puntob.join(puntoc).join(puntod)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mylib import mylib

dir_file = '../data/coches.csv'
vehicles= pd.read_csv(dir_file)

dir_file = '../data/accidentes.csv'
accidentes = pd.read_csv(dir_file)

dir_file = '../data/casualties.csv'
casualities = pd.read_csv(dir_file)

#%%
#puntob
#a.	Realizar un histograma de las localizaciones de los accidentes,
 #y comentar estos histogramas. 

puntob=pd.DataFrame(pd.value_counts(accidentes['Location_Easting_OSGR']))
plt.hist(accidentes.dropna()['Location_Easting_OSGR'])
plt.title('frecuencia de localizacion')
plt.xlabel('localizaciones')
plt.ylabel('frecuencia')
plt.show()
#%%
n_day=    pd.DataFrame(pd.value_counts(accidentes['Day_of_Week']))

#%%
num_casualities= pd.DataFrame(pd.value_counts(accidentes['Number_of_Casualties']))
#%%
sex=pd.DataFrame(pd.value_counts(casualities['Sex_of_Casualty']))
#%%
#edades=['Age_of_Casualty']
plt.hist(casualities['Age_of_Casualty'],
         bins=20)
plt.xlabel('edad')
plt.ylabel('frecuencia')
plt.title('distribucion de edad')
plt.show()
#la mayoria de las personas son de edad 20-30 anos
#%%
Sex_of_Driver=pd.DataFrame(pd.value_counts(vehicles['Sex_of_Driver']))
#pinche raza, ahora ponen que existen 4 sexos
#%%
Age_of_Driver=pd.DataFrame(vehicles['Age_of_Driver'])
Age_of_Driver.mean()
