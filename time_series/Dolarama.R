#Antes de empezar, asegurar que tenemos instalados los siguientes paquetes:
#Instalar paquete timeseries, tseries, forecast, stats
#Seleccionar a CRAN mirror
library(tseries)

library(forecast)
library(stats)
library(fGarch)
library(rugarch)
library(zoo)

#Metodolog�a Box-Jenkins para modelos ARIMA(p,d,q)
#D�lar

#Primera etapa: Identificaci�n del modelo ARIMA(p,d,q)
#1.Identificar el orden de integraci�n de la serie, para ello
#graficamos la serie original, tomamos diferencias y las analizamos, 
#hacemos la prueba de estacionaridad Dickey Fuller Aumentada (ADF)
#Importar los datos
data1<-read.csv("C:/Users/juanp/OneDrive for Business/tercer semestre/series de tiempo/Dolar.csv", header=T)
attach(data1)
data1
data1$D�lar < -ts(data1$D�lar,start=c(2010,01),end=c(2017,10),frequency=12)
summary(data1)
#Graficar la serie original para determinar visualmente si es estacionaria o no
plot(data1,type="l")
plot(D�lar,type="l")
#Tomamos diferencias y comparamos la varianza de cada difencia inclu�da con la original
ddolar<-diff(data1$D�lar)
d2dolar<-diff(ddolar)
summary(ddolar)
summary(d2dolar)
var(D�lar)
var(ddolar)
var(d2dolar)
#Tomamos la serie con la menor varianza
par(mfrow=c(2,1))
plot(ddolar, type="l")
plot(d2dolar, type="l")
#Prueba Dickey Fuller de ra�z unitaria
#La H0 en la prueba Dickey Fuller Aumentada es que la serie no es estacionaria, 
#interpretamos el pvalue de la prueba
adf.test(D�lar)
adf.test(ddolar)
#Por lo tanto, la puebra ADF nos confirma el an�lisis de la varianza de las diferencias
#Para determinar el orden p y q del modelo analizamos la FAC y la FAC parcial
#El �rden p lo identidicamos en la FAC parcial, y el �rden q en la FAC
par(mfrow=c(2,1))
acf(D�lar)
pacf(D�lar)
 
par(mfrow=c(2,1))
acf(ddolar)
pacf(ddolar)

#Segunda etapa: Estimaci�n del modelo ARIMA(p,d,q identificado
#Hay una funci�n para determinar el arima de forma autom�tica
##Si estimamos el AR(1)=ARIMA(1,0,0) sobre la serie original confirmamos 
##que no es estacionaria:
arima(D�lar,order=c(1,0,0))
#Por lo tanto, modelar la serie original no es correcto

#Modelamos el arima con la diferencia estacionaria
auto.arima(D�lar)
auto.arima(ddolar)
arimadolar=arima(D�lar,order=c(0,1,1))
arimadolar

#Tercera etapa: Verificaci�n del modelo ARIMA(p,d,q) estimado
##Pruebas de residuales
plot(arimadolar$residuals, type="l")
##Prueba 2: Correlaci�n de los residuales
par(mfrow=c(2,1))
acf(arimadolar$residuals)
pacf(arimadolar$residuals)

tsdiag(arimadolar)
Box.test(arimadolar$residuals,type="Ljung-Box",lag=7)
##Prueba 3: Heteroscedasticidad (prueba ARCH)
ArchTest(arimadolar$residuals,lag=1)


#Cuarta etapa: Pron�sticos
forecast(arimadolar,12)
plot(forecast(arimadolar,12))
