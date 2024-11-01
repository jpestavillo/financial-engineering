import numpy as np
import random
"datos problema"
pr0=.1
pr1=.2
pr2=.45
pr3=.75
pr4=1

prd1=.4
prd2=.75
prd3=.9
prd4=1

numerooptimo=0
numerooptimo2=0
incisob=0
incisob2=0
numerodiasmayor=0

c=0
c1=0 
#%%
"estructura"
"columna0=aleatorionumero"
"columna1=rentahoy"
"columna2= rentados anteriormente se usa for de columna 31-46"
"columna3=disponible = k-rentados  (estos que sobran restan 50 a ganancia"

"columna6= interes aleatorio"
"columna8 sobra de coche"
"columna9=perdidaporfaltadecoche"
"columna10=ganancia"

"columna11-27 existencia carros  (usamos for para llenar esos espacios) "
"columna31-46 0=disponibilidad  numero=diasparaqueesterentado"   
"disponibles=existentes-rentados)"
"columna 51-66 aleatorios dias "
"columna 71-86 numero de dias"
"columna 91-106 dias restantes"
"columna 111-126 "
"columna 131-146 ganancia"
#%%

"declaramos variables"
"k=numero de coches"
"day=numero de dia corriendo"
for n in range (1,2,1):  
        "veces que se ejecuta la simulacion"
        simulacion=np.zeros((366,127,17))
        for k in range (1,17,1): 
            columna11=11
            columna31=31
            columna51=51
            columna71=71
            columna91=91
            columna111=111
            columna131=131
            gananciatotal=0
            perdidatotal=0
            resultado=0
            c=0
            a=0
            b=0
            for i in range (0,365,1):
                "dias"
                simulacion[i,0,k]=random.random()
                
                if  simulacion[i,0,k]<pr0:
                    simulacion[i,1,k]=0
                elif simulacion[i,0,k]<pr1:
                    simulacion[i,1,k]=1
                elif simulacion[i,0,k]<pr2:
                    simulacion[i,1,k]=2   
                elif simulacion[i,0,k]<pr3:
                    simulacion[i,1,k]=3
                elif simulacion[i,0,k]<pr4:
                    simulacion[i,1,k]=4   
                
                simulacion[i,6,k]=random.random()
                simulacion[i,6,k]=(1.5+simulacion[i,6,k])/100
                simulacion[0,2,k]=0
                simulacion[i,3,k]=(k-simulacion[i,2,k]-simulacion[i,1,k])
                
                if simulacion[0,3,k]>0:
                    simulacion[0,4,k]=k-simulacion[0,3,k]
                if simulacion[0,3,k]==0:
                    simulacion[0,4,k]=k
                if simulacion[0,3,k]<0:
                    simulacion[0,4,k]=k
                        
                
                if simulacion [i,3,k]<0:
                    simulacion[i,9,k]=simulacion[i,3,k]
                    simulacion[i,3,k]=0
                    simulacion[i,5,k]=simulacion[i,10,k]
                if simulacion [i,3,k]==0:
                    simulacion[i,10,k]=k
                    simulacion[i,5,k]=simulacion[i,10,k]
                if simulacion[i,3,k]>0: 
                    simulacion[i,10,k]=k-simulacion[i,3,k]
                    simulacion[i,5,k]=simulacion[i,10,k]
               
                
                
                if i>0:    
                    simulacion[i,4,k]=simulacion[i-1,3,k]-simulacion[i,3,k]  
                    if simulacion[i,4,k]<0:
                        simulacion[i,4,k]=0
                if i==0:
                    for contador2 in range(0,k,1):
                        simulacion[0,columna11+contador2,k]=1
                simulacion[i,5,k]=0
                
                
                
                
                for contador in range (0,k,1):
                    if simulacion[i,columna11+contador,k]>1:
                        simulacion[i,5,k]=simulacion[i,5,k]+1
                        
                    if simulacion[i,5,k]<simulacion[i,10,k]:
                       
                            if simulacion[i,columna11+contador,k]==1:                
                                
                
                                    simulacion[i,(columna31)+contador,k]=random.random()
                                    if simulacion[i,(columna31)+contador,k]<prd1:
                                        simulacion[i,(columna11)+contador,k]=2
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                        b=b+simulacion[i,(columna11)+contador,k]-1    
                                        numerodiasmayor=numerodiasmayor+1
                                    elif simulacion[i,(columna31)+contador,k]<prd2:
                                        simulacion[i,(columna11)+contador,k]=3
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                        b=b+simulacion[i,(columna11)+contador,k]-1    
                                        numerodiasmayor=numerodiasmayor+1
                                    elif simulacion[i,(columna31)+contador,k]<prd3:
                                        simulacion[i,(columna11)+contador,k]=4
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                        b=b+simulacion[i,(columna11)+contador,k]-1    
                                        numerodiasmayor=numerodiasmayor+1
                                    elif simulacion[i,(columna31)+contador,k]<prd4:
                                        simulacion[i,(columna11)+contador,k]=5
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                        b=b+simulacion[i,(columna11)+contador,k]-1    
                                        numerodiasmayor=numerodiasmayor+1
                           
                                
                    if simulacion[i,columna11+contador,k]>1:
                        simulacion[i+1,columna11+contador,k]= simulacion[i,(columna11)+contador,k]-1       
                    if simulacion[i,columna11+contador,k]>2:
                        simulacion[i+1,2,k]=simulacion[i+1,2,k]+1
                    if simulacion[i,columna11+contador,k]==1:
                        simulacion[i+1,columna11+contador,k]=1                      
                        
                            
                        
                c=c+simulacion[i,10,k]    
                
                a=a+ simulacion[i,1,k]  
                    
                    
                  
                simulacion[i,5,k]=0
                simulacion[i,8,k]=simulacion[i,3,k]  
                perdidatotal=perdidatotal+simulacion[i,9,k]*-200+ simulacion[i,3,k]*(50)
                gananciatotal=gananciatotal+simulacion[i,10,k]*350
                resultado=gananciatotal-perdidatotal
                if (resultado)>incisob:
                    numerooptimo=k
                    incisob=(resultado)
                if (resultado-75000*k*(1+simulacion[i,6,k]))>incisob2:
                    numerooptimo2=k
                    incisob2=(resultado-75000*k*(1+simulacion[i,6,k]))
                
            print ("ganancia",k,"coches ","=",resultado-75000*k)
            print("inciso a con",k,"coches es",a/365)
            print("inciso b con",k,"coches es",b/numerodiasmayor)
            
            print("inciso c con",k," coches es ",c/365)
        print("el numero optimo de coches es",numerooptimo, "con ganancias sin contar costo anual es $", incisob)
        print("el numero optimo de coches es",numerooptimo2,"con ganancias menos el costo anual",incisob2)
        
  
#%%

print("el numero optimo de coches en esta simulacion es de ",numerooptimo,"ya que tienes ganancias de",incisob)
print ("pongame 100 profe,duré mucho haciendolo")
