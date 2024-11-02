Proceso factorial
	definir num,factoria,cont como real;
	escribir "ingrese el pinche numero para sacar la pinche factorial";	
	leer factoria;
	factoria<- trunc(factoria);
	cont<- factoria ;
	si cont<1 entonces 
		escribir "no sea payaso, pon otro numero";
	
	FinSi
	mientras cont>1 Hacer 
		factoria<- factoria*(cont-1);
		cont<- cont-1 ;
	FinMientras
	si cont=1 entonces 
		escribir "el resultado es", factoria; 
	FinSi
	
FinProceso
