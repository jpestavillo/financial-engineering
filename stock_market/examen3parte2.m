% Limpieza
clear all;
close all;
clc;

%Cargar datos
data=xlsread('qsar_fish_toxicity.xlsx','qsar_fish_toxicity','a1:g908');

%housel = house
%mar = max(house(4,:));
%houser = house';
%marp = cumsum(houser(:,4));

Y=data(:,7);
X=data(:,1:6);

ndat=round(0.85*908); %Cantidad de datos a tomar

% Separaci?n en conjuntos de entrenamiento
Xtrain=X(1:ndat,:);
Ytrain=Y(1:ndat,:);
%Creaci?n de la red multicapa
red=feedforwardnet([2 3 3]);
%Definir los par?metros de entrenamiento
red.trainFcn='trainlm' %lm entrenar por Levenberg-Marquart 
%Traingd entrenar con Gradiente Descendente

red=train(red,Xtrain,Ytrain); %Qu? red, qu? datos de entrada 
%y qu? datos de salida

%Simulaci?n
Yg=red(X); %C?lculo de Estimaciones