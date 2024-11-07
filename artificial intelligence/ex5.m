clear all; close all; clc;
np= 1000
x1p=rand(np,1); %s(t0)
x1pg=0; %s(t0) global
x1pL=x1p; %mejores locales
vx1=zeros(np,1); %v(t)
x2p=rand(np,1); %s(t0)
x2pg=0; %s(t0) global
x2pL=x1p; %mejores locales
vx2=zeros(np,1); %v(t)
fxpg=1000000; %fx
fxpL=ones(np,1)*fxpg; %fx(t0)
c1=0.75; %velocidad 1
c2=0.75; %velocidad 2 
a=10000 % penalizacion
for k=1:500
    
    %fx=-(exp(x1p+1).*(2*x1p-x1p.^2+1)-2*x1p)./(exp(x1p+1)-1).^2+a*max(-x1p-1,0)+a*max(-x1p-5,0) + a*max(x1p-5,0);
    fx=(x1p.^2+x2p.^2)./exp(x1p.^2+x2p.^2+1)%+a*max(-x2p-x1p,0);
    %esta es la primera 
    %fx=-2+a*max(x1p+1,0)+a*max(-x1p-5,0) + a*max(x1p-5,0);
    %esta es la segunda 
    [val, ind]=min(fx); %minimo de la funcion y su posicion
    if val<fxpg  % if para ver cual es mejor 
        x1pg=x1p(ind,1);
        fxpg=val;
    end
 
    for p=1:np 
        if fx(p,1)<fxpL(p,1); 
            fxpL(p,1)=fx(p,1);
            x1pL(p,1)=x1p(p,1);        
        end      
    end 
        vx1= vx1+c1*rand()*(x1pg-x1p)+c2*rand()*(x1pL-x1p);
        x1p=x1p+vx1;
       
end
fx= (x1p.^2+x2p.^2)/exp(x1p.^2+x2p.^2+1)

