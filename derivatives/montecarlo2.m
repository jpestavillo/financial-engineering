%Start
clear all; close all; clc


%% Define the Call Instrument
% Option

Time = 243./365.;
Strike = 30;
AssetPrice = 25;
Sigma = .35;
Yield =0.;

%% Create the Interest Rate Term Structure
%Flat
Rates = 0.0111;
%% Price the Options Using the Black-Scholes Closed Formula
PriceBLS = blsprice(, Strike, Rates, Time, Sigma, Yield)
AssetPrice

%% Monte Carlo



%%Loop
tic
NSim=100000;
InitialStep=100;
LenghtStep=100;
NumPeriodMC  = InitialStep : LenghtStep : NSim;
NbStepMC     = length(NumPeriodMC);
%PriceMC = nan(NbStepCRR, 1); %Ignore value

Option=[];
k2=0.;
for i=1:NbStepMC
    k2= k2+1.;
    Option = nan(k2, 1);  
    for k=1:i
        %Get ST
        Exp= ((Rates-0.5*Sigma*Sigma)*(Time)+(Sigma*randn()*sqrt(Time)));
        AssetPriceatT= AssetPrice*exp(Exp);
        %PayOff 
         Option(k)= max(AssetPriceatT-Strike,0.);
        
    end
    PriceMC(i)=mean( Option)*exp(-Rates*Time);
end
toc
%% Plot
 plot(NumPeriodMC, PriceMC, '.');
hold on;
plot(NumPeriodMC, PriceBLS*ones(NbStepMC,1),'Color',[0 0.9 0], 'linewidth', 1.5);


%Titles
% Annotate Plot
titleString = sprintf('\nConvergence of Generalized Monte Carlo to a BLS Solution (OTM)\nStrike = %d,  Asset Price = %d', Strike , AssetPrice);
title(titleString)
ylabel('Option Price')
xlabel('Number of Sim')
legend('MonteCarlo', 'BLS', 'Location', 'NorthEast')

