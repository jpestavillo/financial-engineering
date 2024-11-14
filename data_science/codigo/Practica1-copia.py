# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import numpy as np

from mylib import mylib

dir_file = '../data/coches.csv'
vehicles= pd.read_csv(dir_file)

dir_file = '../data/accidentes.csv'
accidentes = pd.read_csv(dir_file)

dir_file = '../data/casualties.csv'
casualities = pd.read_csv(dir_file)

mireporte1= mylib.dqr(vehicles)
mireporte2= mylib.dqr(casualities)
mireporte3=mylib.dqr(accidentes)






 






















