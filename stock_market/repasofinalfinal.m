% Limpieza
clear all;
close all;
clc;

%Cargar datos
load house.mat
housel = house

Y=housel(14,:);
X=housel([1 2 3 5 6 7 8 9 10 11 12 13],:);
%
%% CV partition
cv = cvpartition(Y,'holdout',0.1);

% Datos de entrenamiento
Xtrain = X(:,training(cv));
Ytrain = Y(training(cv));
% Datos de prueba.
Xtest = X(:,test(cv));
Ytest = Y(test(cv));
n=size(Xtrain,1); %Cantidad de datos
%%
ndat=round(0.9*size(Y,2)); %Cantidad de datos a tomar

% Separaci?n en conjuntos de entrenamiento
Xtrain=X(:,1:ndat);
Ytrain=Y(:,1:ndat);

%Creaci?n de la red multicapa
red=feedforwardnet(10);
%Definir los par?metros de entrenamiento
red.trainFcn='trainlm' %lm entrenar por Levenberg-Marquart 
%Traingd entrenar con Gradiente Descendente

red=train(red,Xtrain,Ytrain); %Qu? red, qu? datos de entrada 
%y qu? datos de salida

%Simulaci?n
Yg=red(X); %C?lculo de Estimaciones
J=perform(red,Y,Yg)
%%
%gr'afica
%%scatter(Yg,Y, 'K*') %dichos V reales
%%xlabel("Yg")
%%ylabel("Y")
%%hold on
%%scatter(Ygtest, Ytest, "ro-")
%%hold off
%%perform(red,Y,Yg)
%perform(red,(Ygtest),Ytest)
%%
%Variables a estimar
Xn = [12.54 45 15.37 0.515 6.1621 45.8 3.3751 7 193 15.2 347.88 2.96];
Yn = red(Xn')