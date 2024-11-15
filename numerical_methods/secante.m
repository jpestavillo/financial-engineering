function secante 
f=input('ingresar tu funcion','s') 
x0=input('hagame el esplendido favor de inscribir su x0') 
x1=input('hagame el favorsote de poner su x1')
era=input('meta el era (error)')
erc=1
iteracion=0
M(1,1)=iteracion 
M(1,2)=x0
M(1,3)=x1
x=M(1,2)
y=eval(f)
M(1,4)=y
x=x1
y=eval(f)
M(1,5)=y
x2=(M(1,3)-(M(1,5)*(M(1,3)-M(1,2))))/(M(1,5)-M(1,4))
M(1,6)=x2
M(1,7)=erc
i=2

while erc > era 
iteracion=iteracion+1
M(i,1)=iteracion
M(i,2)=M(i-1,3)

M(i,3)=M(i-1,4)
x=M(i,2)
y=eval(f)
M(i,4)=y

x=M(i,3);
M(i,5)=y
x2=(M(i,3)-(M(i,5)*(M(i,3)-M(i,2))))/(M(i,5)-M(i,4)) %chido
M(i,6)=x2
erc=(M(i,6)-M(i-1,6))/M(i-1,6)
M(i,7)=erc

i=i+1;
    
end   

end 