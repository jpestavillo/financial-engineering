%tarea final
clc; close all;

X=xlsread('tarea','Problema 3','A2:C201');
Y=xlsread('tarea','Problema 3','D2:D201');

%min cuad
n=size(X,1);

for k=1:2
    
    [Xa, forma]= func_polinomio(X,k);
    wnc=inv(Xa'*Xa)*Xa'*Y;
    yg_mc=Xa*wnc;
    E=Y-yg_mc;
    J(k,1)=E'*E/2*n
end
plot(J,'r')