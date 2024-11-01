
ytm= xlsxread('Repaso tipo examen','BonosM','e21:e35')
cupon=xlsxread('Repaso tipo examen','BonosM','h21:h35')
fechas=xlsxread('Repaso tipo examen','BonosM','d21:d35')
vencimientos=x2mdate(fechas,0)
precio=bndprice(ytm,cupon,'04-04-2017',vencimientos)
