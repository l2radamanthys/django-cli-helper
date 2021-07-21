# Django Cli Helper

Utilidad para generar extructura compatible con Django-REST-Frameworks


## Comandos

#### Actualizar estructura de la app

	python3 cli.py -aa {nombre_app}

#### Generar arbol del modelo

	python3 cli.py -g -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Modelo
	
	python3 cli.py -cm -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Vista
	
	python3 cli.py -cv -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Admin class
	
	python3 cli.py -ca -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}
	
#### Crear Serializer

	python3 cli.py -cs -a {nombre_app} -n {nombre_modelo} -np {nombre_prural}