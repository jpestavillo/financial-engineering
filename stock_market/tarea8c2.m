clc;
clear all;
close all;
%%
data = xlsread('KnowledgeModeling.xls', 'Training_Data')
data = data';
%%

data = xlsread('KnowledgeModeling.xls', 'Clasifica' )
data = data';

%% Entrenamiento de la red. 
Iteraciones = 10

Jcost = zeros(Iteraciones,1);
NNN = zeros(Iteraciones,1);

for iter=2:size(Jcost)+1
    neuronas = iter;
    red = competlayer(neuronas);
    red.trainParam.epochs = 100;
    red = train(red,data) ;
    
    % Calculo de J 
    [J, i] = CalculoJ(data,red)
    Jcost(iter-1) = J
    NNN(iter-1) = i
end
%%
Jcost_escala = (1+(Jcost-max(Jcost))/((max(Jcost)-min(Jcost))))*(max(NNN)-min(NNN))+min(NNN)
plot([2:Iteraciones+1],Jcost_escala,'r',[2:Iteraciones+1],NNN,'b*')
%%
plot([2:Iteraciones+1],NNN)
%% Elejimos cantidad de Neuronas para la clasificación. 

neuronas = 5; %cambiar de acuerdo a grafica de codo
red = competlayer(neuronas);
red.trainParam.epochs = 1000; 
red = train(red,data) ;

% Probar el modelo con los datos. 
Y = vec2ind(red(data))
grupos = unique(Y)
%% Guardar modelo (para no tener que correrlo otra vez)
save red.mat red

%% Cargar modelo guardado 
load red.mat
%% Calculo de J 
[J,i] = CalculoJ(data,red) % i es la cantidad de neuronas que fueron utilizadas. 
%% Graficar Y
plot(vec2ind(red(data)))