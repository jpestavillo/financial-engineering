# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:45:22 2017

@author: juanp
"""

#maximizar z
"z=24x1+20x2"
".5x1+x2 menor a 12"
".0625x1+1/24x2 menor a 1"

import sympy as symp

a=symp.Matrix([[1,-24,-20,0,0,0],
               [0,.5,1,0,0,12],
               [0,.0625,.0416667,0,1,1]])
print (a.rref())

print("z=408")
print("x1=12")
print("x2=6")


