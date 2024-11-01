clear all;
close all;
clc;
%% Par?metros
xmin=-50; %l?mite inferior
xmax=50; %l?mite superior
tp=0.2; %tama?o de paso

elementos=(xmax-xmin+1)/tp; %Cantidad de n?meros
nbits=ceil(log2(elementos)); %N?mero de bits

%% Generar la poblaci?n
np=16; %N?mero de pobladores

x1=randi([0 2^nbits-1],np,1); %padres enteros positivos

x1real=(xmax-xmin)*x1/(2^nbits-1)+xmin; 
%Conversi?n de entero a Real
for k=1:1000
    y=-(x1real+10.125).^2+50; %Evaluaci?n
    yprom(k)=mean(y);
    cromosoma=sortrows([y x1 x1real],1);
    % cromosoma=[x1 x1real y];
    % cromosoma=sortrows(cromosoma,size(cromosoma,2))

    %% Selecci?n
    padresbin=de2bi(cromosoma(np/2+1:np,2),nbits);
    %Selecci?n de mejores y conversi?n

    %% Cruzamiento aritm?tico
    for i=1:np/2
        j=i+1;
        if j==np/2+1
            j=1;
        end
        hijo(i,1)=cromosoma(np/2+i,2)+cromosoma(np/2+j,2);
        hijobin(i,:)=de2bi(hijo(i,1),nbits+1);
    end
        hijobin=hijobin(:,1:end-1);

       %% Mutaci?n
       m=rand();
       if m>=.8
           nhijo=randi(np/2);
           bit=randi(nbits);
           if hijobin(nhijo,bit)==1;
               hijobin(nhijo,bit)=0;
           else
               hijobin(nhijo,bit)=1;
           end
       end
       hijoent=bi2de(hijobin); %se pasa de decimal a entero
       hijoreal=(xmax-xmin)*hijoent/(2^nbits-1)+xmin;
       %hijos enteros a reales
       x1=[cromosoma(np/2+1:np,2); hijoent];
       x1real=[cromosoma(np/2+1:np,3); hijoreal];
       clear hijobin
end   
   
plot(yprom)
y=-(x1real+10.125).^2+50;
cromosoma=[y x1 x1real];

[val,ind]=max(y);

disp(['x1= ' num2str(cromosoma(ind,3)) ' y= ' num2str(val)])