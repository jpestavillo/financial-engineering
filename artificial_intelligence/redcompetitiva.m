%redes competitivas
%clasificacion

clear all;
close all
clc;

%cargar datos 
load datos.mat;
data=datos1;

plot(data(1,:),data(2,:),'.') % no necesario