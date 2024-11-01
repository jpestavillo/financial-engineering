clear all;
close all
clc;

res=xlsread('tarea','Problema 1','A2:A25');
%% 
nrez=3;  %número de rezagos
x=[]
for k=0:nrez
    x=[x, res(nrez+1-k:end-k)]
    %se obtiene la matriz con los riesgos 
end 

y=x(:,1)
xa=[ones(size(x,1),1), x(:,2:end)]

ntrain=round(.6*size(xa,1));
