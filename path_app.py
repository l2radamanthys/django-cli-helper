import os
import sys
import simple_view


call_path = os.getcwd()


def touch(path):
    with open(path, "a"):
        os.utime(path, None)


def crear_python_dir(path):
    os.mkdir(path)
    touch(os.path.join(path, "__init__.py"))


def actualizar_esquema_app(nombre_app):
    app_path = os.path.join(call_path, nombre_app)
    if os.path.exists(app_path):
        crear_python_dir(os.path.join(app_path, "admin_class"))
        crear_python_dir(os.path.join(app_path, "models"))
        crear_python_dir(os.path.join(app_path, "serializers"))
        crear_python_dir(os.path.join(app_path, "views"))
        crear_python_dir(os.path.join(app_path, "tests"))
        os.remove(os.path.join(app_path, "views.py"))
        os.remove(os.path.join(app_path, "models.py"))
        os.remove(os.path.join(app_path, "tests.py"))
    else:
        print("Error app {nombre_app} no existe")


if len(sys.argv) == 2:
    actualizar_esquema_app(sys.argv[1])
