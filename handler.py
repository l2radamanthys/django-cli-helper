import os
import simple_view

dist_path = "dist"
current_path = os.path.abspath(os.path.dirname(__file__))
call_path = os.path.join(os.getcwd(), dist_path)


def crear_vista(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace("-", " ").replace("_", " ")
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)
    data = {
        # 'modelo': simple_view.pascal_case(nombre),
        "modelo": nombre,
        "nombre_archivo": nombre_archivo,
        "app": app,
    }
    component_ = "views"
    validar_carpeta(call_path)
    validar_carpeta(os.path.join(call_path, app))
    validar_carpeta(os.path.join(call_path, app, component_))
    view = simple_view.View(
        template_path=os.path.join(current_path, "templates/view.py")
    )
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"AGREGADO: {partial_output_path}")
    print(f"from {app}.{component_}.{nombre_archivo} import {nombre}View")


def crear_modelo(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace("-", " ").replace("_", " ")
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)

    data = {
        "modelo": nombre,
        "nombre_plural": nombre_plural,
        "nombre_tabla": nombre_archivo,
    }
    component_ = "models"
    # validar estructura de archivos
    validar_carpeta(call_path)
    validar_carpeta(os.path.join(call_path, app))
    validar_carpeta(os.path.join(call_path, app, component_))
    view = simple_view.View(
        template_path=os.path.join(current_path, "templates/model.py")
    )
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"AGREGADO: {partial_output_path}")
    print(f"from {app}.{component_}.{nombre_archivo} import {nombre}")


def crear_admin_class(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace("-", " ").replace("_", " ")
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)

    data = {"modelo": nombre, "nombre_archivo": nombre_archivo, "app": app}
    component_ = "admin_class"
    validar_carpeta(call_path)
    validar_carpeta(os.path.join(call_path, app))
    validar_carpeta(os.path.join(call_path, app, component_))
    view = simple_view.View(
        template_path=os.path.join(current_path, "templates/admin.py")
    )
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"AGREGADO: {partial_output_path}")
    print(f"from {app}.{component_}.{nombre_archivo} import {nombre}Admin")


def crear_serializer(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace("-", " ").replace("_", " ")
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)

    data = {"modelo": nombre, "nombre_archivo": nombre_archivo, "app": app}
    component_ = "serializers"
    validar_carpeta(call_path)
    validar_carpeta(os.path.join(call_path, app))
    validar_carpeta(os.path.join(call_path, app, component_))
    view = simple_view.View(
        template_path=os.path.join(current_path, "templates/serializer.py")
    )
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"AGREGADO: {partial_output_path}")
    print(f"from {app}.{component_}.{nombre_archivo} import {nombre}Serializer")


def crear_test(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace("-", " ").replace("_", " ")
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_plural_ = nombre_archivo
    nombre_modelo = simple_view.to_pascal(nombre_archivo)
    nombre_archivo = "test_api_" + nombre_modelo
    modelo_url = nombre_plural_.replace("_", "-").lower()

    data = {
        "modelo": nombre,
        "nombre_archivo": nombre_archivo,
        "nombre_modelo": nombre_modelo,
        "nombre_plural": nombre_plural_,
        "modelo_url": modelo_url,
        "app": app,
    }

    component_ = "tests"
    validar_carpeta(call_path)
    validar_carpeta(os.path.join(call_path, app))
    validar_carpeta(os.path.join(call_path, app, component_))
    view = simple_view.View(
        template_path=os.path.join(current_path, "templates/test.py")
    )
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"AGREGADO: {partial_output_path}")
    # print(f"from {app}.{component_}.{nombre_archivo} import {nombre}")


def touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, "a").close()


def validar_carpeta(path, archivo_init=False):
    if not os.path.isdir(path):
        os.mkdir(path)
        # print(f'Agregado {path}')
        if archivo_init:
            touch(os.path.join(path, "__init__.py"))
            # print(f'Agregado {path}/__init__.py')


def actualizar_estructura_app(app):
    carpetas = [
        "admin_class",
        "tests",
        "models",
        "serializers",
        "views",
        "jobs",
        "signals",
    ]
    borrar = ["models.py", "views.py", "tests.py"]

    if not os.path.exists(app):
        raise Exception(f"Error, no se encontro la app: {app}")

    for archivo in borrar:
        path = os.path.join(app, archivo)
        if os.path.exists(path):
            os.remove(path)
            print(f"Quitado {path}")

    for carpeta in carpetas:
        path = os.path.join(app, carpeta)
        if os.path.isdir(path):
            print(f"Omitido, ya existe el directorio, {path}")
        else:
            os.mkdir(path)
            touch(os.path.join(path, "__init__.py"))
            print(f"Agregado {path}")
            print(f"Agregado {path}/__init__.py")
