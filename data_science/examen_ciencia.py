import numpy as np
import pandas as pd
import string
data = pd.read_csv('../Data/dirty_Info_Alumnos_v1.csv', encoding ='latin1')
datanew = data[:]
columns = list(data.columns.values)
data =pd.DataFrame(data.rename(columns={'Combre Completo':'Nombre_Completo'}))
data =pd.DataFrame(data.rename(columns={'Num Expediente':'Num_Expediente'}))
#%% Dejar nombres correctos en mayúsculas
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x    

def remove_punctuation(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x
def remove_digits(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.digits)
    except:
        pass
    return x
def remove_digits22(x):
    try:
        x = ''.join(ch for ch in x if ch in string.digits)
    except:
        pass
    return x
def uppercase_text(x):
    try:
        x = x.upper()
    except:
        pass
    return x
def remove_whitespaces(x):
    try:
        x = ' '.join(x.split())
    except:
        pass
    return x


data.Nombre_Completo = data.Nombre_Completo.apply(replace_text, args=('¥','Ñ')).apply(replace_text, args=('_',' ')).apply(replace_text, args=('-',' ')).apply(replace_text, args=('&',' ')).apply(replace_text, args=('?',' ')).apply(remove_punctuation).apply(remove_digits).apply(uppercase_text).apply(remove_whitespaces).apply(replace_text, args=('ALFONS','ALFONSO')).apply(replace_text, args=('PEDRQ','PEDRO')).apply(replace_text, args=('RUZ','RUIZ')).apply(replace_text, args=('XX','')).apply(replace_text, args=('GUTIERREZ RAMIREZ EVELYN P','GUTIERREZ RAMIREZ EVELYN')).apply(replace_text, args=('MARTINEZ GOMEZ P TAMARA VALERIA','MARTINEZ GOMEZ TAMARA VALERIA'))
data.Telefono = data.Telefono.apply(remove_digits22)
data.Semestre= data.Semestre.apply(remove_digits22)
data.Num_Expediente= data.Num_Expediente.apply(remove_digits22)
#Si el número de expediente no tiene 6 dígitos considerarlo como “missing”.
#%% Poner Missing 
for k in range(0,48):
    if len(data.Telefono[k])<10:
        data.Telefono[k]= 'Missing'
    else:
        pass
#%%
for r in range(0,48):
    if len(str(data.Num_Expediente[r]))<6:
        data.Num_Expediente[r]= 'Missing'
    else:
        pass