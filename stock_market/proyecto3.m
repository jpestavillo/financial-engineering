clear all;
close all;
clc;
%datos 
datos = xlsread('proyecto1.xls','model3','a2:k311');

data = [datos(:,1) datos(:,2) datos(:,3) datos(:,4) datos(:,5) datos(:,6)...
    datos(:,7) datos(:,8) datos(:,9) datos(:,10)];

n = 9 %cantidad de datos 

G0 = data(data(:,10)==0,1:2);    %Grupo Cero
G1 = data(data(:,10)==1,1:2);    %Grupo Uno

    %% regresion_
X = data(:,1:n);
Y = data(:,n+1);
m = size(X,1);
 
ngrado = 2 ;
[Xa,coef] = func_polinomio(X,ngrado);

W = zeros(size(Xa,2),1);

[J,dJdW] = fun_costob(W,Xa,Y);

options = optimset('GradObj', 'on', 'MaxIter', 1000);
[Wopt,Jopt] = fminunc(@(W)fun_costob(W,Xa,Y),W,options);

%% modelo
V = Xa*Wopt;
Yg = 1./ (1+exp(-V));
Yg = (Yg>=.5);  %Función lógica (si cumple da 1, si no 0)

TP = sum((Y==1)&(Yg==1));   %Verdaderos Positivos
TN = sum((Y==0)&(Yg==0));   %Verdaderos Negativos
FP = sum((Y==0)&(Yg==1));   %Falsos Positivos
FN = sum((Y==1)&(Yg==0));   %Falsos Negativos

Accu = (TP+TN)/(TP+TN+FP+FN);   %accuracy
Pre = TP/(TP+FP);    %Precision
Rec = TP/(TP+FN);   %Recall

Accu 
Pre 
Rec

Pred= xlsread('proyecto1.xls','Hoja3','l9:u12');

 Xa = func_polinomio (Pred,ngrado);
 V = Xa*Wopt;
 Yg = 1./(1+exp(-V));
 Yg = round(Yg);

