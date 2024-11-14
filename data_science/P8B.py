# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:12:13 2018

@author: riemannruiz
"""

import pandas as pd
from datetime import datetime
import string
from mylib import mylib

#%% Importar los datos
dirty = pd.read_csv('../Data/dirty_data.csv')

#%% Remover signos puntuación
def remove_punctuation(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x

#%% Remover digitos
def remove_digits(x):
    try:
        x = ''.join(ch for ch in x if ch not in string.digits)
    except:
        pass
    return x

#%% Remover espacios en blanco
def remove_whitespace(x):
    try:
        x = ''.join(x.split())
    except:
        pass
    return x

#%% Remplazar texto
def replace_text(x,to_replace,replacement):
    try:
        x = x.replace(to_replace,replacement)
    except:
        pass
    return x

#%% Convertir a mayusculas
def uppercase_text(x):
    try:
        x = x.upper()
    except:
        pass
    return x

#%% Convertir a minusculas
def lowercase_text(x):
    try:
        x = x.lower()
    except:
        pass
    return x

#%% dejar solo digitos
def digits(x):
    try:
        x = ''.join(ch for ch in x if ch in string.digits)
    except:
        pass
    return x
            

#%% Aplicar las funciones
dirty.people = dirty['people'].apply(remove_punctuation).apply(lowercase_text).apply(remove_digits)
dirty.people = dirty.people.apply(replace_text,args=(' d','')).apply(replace_text,args=('aa','a'))

#%% Limpiar columna marital
import numpy as np

idx = dirty.marital.isnull()
dirty.marital[idx] = 'missing'
dirty.marital = dirty.marital.apply(uppercase_text)

dirty.ssn = dirty.ssn.apply(digits)
#%%
def ceros_ssn(x):
    try:
        x=str(x)
        while (len(x)<10):
            x = '0'+x
    except:
        pass
    return x
dirty.ssn = dirty.ssn.apply(ceros_ssn)
dirty.ssn = dirty.ssn.apply(replace_text,args=('nan','000'))
















