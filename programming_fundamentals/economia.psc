Proceso ECONOMIA
	definir ex1,ex2,ex3,exprom,proyecto,final, esr,pasar,nex3,nproyecto como real;
	proyecto<- 10;
	esr<- 10;
	escribir "ingrese la calificacion del puto primer examen (todo es sobre 100, no te apendejes)";
	leer ex1;
	escribir "ingrese la calificacion del puto segundo examen";
	leer ex2;
	escribir "el profe se va a pasar de lanza y te va a bajar puntos, pero igual ingresa tus esperanzas de proyecto";
	leer proyecto;
	nex3<- ((60-proyecto-esr)/.7)*3  -ex1-ex2;
	si nex3<0 entonces 
		escribir "ya pasaste, no la armes de pedo";
	sino escribir "suponiendo que sacas 15 en el proyecto (porque el profe no te va a dar 20, necesitas  ", nex3, "  en el tercer examen para pasar";
	FinSi
	
	escribir "ingrese la calificacion del puto tercer examen";
	leer ex3;
	exprom<- ((ex1+ex2+ex3)/3)*.7  ;
	final<- exprom+proyecto+ esr;
	pasar<- 60-final;
	escribir "necesitas  ", pasar, "para pasar";
	
	escribir "tu puta calificacion va  a ser  ", final;
	nproyecto<- 60-exprom-esr;
	escribir "necesitas ", nproyecto, " en el proyecto para pasar";
	
FinProceso
