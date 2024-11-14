import pandas as pd
import numpy as np
from mylib import mylib
from datetime import datetime
import string
#%%
data=pd.read_csv('../data/dirty_data.csv')

#%% remover signos de puntuación 
def remover_punctuation(x):
    try:
        x=''.join(ch for ch in x if ch not in string.punctuation)
    except:
        pass
    return x

#%% remover numeros del texto 
def remove_digits(x):
    try:
        x=''.join(ch for ch in x if ch not in string.digits)
    except:
        pass
    return x
#%% remover espacios en blanco
def remove_whitespaces(x):
    try:
        x=''.join(x.split())
    except:
        pass
    return x
#%% convertir todo a mayusculas 
def uppercase_text(x):
    try:
        x=x.upper()
    except:
        pass
    return x

#%% convertir todo a minúsculas 
def lower_case(x):
    try: 
        x=x.lower()
    except: 
        pass
    return x 
#%%
def replace_text(x,to_replace,replacement):
    try:
        x=x.replace(to_replace,replacement)
    except:
        pass
    return x


#%%
data.people=data.people.apply(remover_punctuation).apply(remove_digits).apply(uppercase_text).apply(lower_case)
data.people=data.people.apply(replace_text,args=('AA','A'))

data['marital']=data['marital'].apply(uppercase_text).apply(replace_text,args=('na','MISSING'))
data['marital'][data['marital'].isnull()]='MISSING'
     
data.ssn=data.ssn.apply(remover_punctuation).apply(remove_whitespaces)
data.ssn=data.ssn.apply(replace_text,args=('a',''))

