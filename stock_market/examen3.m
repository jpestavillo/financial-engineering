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
X=data(:,[1 2 3 4 5 6]);
%mar = max(Y)
%for i =1:sze(2)
%    dummyf(i,Testgr(i))= 1;
    %i = i+1;
%end
%X=housel((1:3,:),((5:13,:));
%% CV partition
% cv = cvpartition(Y,'holdout',0.15);
% % holdout: divide aleatoriamente las observaciones en un conjunto de datos
% % de entrenamiento y prueba, usando la información de la clase del grupo.
% % Datos de entrenamiento
% Xtrain = X(:,training(cv));
% Ytrain = Y(training(cv));
% % Datos de prueba.
% Xtest = X(:,test(cv));
% Ytest = Y(test(cv));
% n=size(Xtrain,1); %Cantidad de datos
%%
ndat=round(0.85*908); %Cantidad de datos a tomar

% Separaci?n en conjuntos de entrenamiento
Xtrain=X(1:ndat,:);
Ytrain=Y(1:ndat,:);

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
Xn = [2.53; .754; 1.115; 2; 1; 1.634];
Yn = red(Xn)