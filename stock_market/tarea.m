X2 = xlsread('tarea','Problema 2','A2:A201');
X1 = xlsread('tarea', 'Problema 2', 'B2:B201'); %xlsread(de donde, 'nombre de hoja', 'rango de datos')
Y = xlsread('tarea', 'Problema 2', 'C2:C201'); %xlsread(de donde, 'nombre de hoja', 'rango de datos')
n= size(X1,1); %Cantidad de datos

%%
Xa = [ones(n,1)];
Xa = [Xa X1 X1.^2 X2 X1.*X2 X1.^2.*X2]
Wmc = inv(Xa'*Xa)*Xa'*Y;
% for k = 1:3 %desde 11 ya es overfitting, ajustar los márgenes
%     Xa =[Xa, X.^k];
% end

Yg_mc = Xa*Wmc;
E = Y - Yg_mc; %Error

