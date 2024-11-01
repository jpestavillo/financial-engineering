clear all; % Limpia todas las variables
close all; % Cierra todas las ventanas
clc; % Limpia el espacio de trabajo

np= 500

%% Parametros

x1p=rand(np,1); %la posicion de inicio de cada particula
x1pg=0; %la posicion inicial del mejor global
x1pL=x1p; %valores iniciales de los mejores locales
vx1=zeros(np,1); %velocidad inicial de cada particula

x2p=rand(np,1); %la posicion de inicio de cada particula
x2pg=0; %la posicion inicial del mejor global
x2pL=x2p; %valores iniciales de los mejores locales
vx2=zeros(np,1); %velocidad inicial de cada particula


fxpg=1000000; %desempeño inicial del mejor global
fxpL=ones(np,1)*fxpg; %desempeño inicial de los Locales

c1=0.75; %velocidad de convergencia al mejor global
c2=0.75; %velocidad de convergencia al mejor Local
a=10000; % penalizacion
for k=1:1000
    %% ejercicio 
%fx=sqrt(.05)*x1p.^2+sqrt(0.05)*x2p.^2+a*max(-x1p,0)+a*max(-x2p,0)+a*max(20000*x1p+30000*x2p-50000,0)+a*max(2500-1000*x1p-3000*x2p,0);

fx=sqrt(.05)*x1p.^2+.05*x1p.*x2p+.05*x2p.*x1p+sqrt(0.05)*x2p.^2+...
    a*max(-x1p,0)+...
    a*max(-x2p,0)+...
    a*max(20000*x1p+30000*x2p-50000,0)+...
    a*max(2500-1000*x1p-3000*x2p,0);
    [val, ind]=min(fx); %minimo de la funcion y su posicion
    
    %determinar el mejor GLobal
    
    if val<fxpg
        x1pg=x1p(ind,1);
        x2pg=x2p(ind,1);
        fxpg=val;
    end
    
    %Determinar los mejores locales
    
    for p=1:np %para cada particula
        if fx(p,1)<fxpL(p,1); %compara el desempeño con el mejor local
            fxpL(p,1)=fx(p,1); %actualiza el desempeño 
            x1pL(p,1)=x1p(p,1);% acttualiza la posicion
            x2pL(p,1)=x2p(p,1);
        end
        
    end
    

        %%
        vx1= vx1+c1*rand()*(x1pg-x1p)+c2*rand()*(x1pL-x1p); %nueva velocidad
        x1p=x1p+vx1; %nueva posicion
        vx2= vx2+c1*rand()*(x2pg-x2p)+c2*rand()*(x2pL-x2p); %nueva velocidad
        x2p=x2p+vx2; %nueva posicion
        
end

%% ejercicio 3
%fxpg=sqrt(.05)*x1pg.^2+sqrt(0.05)*x2pg.^2

fxpg=sqrt(.05)*x1pg^2+.05*x1pg*x2pg+.05*x2pg*x1pg+sqrt(0.05)*x2pg^2
x1pg
x2pg