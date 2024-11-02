Proceso sin_titulo
	Definir salariobruto, horastrabajadas, impuestos, salariototal Como Real;
	Escribir "¿cuanto es el salario del esclavo (o empleado) por una hora?" ;
	leer salariobruto ;
	Escribir "¿cuantas horas trabajó el prro este?" ;
	Leer  horastrabajadas ;
	Escribir "¿cuanto es el porcentaje de impuesto que le gobierno puto te esta quitando?" ;
	leer impuestos ;
	salariototal<- (salariobruto*horastrabajadas)*(1-impuestos) ;
	
	
			Si salariobruto<500 Entonces
				Escribir "eres un esclavo del sistema capitalista pinche pobre porque tu salario es solamente de", salariobruto ;
			Sino
				escribir "eres un rico que oprime a la clase trabajadora porque ganas    " , salariobruto ;
			FinSi
			
			Si horastrabajadas<35 Entonces
				Escribir "solamente trabajaste", horastrabajadas, ".Eres un huevon", horastrabajadas ;
			Sino
				Escribir "trabajaste", horastrabajadas, "eres un adicto al trabajo, relaja la raja carnal   " ;
			FinSi
			Escribir  "en fin, tu salario va a ser de  $",  salariototal ;
			
FinProceso
