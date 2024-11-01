clear all;close all;clc;
population=randi([1 1024],32,1)
numerobits=ceil(log2(1024)) % cuantos numerobits se van a usar 
for t=1:1000 %cuantas generaciones existiran 
y=-(population-628).^2+20;
villocromosoma=[population y]
mejores=sortrows(villocromosoma,2);

for i=1:16  %agarramos la mitad 
    r=rand();
    if r>=.2
        padre(i,1)=mejores(2*i,1);
    else
        padre(i,1)=mejores(2*i-1,1)
    end
end
padresbin=de2bi(padre,numerobits);
%cruzamiento
for i=1:16
p1=randi([2,numerobits-2]);
p2=randi([p1,numerobits-1]);
c1=randi([1 16]);
c2=randi([1 16]);
c3=randi([1 16]);
hijo(i,:)=[padresbin(c1,1:p1) padresbin(c2,p1+1:p2) padresbin(c3,p2+1:numerobits)];
end

%mutación  del 10% 
k=.957;
if k>=.90
   vbit=randi([1 numerobits]);
   vhijo=randi([1 16]);
   
   if hijo(vhijo,vbit)==1;
       hijo(vhijo,vbit)=0;
   else
       hijo(vhijo,vbit)=1;
   end
   
   vbit=randi([1 numerobits]);
   
   
   if hijo(vhijo,vbit)==1;
       hijo(vhijo,vbit)=0;
   else
       hijo(vhijo,vbit)=1;
   end
   vbit=randi([1 numerobits]);
 
   
   if hijo(vhijo,vbit)==1;
       hijo(vhijo,vbit)=0;
   else
       hijo(vhijo,vbit)=1;
   end
end
hijodec=bi2de(hijo);
population=[padre; hijodec];
mejores=sortrows(villocromosoma,2)
end