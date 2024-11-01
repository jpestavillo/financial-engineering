
cupones=xlsread('portfolio-charlie','d10:d19');
YTM=xlsread('portfolio-charlie','hoja1','f10:f19');
fechas=xlsread('portfolio-charlie','hoja1','h10:h19');
vencimientos = x2mdate(fechas,0)
precios= bndprice(YTM,cupones,'31-03-2017',vencimientos)


