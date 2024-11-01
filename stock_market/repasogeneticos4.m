clear all; close all; clc; 
np= 500
x1p=rand(np,1); %s(t)
x1pg=0; %s(t) global
x1pL=x1p; %iniciales 
vx1=zeros(np,1); %v(t)
x2p=rand(np,1); %v(0)
x2pg=0; %s(0)
x2pL=x2p; %s(t)
vx2=zeros(np,1); %v(0)
x3p=rand(np,1); %v(0)
x3pg=0; %s(0)
x3pL=x1p; %v(0)
vx3=zeros(np,1); %v(0)
fxpg=1000000; %f(x) 
fxpL=ones(np,1)*fxpg; 
c1=0.5; %v(t) convergencia 
c2=0.5; %v(t) local 
a=100000 % penalizacion
for k=1:1000
    ex1=(2*x1p+x2p+.5*x3p)-400;
    ex2=(.5*x1p+.5*x2p+x3p)-(100-ex1);
    fx=x1p+x2p+x3p+a*max(400-2*x1p-x2p-.5*x3p,0)+a*max(100-ex1-.5*x1p-.5*x2p-x3p,0)+a*max(300-ex2-1.5*x2p-2*x3p,0)+a*max(-x2p,0)+a*max(-x1p,0)+a*max(-x3p,0);
    [val, ind]=min(fx); %minimo
    if val<fxpg
        x1pg=x1p(ind,1);
        x2pg=x2p(ind,1);
        x3pg=x3p(ind,1);
        fxpg=val;
    end
    for p=1:np %para cada particula
        if fx(p,1)<fxpL(p,1); %compara el desempeño con el mejor local
            fxpL(p,1)=fx(p,1); %actualiza el desempeño 
            x1pL(p,1)=x1p(p,1);% acttualiza la posicion
            x2pL(p,1)=x2p(p,1);
            x3pL(p,1)=x3p(p,1);
        end     
    end
       
        vx1= vx1+c1*rand()*(x1pg-x1p)+c2*rand()*(x1pL-x1p); 
        x1p=x1p+vx1;
        vx2= vx2+c1*rand()*(x2pg-x2p)+c2*rand()*(x2pL-x2p);
        x2p=x2p+vx2;
        vx3= vx3+c1*rand()*(x3pg-x2p)+c2*rand()*(x3pL-x3p); 
        x3p=x3p+vx3; 
end
fxpg=x1pg+x2pg+x3pg