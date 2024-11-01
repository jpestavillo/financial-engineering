# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:05:29 2017

@author: juanp y emnuel
"""

import sympy as sy

matriz=sy.Matrix([[1,-24,-20,0,0,0],[0,.5,1,1,0,12],[0,.0625,.04166667,0,1,1]])

print (matriz.rref())

