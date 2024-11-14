% Como funciona el Kmeans
% Script que trata de mostrar el fincionamiento del método de clusterng
% Kmeans

clear all;
close all;
clc;
%% Generacion de los datos par el clustering
n = 20;
g1 = rand(n,2);
g2 = rand(n,2)+3;
g3 = [rand(n,1)+2 , rand(n,1)-2];
g4 = [rand(n,1)-2 , rand(n,1)-2];
G = [g1;g2;g3;g4];
labelG = [ones(n,1);2*ones(n,1);3*ones(n,1);4*ones(n,1)];
plot(G(:,1),G(:,2),'x','LineWidth',2);
xlabel('x_1');
ylabel('x_2');
title('Datos Generados');
grid;
clear g1 g2 g3 g4

%% Inicio del algoritmo Kmeans
N_k = 2;
%C = G(round(rand(N_k,1)*size(G,1)),:);
Gtemp = G(randperm(size(G,1)),:);
C = Gtemp(1:N_k,:);
clear C_new Gtemp

n = N_k-1;
% color = [(1/n)*[0:n]' zeros(N_k,1) (-1/n)*[0:n]'+1];
color = [ones(N_k,1) (1/n)*[0:n]' zeros(N_k,1)];

plot(G(:,1),G(:,2),'k.','LineWidth',2);
hold on;
for k = 1:N_k
    plot(C(k,1),C(k,2),'o','Color',color(k,:),'LineWidth',2);
end
hold off;
xlabel('x_1');
ylabel('x_2');
title('Datos Generados');
grid;

%% Algoritmo Kmeans
N_iter = 10;
for iter = 1:N_iter

    % Calculo de las distancias
    for k = 1:N_k
        D(:,k) = sum((G-ones(size(G,1),1)*C(k,:)).^2,2);
    end
    [valor,cluster] = min(D'); %Identificacion de la pertenencia al cluster
    cluster = cluster';

    %close all;
    hold on;
    for k = 1:N_k
        ind = cluster==k;
        plot(G(ind,1),G(ind,2),'.',C(k,1),C(k,2),'o','Color',color(k,:),'LineWidth',2);
        C_new(k,:)=mean(G(ind,:));
        Gtemp = G(ind,:);
        J(k,1) = mean(sum((Gtemp-ones(size(Gtemp,1),1)*C(k,:)).^2,2));
    end
    hold off;
    xlabel('x_1');
    ylabel('x_2');
    title(['Iter: ' num2str(iter) '; Inertia : J = ' num2str(mean(J))]);
%     grid;
    C= C_new; % Actualizacion de los centroides
    pause(1);
end

%% Algoritmo Kmeans
close all;
N_k = 15;
N_iter = 10;
Gtemp = G(randperm(size(G,1)),:);
C = Gtemp(1:N_k,:);
clear C_new Gtemp D leg

n = N_k-1;
% color = [(1/n)*[0:n]' zeros(N_k,1) (-1/n)*[0:n]'+1];
color = [ones(N_k,1) (1/n)*[0:n]' zeros(N_k,1)];
for iter = 1:N_iter

    % Calculo de las distancias
    for k = 1:N_k
        D(:,k) = sum((G-ones(size(G,1),1)*C(k,:)).^2,2);
    end
    [valor,cluster] = min(D'); %Identificacion de la pertenencia al cluster
    cluster = cluster';
    for k = 1:N_k
        ind = cluster==k;
        C_new(k,:)=mean(G(ind,:));
        Gtemp = G(ind,:);
        J(k,1) = mean(sum((Gtemp-ones(size(Gtemp,1),1)*C(k,:)).^2,2));
    end
    C= C_new; % Actualizacion de los centroides
end
close all;
hold on;
for k = 1:N_k
    ind = cluster==k;
    plot(G(ind,1),G(ind,2),'x',C(k,1),C(k,2),'o','Color',color(k,:),'LineWidth',2);
    leg{k} = sprintf('I_{%d} = %0.5f',k,J(k,1));
end
hold off;
legend(leg,'Location','Best')
xlabel('x_1');
ylabel('x_2');
title(['Inertia : I_{global} = ' num2str(mean(J))]);
grid;