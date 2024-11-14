#casino
import random
rojos=18/38
jugar=True
rondas=1
perdidas=0
ganadas=0
levantadas=0
total=0#
#%%
#regla1 no ser obvio con la estrategia y siempre seguir las reglas
#regla2 apostar con la apuesta inicial al color que haya aparecido menos
#regla3 apostar al mismo color que la apuesta inicial
#%%
for idas_al_casino in range(10000):   
    
    apuesta=50
    aguante=4
    maximo=20
    
    apuesta_base=apuesta
    fallas=2**aguante
    salir=apuesta*fallas
    dinero=(apuesta*fallas)-apuesta #6350
    base=  (apuesta*fallas)-apuesta #6350
    meta= salir+apuesta_base*15
    rondas=0
    
    while jugar==True:
        ruleta=random.random()
        
        if ruleta<= rojos:
            dinero=dinero+apuesta
            apuesta=apuesta_base
            if dinero==meta:
                ganadas=ganadas+1
                print("ya ganaste",dinero)
                total=total+((dinero-base)*.93)
                break
        if ruleta>rojos:
            dinero=dinero-apuesta
            apuesta=apuesta*2
            if apuesta==salir:
                perdidas=perdidas+1
                print(" perdiste tu dinero, te queda", dinero)
                total=total+dinero-base
                break
        if apuesta==apuesta_base and rondas==maximo:
            print("ya levantate de la mesa, tienes",dinero)
            if dinero>base:
                extra=(dinero-base)*.93
                ganadas=ganadas+1
                total=total+extra
            if dinero<=base:
                perdidas=perdidas+1
                total=total+dinero-base  
            break
        #print(dinero)
        rondas=rondas+1
        
    #print("despues de ",rondas,"rondas, ganaste $", total)
porcent_ganadas=ganadas/(ganadas+perdidas)*100
print("ganaste %", porcent_ganadas," de las veces, al final tienes  $", total)



    