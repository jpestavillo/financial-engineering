function secante 
fx = input('ingrese la funcion','s')
x0 = input('x0')
x1 = input ('x1')
era = input('error')
erc = 1
iteracion = 0
M(1,1)=iteracion
M(1,2)= x0
x=x0
y = eval(fx)
M(1,4)= y
M(1,3)=x1
x = x1
y=eval(fx)
M(1,5) = y
x2 = M(1,3)-(M(1,5)*(M(1,3)-M(1,2))/M(1,5)-M(1,4))
M(1,6) =x2
M(1,7 ) = erc

i= 2

while erc >era
    iteracion = iteracion +1
    M(i,1)
    M(i,2)=M(i-1,3)
    x = M(i,2)
    y = eval(fx)
    m(i,4 ) = y
    x=M(i,3)
    y=eval(fx)
    M(i,5)=y
    x2 = M(i,3)-(M(i,5)*(M(i,3)-M(i,2))/M(i,5)-M(i,4))
    M(i,6)=x2
    erc =  (M(i,6)-M(i-1,6)(M(i,6))
    M(i,7)=erc
    i=i+1
end




end 