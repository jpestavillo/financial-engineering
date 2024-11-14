# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:55:27 2018

@author: juanp
"""
import pandas as pd
from random import randint
#ruleta 2 

perder=12/38
empatar=8/38
ganarpoco=14/38
ganarmucho=4/38

data=pd.read_excel('../data/ruleta.xlsx')
apuesta_inicial=50
for i in range(50):
    ruleta=randint(1,36)
    
    print ruleta 