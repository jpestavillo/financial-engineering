function lagrange
fprintf('Author, el villo')
nx=input('¿Cuántos valores tiene x? ')
ny=input('¿Cuántos valores tiene y? ')
%% ingresas valores x
i=1
while i<=nx
  M(i,1)=input('Introduce tu valor de x: ')
  i=i+1;
end
i=1;
%%  ingresas valores y 
while i<=ny
    M(i,2)=input('Introduce tu valor de y: ')
    i=i+1;
    a=5;
end
i=1;
%% valor a interpretar 
valor=input('introduce tu valor de x a evaluar:')
%% 
for i=1:nx 
    suma=0
    multiplica=1
    for j=1:nx
    if j~=i
    numerador=valor-M(i,1);
    denominador=M(i,1)-M(j,1);
    multiplica=multiplica*(numerador/denominador)
    
    

    end 
    j=j+1;

    end
    
    suma=suma+(M(i,2)*multiplica)  
    suma=a;
    i=i+1;
end

disp(suma)



end