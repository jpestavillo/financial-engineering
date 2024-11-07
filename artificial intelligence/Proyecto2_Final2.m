%proyecto2
clc
clear
%%
%paginas={'P2018','P2017','P2016','P2015','P2014','P2013','P2012','O2018','O2017','O2016','O2015','O2014','O2013','O2012'};
paginas={'P2018','P2017','P2016','P2015'};
%% Leer datos
for i=1:size(paginas,2)
    datos{i} = xlsread('Historico2.xlsx',paginas{i},'A1:L1000');
    data{i} = datos{i}(sum(isnan(datos{i}),2)<1,:);
end 
%% Datos test
Test =  xlsread('Historico2.xlsx','P2019 predecir','A1:L230');
%X_test = Test(:, 1:end-1);
X_test=Test(:,[1 2 3 4 5 7 8]);
%X_test=Test(:,[4 ])
Y_test = Test(:, end);

%% Sumas de calificaciones
for i = 1: size(paginas,2) 
   data{i}(:,1) = data{i}(:,2) + data{i}(:,3); 
   data{i}(:,4) = (data{i}(:,1)/160 + data{i}(:,5)/10)/2; 
end

%% Se concatenan todas las tablas en una y se seleccionan X y Y
X = [];
for i=1:size(paginas,2)
   X = [X; data{i}];
end

Y = X(:,end);
X = X(:,[1 2 3 4 5 7 8]);

%% Estadarizamos (normalización)
X = (X-mean(X,1))./std(X,1);
X_test = (X_test-mean(X_test,1))./std(X_test,1);

%% Aplicamos el modelo de MLP
red = feedforwardnet([8 7 7]); %Red de varias capas (Back Propagation), con n capas ocultas
%red = feedforwardnet(10); %Red de varias capas (Back Propagation), con n capas ocultas
red.trainfcn = 'trainscg'; %trainscg, Fcn tarindg es el metodo de entrenamiento de gradiente descenente
%Fcn tarinlm es el metodo de entrenamiento de Leverberg-Marquart
red = train(red,X',Y'); %Que red, datos de entrada y de salida

% Prediccion
Yg = round(red(X'));

% Desempeño
perform(red, Y, Yg');

% Desempeño 
[Exac, Prec, Rec] = desempenio(Yg', Y)

% Desempeño del Modelo Prediccion

Yg2 = round(red(X_test'));

% Desempeño
perform(red, Y_test, Yg2');

% Desempeño 
[ExacP, PrecP, RecP] = desempenio(Yg2', Y_test);
%%
conf = confusionmat(Yg,Y)

tn = conf(1);
fn = conf(3);
fp = conf(2);
tp = conf(4);


