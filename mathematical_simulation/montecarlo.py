

import random
a=1
b=4
exitosos=0
fxevaludado=0
N=1000
c=0
m=100
for i in range (0,N):
    x=a+random.random()*(b-a)
    y=random.random()*m
    fx=x**3+5
    if fx<=y:
        exitosos=exitosos+1
print(exitosos)       
    