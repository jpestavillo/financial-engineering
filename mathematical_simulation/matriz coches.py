
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
                                    elif simulacion[i,(columna31)+contador,k]<prd2:
                                        simulacion[i,(columna11)+contador,k]=3
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                    elif simulacion[i,(columna31)+contador,k]<prd3:
                                        simulacion[i,(columna11)+contador,k]=4
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                                    elif simulacion[i,(columna31)+contador,k]<prd4:
                                        simulacion[i,(columna11)+contador,k]=5
                                        simulacion[i,5,k]=simulacion[i,5,k]+1
                            
                    if simulacion[i,columna11+contador,k]>1:
                        simulacion[i+1,columna11+contador,k]= simulacion[i,(columna11)+contador,k]-1       
                    if simulacion[i,columna11+contador,k]>2:
                        simulacion[i+1,2,k]=simulacion[i+1,2,k]+1
                    if simulacion[i,columna11+contador,k]==1:
                        simulacion[i+1,columna11+contador,k]=1                      
                        
                            
                        
                     
                    
                    
                    
                    
                simulacion[i,5,k]=0
                simulacion[i,8,k]=simulacion[i,3,k]  
