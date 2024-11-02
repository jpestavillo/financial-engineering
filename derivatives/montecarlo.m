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

%Get ST
Exp= ((Rates-0.5*Sigma*Sigma)*(Time)+(Sigma*randn()*sqrt(Time)));
AssetPriceatT= AssetPrice*exp(Exp)


%% Price the Options Using the Black-Scholes Closed Formula
PriceBLS = blsprice(AssetPrice, Strike, Rates, Time, Sigma, Yield)


%% Monte Carlo

NSim=10;

for k=1:NSim
        %Get ST
        Exp= ((Rates-0.5*Sigma*Sigma)*(Time)+(Sigma*randn()*sqrt(Time)));
        AssetPriceatT= AssetPrice*exp(Exp);
        %PayOff 
         Option(k)= max(AssetPriceatT-Strike,0.);
        
 end
    PriceMC=mean( Option)*exp(-Rates*Time)
    
    