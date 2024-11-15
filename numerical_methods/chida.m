function chida
a=input('ingresa el valor inicial de la matriz')
b=input('ingrese el valor final   de la matriz')


y=input('ingresa tu funcion :','s')
M=[[1,2],[3,4]]
matrix= a:b
f= eval(y)
n=0
for i=1:2
    for j=1:2
        M(i,j)=j+2*n
        j=j+1
    end
    n=n+1
end
disp(M)
