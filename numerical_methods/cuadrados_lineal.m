function cuadrados_lineal
%Limpieza de consola para correr el programa nuevamente
clc
 
%Mostrar datos de los alumnos que hicieron el programa%
disp('Becerra Casas Gustavo Eduardo')
disp('Estavillo Urrea Juan Pablo')
disp('Osuna Rios Rodrigo')
 
%Introducción de datos por el usuario%
nx=input('¿Cuántos valores tiene x? ')
ny=input('¿Cuántos valores tiene y? ')
 
%=ESTA SECCIÓN ES PARA DEFINIR VARIABLES A UTILIZAR MÁS ADELANTE=%
 
%Contador utilizado para todos los ciclos%
i=1;
%Sumatorias%
sumx=0;
sumy=0;
sumxc=0;
sumxy=0;
sumyn=0;
s1=0;
s2=0;
 
%=ESTA SECCIÓN ES PARA INTRODUCIR LOS DATOS DENTRO DE LA MATRIZ=%
 
%Introducción datos de x y sumatoria de x%
while i<=nx
  M(i,1)=input('Introduce tu valor de x: ')
  sumx=sumx+M(i,1);
  i=i+1;
end
i=1;
 
%Introducción datos de y sumatoria de y%
while i<=ny
    M(i,2)=input('Introduce tu valor de y: ')
    sumy=sumy+M(i,2);
    i=i+1;
end
i=1;
 
%=ESTA SECCIÓN ES PARA CALCULAR LOS DIFERENTES VALORES CON LOS DATOS
%INTRODUCIDOS POR EL USUARIO=%
 
%Sacar x^2 y sumatoria de x^2%
while i<=nx
M(i,3)=(M(i,1)^2);
sumxc=sumxc+M(i,3);
i=i+1;
end
i=1;
 
%Sacar x*y y sumatoria de x*y%
while i<=nx
M(i,4)=(M(i,1)*M(i,2));
sumxy=sumxy+M(i,4);
i=i+1;
end
i=1;
 
%=ESTA SECCIÓN ES PARA CALCULAR LOS VALORES DE A0, A1 Y R=%
 
%Sacar los valores de a0 y a1
a0=(((sumy*sumxc)-(sumx*sumxy))/((nx*sumxc)-(sumx^2)));
a1=(((nx*sumxy)-(sumx*sumy))/((nx*sumxc)-(sumx^2)));
 
%Promedio de y%
prom=sumy/nx;
 
%=ESTA SECCIÓN ES PARA CALCULAR LAS DESVIACIONES CON LA FUNCIÓN NUEVA Y LA
%FUNCIÓN ORIRIGINAL=%
 
%Calculos con la Ynueva%
while i<=nx
M(i,5)=(a0+(a1*M(i,1)));
sumyn=sumyn+M(i,5);
M(i,6)=(M(i,5)-M(i,2))^2;
s2=s2+M(i,6);
M(i,7)=(prom-M(i,2))^2;
s1=s1+M(i,7);
i=i+1
end
 
%=ESTA SECCIÓN ES PARA CALCULAR EL FACTOR DE CORRELACIÓN=%
 
%Factor de Correlación
rnum=((s1-s2)/s1)^(1/2);
rpor=rnum*100;
 
%Guardando los valores finales%
valorfa0 = a0;
valorfa1 = a1;
fcorre = rnum;
fcorrepor=rpor;
 
%Display de los valores finales obtenidos%
fprintf('Tus Cálculos son: \n')
disp('       X         Y        X^2       X*Y       Yn     (Yn-y)^2  (Ypm-y)^2')
disp(M)
fprintf('Tu Valor de a0 es %f \n', valorfa0)
fprintf('Tu Valor de a1 es %f \n', valorfa1)
fprintf('Tu Factor de Correlación (numéricamente) fue %f \n', fcorre)
fprintf('Tu Factor de Correlación (porcentaje) fue %f \n', fcorrepor)
 
if rnum<=0.90
    fprintf('Una función lineal no es viable para el problema \n')
elseif rnum>=0.90
    fprintf('Una función lineal es viable para el problema \n')
end


kk=M(:,1)
kkck=M(:,2)
plot(kk,kkck,'d-g')
kkckdbb=M(:,5)
plot(kk,kkckdbb,'d-g')
end
