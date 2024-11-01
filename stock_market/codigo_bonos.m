clear all; clc
cupones=xlsread('cupones.xlsx','Hoja1','c7:c17');
fechas=xlsread('cupones.xlsx','Hoja1','e7:e17');
vencimientos=x2mdate(fechas,0);
ytm=xlsread('cupones.xlsx','Hoja1','f7:f17');
precios=bndprice(ytm/100,cupones,'29-mar-2017',vencimientos')
preciosisube=bndprice((ytm/100)+0.01,cupones,'29-mar-2017',vencimientos')
preciosibaja=bndprice((ytm/100)-0.01,cupones,'29-mar-2017',vencimientos')
DM=bnddury(ytm/100,cupones,'29-mar-2017',vencimientos)
