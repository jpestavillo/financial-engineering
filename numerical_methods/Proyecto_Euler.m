function Proyecto_Euler
syms x %variable simb�lica x, la cual podr� ser evauluada como funci�n
syms y %variable simb�lica
f = input('Ingrese la Funcion: ','s'); %% introducci�n de la para no homogenea de la ecuaci�n diferencial ordinaria
x = input('Ingrese el valor inical de x: ');%% valor  partir del cual se comenzar� el m�todo
xf = input('Ingrese el valor a buscar x: '); %% valor a encontrar, en el cual el m�todo se detendr�
y = input('Ingrese el valor inicial de y: ');%% valor inicial de y, con el cual se har� la primera iteraci�n del m�todo
h = input('Ingrese el valor de h: '); %% valor del paso a usar para ls iteraciones
n = (xf-x)/h %% cantidad de iteracions a usar en el m�todo

disp('x(n) y(n)'); %% mostrar la iteraci�n cero del m�todo
i=1
%%for i=1 : n+1
while i<=n+1 %%ciclo que se detendr� hasta que llegue al n�mero de iteraciones deseado
y1 = eval(f); % evaluaci�n de la funci�n
hy1 = h*y1; %% segundo t�rmino de la f�rmula del m�tdo
fprintf('\n%0.1f %0.4f', x,y); %%impresi�n de los valores acutales de x, y
y = y + hy1;%% y de la siguiente iteraci�n
x = x + h; %% x de la siguiente iterac�n
i=i+1 ;%% siguiente paso del contador 
end




