# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import string
from datetime import datetime

#%% Importar la base de datos
data = pd.read_csv('../Data/dirty_data.csv')

#%% Remover signos puntuacion
def remove_punctuation(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x

#%% Remover numeros del texto
def remove_digits(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.digits)
    except:
        pass
    return x

#%% Remover espacios en blanco
def remove_whitespaces(x):
    try:
        x = ''.join(x.split())
    except:
        pass
    return x

#%% Convertir todo a mayusculas
def uppercase_text(x):
    try:
        x = x.upper()
    except:
        pass
    return x

#%% Convertir todo a minusculas
def lowercase_text(x):
    try:
        x = x.lower()
    except:
        pass
    return x

#%% Reemplazar texto
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x



#%%
data.people = data.people.apply(remove_punctuation).apply(remove_digits).apply(uppercase_text)
data.people = data.people.apply(replace_text,args=('AA','A'))

data['marital'] = data['marital'].apply(uppercase_text).apply(replace_text,args=('nan','MISSING'))
data['marital'][data['marital'].isnull()]='MISSING'

data.ssn = data.ssn.apply(remove_punctuation).apply(remove_whitespaces)
data.ssn = data.ssn.apply(replace_text,args=('a',''))














