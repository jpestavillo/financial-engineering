%Limpieza general
clear all;
close all;
clc;

%% Funci?n a identificar
datos=xlsread('DatosEx2.xls','Delfines','a2:c46');
Y=datos(:,1);
X=datos(:,2:3);
%% M?nimos cuadrados
n=size(X,1); %Dimensi?n de las filas de X (Cantidad de datos)

%Construir X*=[1 X]
Xa=[ones(n,1)];

for k=1:2
    [Xa, forma]=func_polinomio(X,k);
    %Xa=[Xa, X.^k];
    Wmc=inv(Xa'*Xa)*Xa'*Y;
    Yg_mc=Xa*Wmc;
    E=Y-Yg_mc;
    J(k,1)=E'*E/(2*n);
end
  plot(J,'b')
  xlabel('Grado del polinomio')
  ylabel('J(X,W)')
  %plot(X,Y,'b.',X,Yg_mc,'r.')
  


  
      
      
      
      
      
      
      
  
  
  
  
  
  
  
    
    
    
