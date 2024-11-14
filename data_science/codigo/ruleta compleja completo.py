# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:03:24 2018

@author: if709274
"""
from random import randint


jugar=True
while jugar==True:
    ganancia=0
    apuesta=50
    for i in range(1,200):
        ruleta=randint(1,38)
        #print(ruleta)
        #print("estamos en la jugada", i)
        if ruleta<=2:
            #print("apuesta de",apuesta)
            ganancia=ganancia+apuesta*1.4
            print("ganas!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
            apuesta=50
            if i>20:
                break
        elif ruleta<=4:
            #print("apuesta de",apuesta)
            ganancia=ganancia+apuesta*1.2
            print("ganas!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
            apuesta=50
            if i>20:
                break
        
        elif ruleta<=8:
            #print("apuesta de",apuesta)
            ganancia=ganancia+apuesta*.4#71428571)
        elif ruleta<=18:
            #print("apuesta de",apuesta)
            ganancia=ganancia+apuesta*.2
            
        elif ruleta<=30:
            #print("apuesta de",apuesta)
            ganancia=ganancia
        elif ruleta<=34:
            ganancia=ganancia-.8*apuesta
            apuesta=apuesta*2
            #print("apuesta de",apuesta)
            print("pierdes------------------------------")
            if apuesta==400:
                print("perdiste en la jugada", i)
                print(ganancia)
                break
        elif ruleta<=38:
            ganancia=ganancia-apuesta
            apuesta=apuesta*2
            #print("apuesta de",apuesta)
            #print("pierdes------------------------------")
            if apuesta==400:
                #print("perdiste en la jugada", i)
                #print(ganancia)
                break
        print (ganancia)
    print("en la jugada",i, "ganaste",ganancia)
