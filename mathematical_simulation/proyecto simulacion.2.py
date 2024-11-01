# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:57:47 2017

@author: villo el guapo
"""

import pandas as pd 
import random 
import matplotlib.pyplot as mpl
import numpy as np
import scipy.stats as stats
#%%

ordenadaorigen=0
pendiente=0
regresionlineal=np.zeros((666,666))
datos= pd.read_excel('C:/Users/juanp/Desktop/base de datos cool.xlsx',sheetname='IED Jalisco Sectores',skiprows=5,)
originales= pd.read_excel('C:/Users/juanp/Desktop/base de datos cool.xlsx',sheetname='IED Jalisco Sectores',skiprows=5,)
segmentoutil=datos.iloc[0:18,:]  
total=datos.iloc[17,1:10]
datosna = datos.dropna()  #Elimina los datos en blanco o con valor 'nan'

#estas son las graficas de rayitas
mpl.plot(segmentoutil.index,segmentoutil[2008],color='r')
mpl.plot(segmentoutil.index,segmentoutil[2012],color='g')
mpl.plot(segmentoutil.index,segmentoutil[2016],color='orange')

mpl.show()

#estas son las grafias de puntitos
mpl.scatter(segmentoutil.index,segmentoutil[2010],color='b')
mpl.scatter(segmentoutil.index,segmentoutil[2014],color='r')

mpl.show()

"m=pd.read_excel('C:/Users/juanp/Desktop/base de datos cool.xlsx',sheetname='IED Jalisco Sectores',"
pendiente=datos.resultados9[4]
ordenadaorigen=datos.resultados9[6]
print("la pendiente es",pendiente,"la ordenada al origen es",ordenadaorigen)

for i in range(1,10):
    regresionlineal[i,0]=pendiente*i+ordenadaorigen

print("esta es la grafica del total")
mpl.plot(total,color='g')
mpl.show()

print("esta es la regresion lineal")
mpl.plot(regresionlineal[1:10,0],color='b')
mpl.show()



#%%
#aqui pondre todas medidas de tendencia central

media=datos.mean()
print("los promedios de la base de datos son",media)

mediana=np.median(total)
print("esta es la mediana de los datos",mediana)

moda=stats.mode(total)
print("no hay moda")

dsvstd=np.std(total)
print("esta es la desviacion estandar de los datos",dsvstd)

varianza=np.var(total)
print("esta es la varianza de los datos",varianza)

                    
