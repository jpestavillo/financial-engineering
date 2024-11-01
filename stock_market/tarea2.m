clear all, clc, close all, format compact

% define coordinates
x = xlsread('tarea','Problema 2','A2:A301');
x2=xlsread('tarea','Problema 2','B2:B301')
y = xlsread('tarea','Problema 2','C2:C301') ;

% plot given data in red
%plot(x, y, 'ro', 'linewidth', 2)
hold on 

% find polynomial fits of different orders
p2 = polyfit(x, y, 2)
p4 = polyfit(x, y, 4)
p5 = polyfit(x, y, 5) 
polyfit(

% see interpolated values of fits
xc = 1 : .1 : 10; 

% plot 2nd order polynomial
y2 = polyval(p2, xc);
plot(xc, y2, 'g.-') 

% plot 4th order polynomial
y4 = polyval(p4, xc);
plot(xc, y4, 'linewidth', 2) 

% plot 5th order polynomial
y5 = polyval(p5, xc);
plot(xc, y5, 'k.', 'linewidth', 2)
grid

legend('original data', '2nd. order fit', '4th. order', '5th. order')