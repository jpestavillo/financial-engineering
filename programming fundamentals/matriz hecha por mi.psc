Proceso sin_titulo
	definir n,i,contador,t,contat,a como entero;
	definir bandera como logico;
	escribir "cuanto va a medir su matriz, bella dama?";
	leer n;
	dimension a(1000,1000);
	para contador<-0 hasta n-1 Hacer
		para contat<-0 hasta n-1 Hacer
			leer a(contador,contat);
		FinPara
	FinPara
	
	contador<-0;
	contat<-0;
	
	bandera<- verdadero;
	para contador<-0 hasta n-1 hacer
		para contat<-0 hasta n-1 hacer 
			si a(contador,contat) <> a(contat,contador) 
				entonces bandera<-falso;
			FinSi
		FinPara
	FinPara
	
	si bandera=verdadero entonces 
		escribir "la matriz es simetrica patrona";
	sino escribir "pinche matriz culera";
	FinSi
FinProceso


