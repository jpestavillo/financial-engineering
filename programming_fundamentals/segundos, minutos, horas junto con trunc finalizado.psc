Proceso sin_titulo
	definir sobrantehoras,sobranteminutos,seg,horas,sobranteseg Como real;
	Escribir "cuantos segundos han transcurrido?" ;
	leer seg ;
	sobranteseg<- seg mod 60 ;
	
	sobranteminutos<- seg mod 3600 - sobranteseg ;
	horas<- (seg-sobranteseg-sobranteminutos)/3600 ;

	
	escribir horas, ":" , sobranteminutos, ":", sobranteseg, "si puedes ver esto mi programa si funciona, podre dormir"  ;
FinProceso
