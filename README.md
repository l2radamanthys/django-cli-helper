# Django CLI Helper

Herramienta de línea de comandos para **generar estructura compatible con Django REST Framework**.  
Facilita la creación de modelos, vistas, serializers, clases de administrador y árboles de modelos en proyectos Django.

---

## 🚀 Características
- Generación rápida de estructuras para **Django REST Framework**.  
- Comandos simples para crear:
  - Modelos
  - Vistas
  - Serializers
  - Clases de administrador
  - Árbol de modelos
- Automatización de la estructura de aplicaciones.

---

## 📦 Instalación

Clonar el repositorio y entrar en el directorio:

```bash
git clone https://github.com/tu_usuario/django-cli-helper.git
cd django-cli-helper
```

Ejecutar con Python 3:

```bash
python3 cli.py [opciones]
```

---

## 🛠️ Comandos disponibles

### 🔄 Actualizar estructura de la app
```bash
python3 cli.py -aa {nombre_app}
```

### 🌳 Generar árbol del modelo
```bash
python3 cli.py -g -a {nombre_app} -n {nombre_modelo} -np {nombre_plural}
```

### 📌 Crear Modelo
```bash
python3 cli.py -cm -a {nombre_app} -n {nombre_modelo} -np {nombre_plural}
```

### 👁️ Crear Vista
```bash
python3 cli.py -cv -a {nombre_app} -n {nombre_modelo} -np {nombre_plural}
```

### 🛠️ Crear Admin class
```bash
python3 cli.py -ca -a {nombre_app} -n {nombre_modelo} -np {nombre_plural}
```

### 🔗 Crear Serializer
```bash
python3 cli.py -cs -a {nombre_app} -n {nombre_modelo} -np {nombre_plural}
```

---

## 📖 Ejemplo de uso

```bash
# Crear un modelo "Producto" en la app "inventario"
python3 cli.py -cm -a inventario -n Producto -np Productos

# Crear un serializer para el mismo modelo
python3 cli.py -cs -a inventario -n Producto -np Productos
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Si quieres mejorar el proyecto, haz un fork, crea una rama y abre un **Pull Request**.

---
