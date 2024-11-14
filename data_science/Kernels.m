clear all;
close all;
clc;


%data = importfile('C:\Users\riemannruiz\OneDrive - ITESO\CDIN_O2017\Referencias\Data\Reg_Log\ex2data1.txt',1,118);
% data = importfile('G:\CDIN_O2017\Data\ex2data1.txt',1,118);
% data = table2cell(data);
% data = cell2mat(data);
load data.mat;
x1 = data(:,1);
x2 = data(:,2);
Y = data(:,3);
indx0 = Y==0;
indx1 = Y==1;
%%
figure(1);
plot(x1(indx0),x2(indx0),'b.',x1(indx1),x2(indx1),'r.','MarkerSize',15)
grid;

%% Enfoque regresión logística
W = [ 2.58468	3.24746	4.16619	-12.0267	-7.53112	-11.8224]';
xx1 = [min(x1):0.1:max(x1)];
xx2 = [min(x2):0.1:max(x2)];
[xxx1,xxx2] = meshgrid(xx1,xx2);
[m,n] = size(xxx1);
xxx1_f = reshape(xxx1,m*n,1);
xxx2_f = reshape(xxx2,m*n,1);
Xa_f = [ones(m*n,1),xxx1_f,xxx2_f,xxx1_f.^2,xxx1_f.*xxx2_f,xxx2_f.^2];
Z = Xa_f*W;
Z = reshape(Z,m,n);

figure(1);
plot(x1(indx0),x2(indx0),'b.',x1(indx1),x2(indx1),'r.','MarkerSize',15)
hold on;
mesh(xxx1,xxx2,Z);
hold off;
grid;




%%
W = [ 2.58468	3.24746	4.16619	-12.0267	-7.53112	-11.8224]';
Xa = [ones(size(Y)),x1,x2,x1.^2,x1.*x2,x2.^2];
Z = Xa*W;
figure(2);
plot3(x1(indx0),x2(indx0),Z(indx0),'b.',x1(indx1),x2(indx1),Z(indx1),'r.','MarkerSize',15)
hold on;
mesh(xxx1,xxx2,zeros(size(xxx1)));
hold off;
xlabel('x1'),ylabel('x2'),zlabel('z = w0+w1x1+w2x2+w3x1^2+w4x1x2+w5x2^2')
grid;

%%
x1k = -5.76336103e-01*x1;
x2k = -6.62726216e-01*x2;
x3k = 1.96601502e-02*x1.*x2;
figure(3);
plot3(x1k(indx0),x2k(indx0),x3k(indx0),'b.',x1k(indx1),x2k(indx1),x3k(indx1),'r.','MarkerSize',15)
xlabel('w1x1'),ylabel('w2x2'),zlabel('w4x1x2')
grid;

%% Datos 2
clear all;
close all;
clc;


% data = importfile('C:\Users\riemannruiz\OneDrive - ITESO\CDIN_O2017\Referencias\Data\Reg_Log\ex2data2.txt',1,118);
% data = table2cell(data);
% data = cell2mat(data);
load data.mat;
x1 = data(:,1);
x2 = data(:,2);
Y = data(:,3);
indx0 = Y==0;
indx1 = Y==1;
%%
figure(1);
plot(x1(indx0),x2(indx0),'b.',x1(indx1),x2(indx1),'r.','MarkerSize',15);
grid;


%% polinomio cuadratico
W = [  2.58467631,   3.2474591 ,   4.16618792, -12.02671614, -7.53111697, -11.82237042]';
Xa = [ones(size(Y)),x1,x2,x1.^2,x1.*x2,x2.^2];
Z = Xa*W;
figure(2);
plot3(x1(indx0),x2(indx0),Z(indx0),'b.',x1(indx1),x2(indx1),Z(indx1),'r.','MarkerSize',15)
xlabel('x1'),ylabel('x2'),zlabel('z = w0+w1x1+w2x2+w3x1^2+w4x1x2+w5x2^2')
grid;

%% polinomio a la 8
W = [  1.30798785e+01,   8.16470917e+01,   4.42453819e+01,...
         -1.44321392e+02,  -1.12823987e+01,  -1.17839319e+02,...
         -4.95907643e+02,  -1.27708144e+02,  -6.88385167e+02,...
         -1.85996443e+02,   2.25531009e+02,   6.40444989e+02,...
          3.53246841e+02,  -1.17048818e+02,   2.90322525e+02,...
          8.79402205e+02,   1.64348937e+02,   2.49079272e+03,...
         -1.24850741e+02,   1.51173653e+03,   1.91203324e+02,...
          2.41363714e+02,  -2.80924576e+03,   3.59636214e+00,...
          4.59470855e+02,   2.31870641e+02,  -5.91734465e+02,...
         -5.11555985e+02,  -3.90376320e+02,   2.65797065e+02,...
          7.80268300e-01,   6.05219109e+02,  -4.43972776e+03,...
          1.51405517e+03,   7.49082394e+02,   5.56126792e+02,...
         -7.94623054e+02,   2.52194365e+03,  -1.16193832e+03,...
         -2.62546466e+03,  -1.84414591e+03,   2.09439120e+03,...
         -2.00394840e+03,  -1.17650286e+03,  -3.18798121e+02]';

Xa = [ones(size(Y)),x1,x2,x1.^2,x1.*x2,x2.^2,x1.^3,x1.^2.*x2,x1.*x2.^2,x2.^3,...
    x1.^4,x1.^3.*x2,x1.^2.*x2.^2,x1.*x2.^3,x2.^4,...
    x1.^5,x1.^4.*x2,x1.^3.*x2.^2,x1.^2.*x2.^3,x1.*x2.^4,x2.^5,...
    x1.^6,x1.^5.*x2,x1.^4.*x2.^2,x1.^3.*x2.^3,x1.^2.*x2.^4,x1.*x2.^5,x2.^6,...
    x1.^7,x1.^6.*x2,x1.^5.*x2.^2,x1.^4.*x2.^3,x1.^3.*x2.^4,x1.^2.*x2.^5,x1.*x2.^6,x2.^7,...
    x1.^8,x1.^7.*x2,x1.^6.*x2.^2,x1.^5.*x2.^3,x1.^4.*x2.^4,x1.^3.*x2.^5,x1.^2.*x2.^6,x1.*x2.^7,x2.^8];
Z = Xa*W;
figure(3);
plot3(x1(indx0),x2(indx0),Z(indx0),'b.',x1(indx1),x2(indx1),Z(indx1),'r.','MarkerSize',15)
xlabel('x1'),ylabel('x2'),zlabel('V')
axis([-1.5 1.5 -1.5 1.5 -20 20])
grid;

%% Kernel guasiano
Z = zeros(size(data,1),1);
%c = [-0.4 0.4;-0.2 0.6;0.2 0.5; 0.7 -0.2];
%c = [0.2 0.1];
c = data(indx1,1:2);
sigma = 0.05;
X = data(:,1:2);

for ci = 1:size(c,1)
    norm = sum((X-ones(size(data,1),1)*c(ci,:)).^2,2)/(sigma^2);
    Z = Z + exp(-norm);
end


figure(4);
plot3(x1(indx0),x2(indx0),Z(indx0),'b.',x1(indx1),x2(indx1),Z(indx1),'r.','MarkerSize',15)
xlabel('x1'),ylabel('x2'),zlabel('V')
grid;


%% Superficie del Kernel
xx = -1.5:0.01:1.5;
yy = xx;
[XX,YY] = meshgrid(xx,yy);
[m,n]=size(XX);
Xn = [reshape(XX,m*n,1) reshape(YY,m*n,1)];
Z = zeros(size(Xn,1),1);
for ci = 1:size(c,1)
    norm = sum((Xn-ones(size(Xn,1),1)*c(ci,:)).^2,2)/(sigma^2);
    Z = Z + exp(-norm);
end
ZZ = reshape(Z,m,n);
figure(5);
subplot(1,2,1);
mesh(XX,YY,ZZ);
subplot(1,2,2);
contour(XX,YY,ZZ),hold on,plot(x1(indx0),x2(indx0),'b.',x1(indx1),x2(indx1),'r.','MarkerSize',15),grid,hold off;