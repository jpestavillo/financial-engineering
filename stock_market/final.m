clear all;close all;clc
datos=xlsread('bonos.xlsx','bonds','C4:E8'); %debo actualizar las ytms de los bonos segun lo que el profe me indique o lo bajo de citibanamx 
bonos=[x2mdate(datos(:,1),0),datos(:,2)];
[zerorates,curvedates]=zbtyield(bonos,datos(:,3),'05-dec-2019'); %la fecha debe ser igual a la fechas de las ytms
curvacero=[curvedates,zerorates];
probas=[curvedates,(ones(1,length(curvedates))*(.143+.075)/(1-.38))']; %debo actualizar la proba de default segun el spread de credito (dif en ytms entre tu bono y el riskfree-treasury)
 
[primacds]=cdsspread(curvacero,probas,'05-dec-2019','05-dec-2021','RecoveryRate',.38)

%(.143+.075)/(1-.38)=.2306