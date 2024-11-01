cupones=xlsread('bonos0304','portafolios','b19:b38');
fechas=xlsread('bonos0304','portafolios','d19:d38');
vencimientos=x2mdate(fechas,0);
ytm=xlsread('bonos0304','portafolios','e19:e38')
precios=bndprice(ytm,cupones,'31-mar-2017',vencimientos)
preciomas=bndprice(ytm+.005,cupones,'31-mar-2017',vencimientos)
preciomenos=bndprice(ytm-.005,cupones,'31-mar-2017',vencimientos)
duracionmodificada=bnddury(ytm,cupones,'31-mar-2017',vencimientos)