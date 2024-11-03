##############################
#         Limpiar todo       #
##############################
rm(list=ls())
cat("\014")

##############################
#         PAQUETES           #
##############################
Pkg <- c("ggplot2","reshape2",'banxicoR','xts','PerformanceAnalytics', 'ggpubr', 'gridExtra')
inst <- Pkg %in% installed.packages()
if(length(Pkg[!inst]) > 0) install.packages(Pkg[!inst],  dependencies=TRUE)
instpackages <- lapply(Pkg, library, character.only=TRUE)
cat("\014")
#importar datos
data1<-read.csv("C:/Users/juanp/Desktop/TIIE.csv", header=T)
attach(data1)
data1
plot(data1,type="l")

auto.arima(data1)

