Proceso sin_titulo
	definir c1,c2,c3 como entero ;
	definir p como real ;
	escribir "cual fue tu calificacion de tu primera materia?" ;
	leer c1 ; 
	escribir "cual fue tu calificacion de tu segunda materia?" ;
	leer c2;
	escribir "cual fue tu calificacion de tu tercera materia?" ;
	leer c3;
	p<-(c1+c2+c3)/3 ;
	si p<60
		entonces escribir "reprobaste con", p ;
	sino 
		si p<90 
			entonces escribir "pasaste con", p ;
		sino 
			si p>90 
				entonces escribir "felicidades, sacaste", p ;
			FinSi
		FinSi
	FinSi
	 
FinProceso
