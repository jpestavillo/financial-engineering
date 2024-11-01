%Limpieza general
clear all;
close all;
clc;

%% parteb
data=xlsread('Datainmuno.xlsx','Hoja1','a2:h91');
% data=xlsread('Datainmuno.xslx','Hoja1','a2:h91');
X=data(:,1:7);
Y=data(:,8);



%% Graficado de datos (Se debe BORRAR)
%G0=data(data(:,8)==0,1:2); %Grupo 0
%G1=data(data(:,8)==1,1:2); %Grupo 1
% 
% plot(G0(:,1),G0(:,2),'bo',G1(:,1),G1(:,2),'rx')

%% Regresi?n Log?stica
% X=data(:,1:2);
% Y=data(:,3);
n=size(X,1); %Cantidad de datos

%Xa=[ones(n,1) X X.^2];
Xa=func_polinomio(X,2);
W=zeros(size(Xa,2),1); %Pesos iniciales
[J,dJdW]=fun_costob(W,Xa,Y); %Calculo de J y W

options=optimset('GradObj','on','MaxIter',1000);

[Wopt,Jopt]=fminunc(@(W)fun_costob(W,Xa,Y),W,options);

%% Simulaci?n del modelo obtenido
V=Xa*Wopt;
Yg=1./(1+exp(-V));
%Yg=(Yg>=0.5); %Coniverte en unos y ceros
Yg=round(Yg);
TP=sum((Y==1)&(Yg==1)); %True Positive
TN=sum((Y==0)&(Yg==0)); %True Negative
FP=sum((Y==0)&(Yg==1)); %False Positive
FN=sum((Y==1)&(Yg==0)); %False Negative

Accu=(TP+TN)/(TP+TN+FP+FN); %Exactitud
Prec=TP/(TP+FP); %Precisi?n
Rec=TP/(TP+FN); %Recall

[Accu Prec Rec]

