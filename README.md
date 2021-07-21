# Django Cli Helper

Utilidad para generar extructura compatible con Django-REST-Frameworks


## Comandos

#### Actualizar estructura de la app

	python3 dch.py -aa {nombre_app}

#### Generar arbol del modelo

	python3 dch.py -g -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear extructura del modelo
	
	python3 dch.py -cm -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Vista
	
	python3 dch.py -cv -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Admin class
	
	python3 dch.py -ca -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Serializer

	python3 dch.py -cs -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}