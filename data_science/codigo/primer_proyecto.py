from mylib import mylib 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from  scipy.cluster import hierarchy


data= pd.read_csv('../data/datos_matricula_carrera_2.1718_feb-jul_2018.csv', encoding='latin1')
data =data.iloc[:-1,:-1]
data=data.drop(['Entidad','Periodo'],axis=1)
reporte_calidad = mylib.dqr(data)
 
 #%%
modelo = pd.value_counts(data['Modelo educativo'])
carreras=pd.value_counts(data['Carrera Profesional Tecnico -Bachiller'])
plantel=pd.value_counts(data['Plantel'])

d = sorted (data.Matricula, reverse= True)

r  = pd.DataFrame(data= d, columns = ['Matricula'], index = data['Carrera Profesional Tecnico -Bachiller'])

indice = pd.DataFrame(plantel.index.values)
indice = pd.DataFrame(np.array(indice))
carrera = pd.DataFrame(data['Carrera Profesional Tecnico -Bachiller'].index.values)

D=data[['Plantel','Carrera Profesional Tecnico -Bachiller']]


#%%
len(r)
#%%
r.index = np.arange(1,83)
r['Matricula'].plot()

plt.xlabel("Carreras")
plt.ylabel("Matriculas")
plt.figure
plt.show()  


#%% modelos educativos
modelo.plot.bar(title = 'Modelos educativos')
plt.ylabel('# carreras')
plt.xlabel('Modelo')




#%% Matriculas por plantel
indice = np.array(indice)
arr = []
data.index= data.Plantel
for k in indice:
    da= data.loc[k]
    arr.append(sum(da.Matricula))
arr = np.array(arr)
matriuclaxplantel = pd.DataFrame(indice)
matxpl= pd.DataFrame(columns= ['Matricula'], index = matriuclaxplantel)
matxpl['Matricula']= arr

matxpl.plot.bar(title = 'Modelos educativos')
plt.ylabel('# Matriculas')
plt.xlabel('Plantel')
#%% matricula x carrera

carrera = np.array(carrera)
arr = []
data.index= data['Carrera Profesional Tecnico -Bachiller']
for k in carrera:
    da= data.loc[k]
    arr.append(sum(da.Matricula))
arr = np.array(arr)
matriuclaxcarrera = pd.DataFrame(carrera)
matxca= pd.DataFrame(columns= ['Matricula'], index = matriuclaxcarrera)
matxca['Matricula']= arr
unique_values = pd.DataFrame(columns=['Unique_values'])
matxca.drop_duplicates().plot.bar()
#%% carrera x plantel

carreras.plot.bar()

#%%
plt.figure(1)
plt.subplot(211)
plt.plot(carreras)
plt.subplot(212)
plt.plot(matxpl)
#%% indices  carreras, planteles y modelo educativo 
indx=np.array(data.dtypes=='string')
col_names=list(data.columns.values[indx])

col_data=data[col_names]
dummy1=pd.get_dummies(data.Plantel)
dummy2=pd.get_dummies(data['Carrera Profesional Tecnico -Bachiller'])
dummy3=pd.get_dummies(data['Modelo educativo'])
dummy_maestro=[]
dummy1=dummy1.join(data.Matricula)
Z= hierarchy.linkage(dummy1,metric='euclidean',method='complete')
plt.figure(figsize=(25,15))
plt.title('dendograma')
plt.xlabel('indice de la muestra')
plt.ylabel('distancia o similitud')
dn=hierarchy.dendrogram(Z,
                        truncate_mode='lastp',p=12)

#dn=hierarchy.dendogram(z, truncate_mode='level', p=5)
plt.show()
for col in range(col_names):
    tmp= pd.get_dummies(col_data[col],
                        prefix=col)
    dummy_maestro=dummy_maestro.join(tmp)

   # ac_dummy=ac_dummy.join(tmp)
#del tmp

#data_cluster=data.Matricula.
#Z= hierarchy.linkage(data_cluster,metric='euclidean',method='complete')
#plt.figure(figsize=(25,15))
#plt.title('dendograma')
#plt.xlabel('indice de la muestra')
#plt.ylabel('distancia o similitud')
#dn=hierarchy.dendrogram(Z)
#plt.show()



    
