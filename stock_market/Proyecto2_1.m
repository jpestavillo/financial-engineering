%% _____________________ Proyecto dos _____________________________________
% ---------------------- Modelo 1 -----------------------------------------
% Rodrigo de la Peña
% Diana Chavez
% Francisco Yasaka
%% ____________________ Limpeiza General __________________________________
clear all;
close all;
clc;
%% ___________________ Obtención de datos _________________________________
datos = xlsread('proyecto1.xls','Model1','a2:e313');

data = [datos(:,1) datos(:,2) datos(:,3) datos(:,4) datos(:,5)];

n = 4

G0 = data(data(:,n)==0,1:2);    %Grupo Cero
G1 = data(data(:,n)==1,1:2);    %Grupo Uno
%% ________________ Regresión Logística ___________________________________
X = data(:,1:n);
Y = data(:,n+1);
m = size(X,1);
 
ngrado = 4 ;
[Xa,coef] = func_polinomio(X,ngrado);

W = zeros(size(Xa,2),1);

[J,dJdW] = func_costo(W,Xa,Y);

options = optimset('GradObj', 'on', 'MaxIter', 1000);
[Wopt,Jopt] = fminunc(@(W)func_costo(W,Xa,Y),W,options);

%% ___________________ Simulación del modelo obtenido _____________________
V = Xa*Wopt;
Yg = 1./ (1+exp(-V));
Yg = (Yg>=.5);  %Función lógica (si cumple da 1, si no 0)

TP = sum((Y==1)&(Yg==1));   %Verdaderos Positivos
TN = sum((Y==0)&(Yg==0));   %Verdaderos Negativos
FP = sum((Y==0)&(Yg==1));   %Falsos Positivos
FN = sum((Y==1)&(Yg==0));   %Falsos Negativos

Accu = (TP+TN)/(TP+TN+FP+FN);   %Exactitud
Pre = TP/(TP+FP);    %Precisión
Rec = TP/(TP+FN);   %Recall

Accu 
Pre 
Rec
%% ____________________ Predicción ________________________________________
 Pred= xlsread('proyecto1.xls','Hoja3','l9:u12');
 Xa = func_polinomio (Pred,ngrado);
 V = Xa*Wopt;
 Yg = 1./(1+exp(-V));
 Yg = round(Yg);
 Default= Yg

