%Competitivas 3

%Limpieza
clear all;
close all;
clc;

%Cargar datos
data=xlsread('base_semillas.xlsx','Hoja1','a2:g211');
data=data(:,1:end)
data=data';

%data=chemicalTargets;
%Creaci?n de la red neuronal

nn=3; %Cantidad de neuronas

red=competlayer(nn); %Crea la red competitiva
red.trainParam.epochs=50; %Definir ?pocas y otros par?metros
red=train(red,data); %entrenamiento de la red

Wf=red.IW{1,1}'; %Pesos finales

%Simulaci?n
Y=red(data);

Y=vec2ind(Y);
grupos=unique(Y);

for k=1:size(grupos,2)
    temp=data(:,Y==grupos(1,k));
    eval(sprintf('grupo%d=temp;',k));
end



plot(data(1,:),data(2,:),'b.',Wf(1,:),Wf(2,:),'rp')
j=grupo1-Wf(:,1);
sum(j)
sqrt(j.^2)
sum(j)