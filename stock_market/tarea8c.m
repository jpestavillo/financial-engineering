%Red Competitva 1

%Limpieza
clear all;
close all;
clc;
% Cargar datos
%load datos1.mat;
data=xlsread('KnowledgeModeling.xls','Training_Data','a2:e259');

% plot(data(1,:),data(2,:),'.') % No necesario

% Creaci?n de la red competitiva

nn=10; %N?mero de neuronas
prom=mean(data')';

%W=[prom prom prom prom prom]; %Pesos iniciales
%W=zeros(2,5);
W=rand(size(data',2),nn);
eta=0.01; % Velocidad de convergencia

W0=W; % ?nicamente para dibujar

for nepoc=1:35
    for k=1:size(data,2)
        for j=1:nn
            %Distancia de neuronas
            distancia(1,j)=sum((data(:,k)-W(:,j)).^2);
        end
        [val,ind]=min(distancia); % ley de adaptaci?n

        W(:,ind)=W(:,ind)+eta*(data(:,k)-W(:,ind));
    end
end

Wf=W; %Pesos finales s?lo para graficar
plot(data(1,:),data(2,:),'b.',W0(1,:),W0(2,:),'r.',Wf(1,:),Wf(2,:),'rp')
