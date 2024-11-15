function biseccion cresciente
f=input ('favor de ingresar la funcion:','s') %s es para una letra o número
x0=input('favor de ingresar x0')  %s  es para string = letra , no número 
x1=input('Favor de ingresar x1')
erra=input('favor de ingresar el error')

M(1,1)=0 
M(1,2)=x0
M(1,3)=x1
xm=(x0+x1)/2
M(1,4)=xm
x=xm
y=eval(f)
M(1,5)=y
M(1,6)=1

n=2
erroab=1
while errorab>erra
    M(n,1)=M(n-1)+1
    if M(1,2) <0
        M(n,2)=M(n-1,2)
        M(n,3)=M(n-1,4)
    elseif M(1,2)>0
        M(n,2)=M(n-1,4)
        M(nm3)=M(n-1,3)
    end
    xm=M(n,2)+M(n,3)/2
    x=xm
    M(n,4)=xm
    y=eval(f)
    M(1,5)=y
    errorab=abs(M(n,4)-M(n-1,4)/M(n,4))
    M(n,6)=errorab
    n=n+1
end
itera=M(n-1,1);
error1=M(n-1,6);
raiz=M(n-1,4);

fprintf('el valor de tu raiz es de %f,  alcanzando en la iteracion %d, con un error relativo de %f', raiz1, itesra,error1)





while 