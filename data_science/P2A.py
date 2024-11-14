# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

dir_file = '../Data/Vehicles_2015.csv'
#dir_file = 'G:/CDIN_O18/Data/Vehicles_2015.csv'
#dir_file = 'Vehicles_2015.csv'
vehicles = pd.read_csv(dir_file)

dir_file = '../Data/Accidents_2015.csv'
accidents = pd.read_csv(dir_file)

dir_file = '../Data/Casualties_2015.csv'
casualties = pd.read_csv(dir_file)

#%%
N_date = pd.DataFrame(pd.value_counts(accidents['Date']))
N_dayweek = pd.DataFrame(pd.value_counts(accidents['Day_of_Week']))
Num_vehicles = pd.DataFrame(pd.value_counts(accidents['Number_of_Vehicles']))
Num_casualties = pd.DataFrame(pd.value_counts(accidents['Number_of_Casualties']))

Vehicles_date = pd.DataFrame(accidents.groupby(['Date'])['Number_of_Vehicles'].sum())
Casualtie_date = pd.DataFrame(accidents.groupby(['Date'])['Number_of_Casualties'].sum())

resumen = N_date.join(Vehicles_date).join(Casualtie_date).join(N_dayweek)

N_vehiclestypes = pd.DataFrame(pd.value_counts(vehicles.Vehicle_Type))

N_time = accidents.groupby(['Time'])['Number_of_Vehicles'].sum()

#%% Graficos
plt.hist(accidents['Number_of_Vehicles'],bins=30)
plt.xlabel('Number of Vehicles')
plt.ylabel('Frecuencia')
plt.title('Vehicles Histogram')
plt.show()

#%%
plt.hist(accidents['Number_of_Vehicles'],
         bins=30,
         normed=True)
plt.xlabel('Number of Vehicles')
plt.ylabel('Frecuencia')
plt.title('Vehicles Histogram')
plt.show()

#%%
plt.hist(accidents['Number_of_Vehicles'],
         bins=30,
         normed=True,
         cumulative=True)
plt.xlabel('Number of Vehicles')
plt.ylabel('Frecuencia')
plt.title('Vehicles Histogram')
plt.show()

#%%
fig = plt.figure(1)
plt.hist(accidents['Number_of_Vehicles'],
         bins=30,
         normed=True,
         histtype='stepfilled',
         color='b',
         alpha=0.5)
plt.xlabel('Number of Vehicles')
plt.ylabel('Frecuencia')
plt.title('Vehicles Histogram')
fig.savefig('../Data/myfig.png')
plt.show()

#%%
hist,bins = np.histogram(accidents['Number_of_Vehicles'],bins=30)




















