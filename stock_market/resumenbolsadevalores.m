%poner los datos en la tabla despues de limpiar las columnas y acomodar
%rangos aqui abajo
cupon= xlsread('resumenbolsadevalores','BonosM','e15:e29') 
YTM= xlsread('resumenbolsadevalores','BonosM','f15:f29')
fechas= xlsread('resumenbolsadevalores','BonosM','d15:d29')
vencimientos=x2mdate(fechas,0)
%en el siguiente inciso usa la fecha de hoy
precio=bndprice(YTM,cupon,'04-may-2017',vencimientos)
dmodificada=bnddury(YTM,cupon,'04-may-2017',vencimientos)
preciosube=bndprice(YTM+.005,cupon,'04-may-2017',vencimientos)
preciobaja=bndprice(YTM-.005,cupon,'04-may-2017',vencimientos)

%en este punto vamos a calcular calls y puts
%[call,put]=blsprice(precio actual, strike, tasa, tiempo en años y
%volatibilidad
[Call, Put] = blsprice(100, 95, 0.1, 0.25, 0.5)
[c2,p2]= blsprice(49,485.67,47000,.067,1.13,