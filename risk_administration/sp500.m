clear all;
close all;
clc;
%este codigo usa los precios de cualquier activo durante 3 años,saca sus
%rendimientos, con los primeros 2 años entrena el modelo garch y con el
%tercero empieza a calibrarse para poder correrlo para el garch 

precios=xlsread('sp500final.xlsx','d','B2:B765');
rends=price2ret(precios);
Modelogarch=garch(1,1);
 
for n=500:length(rends)
    Mgarchajustado{n}=estimate(Modelogarch,rends(n-499:n));
    varianza{n}=forecast(Mgarchajustado{n},1,'Y0',rends(n-249:n));
    
end

