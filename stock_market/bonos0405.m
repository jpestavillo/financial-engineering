ytm= xlsread('Repaso tipo examen','BonosM','e21:e35');
cupon=xlsread('Repaso tipo examen','BonosM','h21:h35');
fechas=xlsread('Repaso tipo examen','BonosM','d21:d35');
vencimientos=x2mdate(fechas,0);
precio=bndprice(ytm,cupon,'04-04-2017',vencimientos);
dmodificada=bnddury(ytm,cupon,'04-04-2017',vencimientos)
preciosube=bndprice(ytm+.005,cupon,'04-04-2017',vencimientos)
preciobaja=bndprice(ytm-.005,cupon,'04-04-2017',vencimientos)