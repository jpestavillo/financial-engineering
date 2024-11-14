import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dir_file = '../data/coches.csv'
#dir_file = 'C:\Users\sacel\Desktop\CDIN\DATA\Vehicles_2015.csv'
#dir_file = 'Vehicles_2015.csv'
vehicles= pd.read_csv(dir_file)

dir_file = '../data/Accidentes.csv'
accidentes = pd.read_csv(dir_file)

dir_file = '../data/Casualties.csv'
casualities = pd.read_csv(dir_file)
#%%
n_date=   pd.DataFrame(pd.value_counts(accidentes['Date']))
n_day=    pd.DataFrame(pd.value_counts(accidentes['Day_of_Week']))
num_vehicles= pd.DataFrame(pd.value_counts(accidentes['Number_of_Vehicles']))
num_casualities= pd.DataFrame(pd.value_counts(accidentes['Number_of_Casualties']))

vehicles_day=  pd.DataFrame(accidentes.groupby(['Date'])['Number_of_Vehicles'].sum())
casualtie_date=pd.DataFrame(accidentes.groupby(['Date'])['Number_of_Casualties'].sum())

resumen= n_date.join(vehicles_day).join(casualtie_date).join(n_day)
N_time=  accidentes.groupby(['Time'])['Number_of_Vehicles'].sum()

#%%
fig=plt.figure(1)

plt.hist(accidentes.dropna()['Number_of_Vehicles'],
         bins=30,
         normed=False,
         cumulative=False,
         alpha=.9)
plt.ylabel('frecuencia')
plt.title('histogram')
fig.savefig('myfig.jpg')
plt.show()
#%%
hist,bins=np.histogram(accidentes['Number_of_Vehicles'],bins=30)