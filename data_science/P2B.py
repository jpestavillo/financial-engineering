# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd
from mylib import mylib

#%%
data_dir = '../Data/Vehicles_2015.csv'
#data_dir = 'G:\CDIN_O18\Data\Vehicles_2015.csv'
#data_dir = 'Vehicles_2015.csv'
vehicles = pd.read_csv(data_dir)

data_dir = '../Data/Accidents_2015.csv'
accidents = pd.read_csv(data_dir)
data_dir = '../Data/Casualties_2015.csv'
casualties = pd.read_csv(data_dir)


#%% Consultas sencillas de informacion
Num_by_Date = pd.DataFrame(pd.value_counts(accidents['Date']))
vehicles_day = pd.DataFrame(accidents.groupby(['Date'])['Number_of_Vehicles'].sum())
casualties_day = pd.DataFrame(accidents.groupby(['Date'])['Number_of_Casualties'].sum())
vehicles_casualties = Num_by_Date.join(vehicles_day).join(casualties_day)

#%% 
vehicle_by_day = accidents.groupby(['Day_of_Week'])['Number_of_Vehicles'].sum()
vehicle_by_time = accidents.groupby(['Time'])['Number_of_Vehicles'].sum()
vehicle_by_day_time = accidents.groupby(['Day_of_Week','Time'])['Number_of_Vehicles'].sum()
vehicle_by_position = accidents.groupby(['Latitude','Longitude'])['Number_of_Vehicles'].sum()

#%%
import matplotlib.pyplot as plt
plt.hist(accidents['Latitude'][accidents['Latitude'].isnull()==False],bins=30)
plt.xlabel('Latitude')
plt.ylabel('Num_Accidents')
plt.title('Histogram_Accidents')
plt.show()

plt.hist(accidents['Longitude'][accidents['Longitude'].isnull()==False],bins=30)
plt.xlabel('Longitude')
plt.ylabel('Num_Accidents')
plt.title('Histogram_Accidents')
plt.show()

#%%
plt.hist(accidents['Longitude'][accidents['Longitude'].isnull()==False],
                   bins=30,
                   normed=True)
plt.xlabel('Longitude')
plt.ylabel('Num_Accidents')
plt.title('Histogram_Accidents')
plt.show()

#%%
plt.hist(accidents['Longitude'][accidents['Longitude'].isnull()==False],
                   bins=30,
                   normed=True,
                   cumulative=True)
plt.xlabel('Longitude')
plt.ylabel('Num_Accidents')
plt.title('Probability_Accidents')
plt.show()

#%%
plt.hist(accidents['Longitude'][accidents['Longitude'].isnull()==False],
                   bins=30,
                   normed=True,
                   histtype='step')
plt.xlabel('Longitude')
plt.ylabel('Num_Accidents')
plt.title('Probability_Accidents')
plt.show()

#%%
plt.hist(accidents['Longitude'][accidents['Longitude'].isnull()==False],
                   bins=30,
                   normed=True,
                   color='b',
                   alpha=0.1)
plt.hist(accidents['Latitude'][accidents['Latitude'].isnull()==False],
                   bins=30,
                   normed=True,
                   color='r')
plt.xlabel('Longitude')
plt.ylabel('Num_Accidents')
plt.title('Probability_Accidents')
plt.show()

#%% Forma alternativa
hist,bins = np.histogram(accidents['Longitude'][accidents['Longitude'].isnull()==False],bins=30)



















