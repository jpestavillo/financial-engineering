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
%plot(x,y,'b',x,yg_mc,'r.') % estalinea plotea pero no se si esta bien 
%%gradiente descendiente 

xa=ones(n,1);
for k=1:2 
    xa=[xa x.^k];
end 
wmc=inv(xa'*xa)*xa'*y; %w de minimos cuadrados 
%solo para comparar contra gradiente 
wgd=rand(size(xa,2),1); %pesos inicialesaleatorios 
eta=1.2; %velocidad de convergencia 

for k=1:100000
    yg_gd=xa*wgd;
    e=y-yg_gd;
    j(k,1)=(e'*e)/(2*n);
    djdw=e'*xa/n;
    wgd=wgd-eta*djdw';
    
end
yg_mc=xa*wmc; %solo para comparar 
yg_gd=xa*wgd;
subplot(1,2,1);
plot(x,y,'b.',x,yg_mc,'r.',x,yg_gd,'g.')
subplot(1,2,2)
plot(j,'b')
[wmc wgd]
