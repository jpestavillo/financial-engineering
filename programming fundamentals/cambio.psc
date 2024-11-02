Proceso sin_titulo
	Definir cambio,billete500,billete200,billete100,billete50,billete20,moneda10,moneda5,moneda2,moneda1 Como Real; ;
	escribir "cuanto es el cambio que se espera otorgar?" ;
	leer cambio ;
	billete500<- trunc(cambio/500) ;
	billete200<- trunc((cambio -billete500*500)/200) ;
	billete100<- trunc((cambio -billete500*500 -billete200*200)/100) ; 
    billete50<-  trunc((cambio -billete500*500 -billete200*200 -billete100*100)/50) ;
	billete20<-  trunc((cambio -billete500*500 -billete200*200 -billete100*100 -billete50*50)/20) ;
	moneda10<-   trunc((cambio -billete500*500 -billete200*200 -billete100*100 -billete50*50 -billete20*20)/10) ;
	moneda5<-    trunc((cambio -billete500*500 -billete200*200 -billete100*100 -billete50*50 -billete20*20 -moneda10*10)/5) ;
	moneda2<-    trunc((cambio -billete500*500 -billete200*200 -billete100*100 -billete50*50 -billete20*20 -moneda10*10 -moneda5*5)/2) ;
	moneda1<-    trunc(cambio -billete500*500 -billete200*200 -billete100*100 -billete50*50 -billete20*20 -moneda10*10 -moneda5*5-moneda2*2) ;
	
	
	 Escribir billete500, " billetes de 500, ", billete200, "  billetes de 200, ",  billete100, " billetes de 100,", billete50, " billetes de 50,", billete20, "billetes de 20,", moneda10, "monedas de 10,", moneda5, "monedas de 5,", moneda2, "monedas de 2,", moneda1, "monedas de 1," ;
	 
FinProceso
