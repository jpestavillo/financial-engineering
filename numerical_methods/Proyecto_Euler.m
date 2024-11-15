function Proyecto_Euler
syms x %variable simbólica x, la cual podrá ser evauluada como función
syms y %variable simbólica
f = input('Ingrese la Funcion: ','s'); %% introducción de la para no homogenea de la ecuación diferencial ordinaria
x = input('Ingrese el valor inical de x: ');%% valor  partir del cual se comenzará el método
xf = input('Ingrese el valor a buscar x: '); %% valor a encontrar, en el cual el método se detendrá
y = input('Ingrese el valor inicial de y: ');%% valor inicial de y, con el cual se hará la primera iteración del método
h = input('Ingrese el valor de h: '); %% valor del paso a usar para ls iteraciones
n = (xf-x)/h %% cantidad de iteracions a usar en el método

disp('x(n) y(n)'); %% mostrar la iteración cero del método
i=1
%%for i=1 : n+1
while i<=n+1 %%ciclo que se detendrá hasta que llegue al número de iteraciones deseado
y1 = eval(f); % evaluación de la función
hy1 = h*y1; %% segundo término de la fórmula del métdo
fprintf('\n%0.1f %0.4f', x,y); %%impresión de los valores acutales de x, y
y = y + hy1;%% y de la siguiente iteración
x = x + h; %% x de la siguiente iteracón
i=i+1 ;%% siguiente paso del contador 
end




