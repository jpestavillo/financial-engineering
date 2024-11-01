cupon=xlsread('resumen bolsa de valores','BonosM','e15:e64')
YTM=xlsread('resumen bolsa de valores','BonosM','f15:f64')
fechas=xlsread('resumen bolsa de valores','BonosM','d15:d64')
vencimientos=x2mdate(fechas,0)
%en el siguiente inciso usa la fecha de hoy
precio=bndprice(YTM,cupon,'04-may-2017',vencimientos)
dmodificada=bnddury(YTM,cupon,'04-may-2017',vencimientos)
preciosube=bndprice(ytm+.005,cupon,'04-04-2017',vencimientos)
preciobaja=bndprice(ytm-.005,cupon,'04-04-2017',vencimientos)
