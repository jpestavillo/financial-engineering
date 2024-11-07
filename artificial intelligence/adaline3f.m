clear all;
close all
clc;

res=DownloadValues('CMG','03/10/2015','03/10/2016','d','history');
%% 
rnez=3;  %número de rezagos
x=[]
for k=0:nrez
    x=[x, precios(nrez+1-k:end-k)]
    %se obtiene la matriz con los riesgos 
end 

y=x(:,1)
xa=[ones(size(x,1),1), x(:,2:end)