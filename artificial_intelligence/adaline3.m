clear all;
close all
clc;

res=downlodValues('CMG','03/10/2015','03/10/2016','d','history');
%% 
rnez=3;  %n�mero de rezagos
x=[]
for k=0:nrez