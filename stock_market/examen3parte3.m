clear all
close all;
clc;

%Cargar datos
load WifiData.mat 


data=WifiData;

X=data(:,1:7)';
Y=data(:,8)';
cv = cvpartition(Y,'holdout',0.1);
% holdout: divide aleatoriamente las observaciones en un conjunto de datos
% de entrenamiento y prueba, usando la información de la clase del grupo.
% Datos de entrenamiento
Xtrain = X(:,training(cv));
Ytrain = Y(training(cv));
% Datos de prueba.
Xtest = X(:,test(cv));
Ytest = Y(test(cv));
%ndat=round(.75*size(Y,2)); %Cantidad de datos para entrenar
n=size(Xtrain,1); %C
%Ytrain=Y(:,1:n);
%Xtrain=X(:,1:n);

%Creaci?n del modelo neuronal

red=feedforwardnet(10);

red.trainFcn='trainrp' 
%Para clasificaci?n Supervisada usar trainscg
%o usar trainrp

red=train(red,Xtrain,Ytrain);

%Simulaci?n
Yg=red(X);

G0=data(data(:,3)==0,1:2);%Grupo 0
G1=data(data(:,3)==1,1:2); %Grupo 1

%Ygr=round(Yg);
Ygr=Yg>=.5
Ygr=double(Ygr)

G0p=data(Ygr==0,8);
G1p=data(Ygr==1,8);
Yg=red(test)
nuevo=[]
for i=1:2000
    if Y(i)==1
        nuevo(i,1)=1
    else 
        nuevo(i,1)=0
    end
        if Y(i)==2
        nuevo(i,2)=1
    else 
        nuevo(i,2)=0
        end
        if Y(i)==3
        nuevo(i,3)=1
    else 
        nuevo(i,3)=0
        end
        if Y(i)==4
        nuevo(i,4)=1
    else 
        nuevo(i,4)=0
    end
   
end 
y1=data(Y==1,8);
y2=data(Y==2,8);
y3=data(Y==3,8);
y4=data(Y==4,8);

TP=sum((Y==1)&(Yg==1)); %True Positive
TN=sum((Y==0)&(Yg==0)); %True Negative
FP=sum((Y==0)&(Yg==1)); %False Positive
FN=sum((Y==1)&(Yg==0)); %False Negative

Accu=(TP+TN)/(TP+TN+FP+FN); %Exactitud
Prec=TP/(TP+FP); %Precisi?n
Rec=TP/(TP+FN); %Recall

[Accu Prec Rec]