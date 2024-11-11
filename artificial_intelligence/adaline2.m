clear all;
close all;
clc;

%funcion a identificar 

x=rand(100,1); %muestra 100 aleatorios 
y=10+3*x+x.^2+4*x.^4;
%solo para verificar el funcionamiento del algoritmo

n=size(x,1); %dimensiónde las filas dex(cantidad de datos)

%construir x*
xa=[ones(n,1)];

for k=1:4 
    xa=[xa,x.^k]
    wmc=inv(xa'*xa)*xa'*y;
    yg_mc=xa*wmc;
    e=y-yg_mc;
    j(k,1)=e'*e/(2*n);
end
plot(j,'red')
xlabel('grado de polinomio')
ylabel('j(x,w)')
%plot(