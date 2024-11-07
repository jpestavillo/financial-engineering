%1.a Para el conjunto de datos data2 proporcionar el que se considere el mejor modelo y justificar el porque se la elección. Proporcionar sus medidas de desempeño (Exactitud, precisión, recall, J, etc). Recordar incluir y explicarlas gráficas. Reportar cuál fue el mejor modelo matemático (escribir sus coeficientes).

%1.b Con el mejor modelo seleccionado indicar a qué clase pertenecen los siguientes datos:

 %  (0,2), (0.5,0.5), (0.75,0.75), (1,1), (2,3)

%2. Con el comando  load simplecluster_dataset.mat  cargar la base de datos de Matlab, obtener el modelo que mejor ajuste y clasificar la información contenida en simpleclusterInputs. Compare sus resultados con los resultados objetivos.

%3.Importe la base de datos contenida en el archivo adjunto BaseSangre.txt y obtenga lo siguiente:

%a) el modelo que mejor ajuste a los datos, particionando los datos al 80% para obtener el modelo y el 20% para probar el modelo, la partición debe ser a través de una selección aleatoria. 

%b) Medidas de desempeño del entrenamiento.

%c) Matriz de confusión con los datos de prueba.

%tarea final
clc; close all;
 
%X=xlsread('tarea','Problema 3','A2:C201');
%Y=xlsread('tarea','Problema 3','D2:D201');
X=BaseSangre1
Y=BaseSangre1
%min cuad
n=size(X,1);
 
for k=1:5
    
    [Xa, forma]= func_polinomio(X,k);
    wnc=inv(Xa'*Xa)*Xa'*Y;
    yg_mc=Xa*wnc;
    E=Y-yg_mc;
    J(k,1)=E'*E/2*n
end
plot(J,'r')
