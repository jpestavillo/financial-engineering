% Limpieza
clear all;
close all;
clc;

%Cargar datos
load ex_mia4_data1.mat
data = train'
%%
clear train
%%



X=data(1:3,:);
Y=data(4,:);

ndat=round(1*size(Y,2)); %Cantidad de datos para entrenar

Ytrain=Y(:,1:ndat);
Xtrain=X(:,1:ndat);

%Creaci?n del modelo neuronal

red=feedforwardnet(1);

red.trainFcn='trainscg' 
%Para clasificaci?n Supervisada usar trainscg
%o usar trainrp

red=train(red,Xtrain,Ytrain);

%Simulaci?n
Yg=red(X);


%Ygr=round(Yg);
Ygr=round(Yg);
%Ygr=double(Ygr)

 Test =red(test_unknown');
 Testgr = round(Test);

 %%
 %Dummies
for i =1:sze(2)
    dummyf(i,Testgr(i))= 1;
    %i = i+1;
end


%%
%Dummies
%ma = max(Testgr);
%sze = size(Testgr);
%dummyf = zeros(sze(2),ma);
%dummyf = zeros(5,5)










%%
%intento 1
%for i in dummyf :
 %   if tras(:,i) = 1:
  %      dummyf(k,tras) =1
   % else if tras(:,i) = 2:
    %    dummyf(k,tras) =1
    %else 
     %   dummyf(k,tras) =1
    %i =+1;
     %   end
    %end
%end
        