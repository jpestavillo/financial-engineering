% Limpieza
clear all;
close all;
clc;

%Cargar datos
load cancer_de_Mama.mat
data = cancerMama'

%% 
%Creaci?n de la red neuronal

nn=5; %Cantidad de neuronas

red=competlayer(nn); %Crea la red competitiva
red.trainParam.epochs=100; %Definir ?pocas y otros par?metros
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

%%
%J
%J
%J
a=grupo1-Wf(:,1) 
c=a.^2
d=sum(c)
e=sqrt(d)
f=sum(e)
g=f/size(e,2)

a2=grupo2-Wf(:,2) 
c2=a2.^2
d2=sum(c2)
e2=sqrt(d2)
f2=sum(e2)
g2=f2/size(e2,2)

a3=grupo3-Wf(:,3) 
c3=a3.^2
d3=sum(c3)
e3=sqrt(d3)
f3=sum(e3)
g3=f3/size(e3,2)

a4=grupo4-Wf(:,4) 
c4=a4.^2
d4=sum(c4)
e4=sqrt(d4)
f4=sum(e4)
g4=f4/size(e4,2)

a5=grupo5-Wf(:,5) 
c5=a5.^2
d5=sum(c5)
e5=sqrt(d5)
f5=sum(e5)
g5=f5/size(e5,2)

a6=grupo6-Wf(:,6) 
c6=a6.^2
d6=sum(c6)
e6=sqrt(d6)
f6=sum(e6)
g6=f6/size(e6,2)

a7=grupo7-Wf(:,7) 
c7=a7.^2
d7=sum(c7)
e7=sqrt(d7)
f7=sum(e7)
g7=f7/size(e7,2)

j=(g+g2+g3+g4+g5+g6+g7)/7