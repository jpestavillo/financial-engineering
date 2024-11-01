clear all;
cupones=xlsread('portolio-charlie','base','d10:d19');
YTM=xlsread('portfolio-charlie','base','f10:f19');
fechas=xlsread('portfolio-charlie','base','h10:h19');
vencimiento=x2mdate(fechas,0)
precios=bndprice(YTM,cupones,fechas,vencimientos)


