# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:34:12 2017

@author: juanp
"""

import pandas as pd 
import random 
import matplotlib.pyplot as mpl
import numpy as np




ecuacion=
regresionlineal=np.zeros(666)
datos= pd.read_excel('C:/Users/juanp/Desktop/base de datos cool.xlsx',sheetname='IED Jalisco Sectores',skiprows=5,)
originales= pd.read_excel('C:/Users/juanp/Desktop/base de datos cool.xlsx',sheetname='IED Jalisco Sectores',skiprows=5,)
segmentoutil=datos.iloc[0:18,:]  

datosna = datos.dropna()  #Elimina los datos en blanco o con valor 'nan'

#estas son las graficas de rayitas
mpl.plot(segmentoutil.index,segmentoutil[2008],color='r')
mpl.plot(segmentoutil.index,segmentoutil[2012],color='g')
mpl.plot(segmentoutil.index,segmentoutil[2016],color='orange')



#estas son las grafias de puntitos
mpl.scatter(segmentoutil.index,segmentoutil[2010],color='b')
mpl.scatter(segmentoutil.index,segmentoutil[2014],color='r')




for i in range(1,10):
    regresionlineal[i]=pendiente*i
 
                    
                    
                    
#vacas=pd.read_excel('C:/Users/juanp/Desktop/Farm_prices',sheetname='beef')

pd.read_excel('C:/Users/juanp/Desktop/Farm_prices')
grafica=np.zeros((666,666))

ordenada=75.9
n=564

pendiente=.528
r=.883


for i in range(1,n):
    ecuacion[i,0]=pendiente*i+ordenada
    
