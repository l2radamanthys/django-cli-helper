import os
import simple_view


current_path = os.path.abspath(os.path.dirname(__file__))
call_path = os.getcwd()


def crear_vista(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace('-', ' ').replace('_', ' ')
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)
    data = {
        # 'modelo': simple_view.pascal_case(nombre),
        'modelo': nombre,
        'nombre_archivo': nombre_archivo,
        'app': app
    }
    view = simple_view.View(template_path=os.path.join(current_path, 'templates/view.py'))
    output_path = os.path.join(call_path, app, 'views', f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, 'views', f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"\nAGREGADO: {partial_output_path}\n")
    print(f"from {app}.views.{nombre_archivo} import {nombre}ViewSet\n")
    print()


def crear_modelo(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace('-', ' ').replace('_', ' ')
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)
    
    data = {
        'modelo': nombre,
        'nombre_plural': nombre_plural,
        'nombre_tabla': nombre_archivo,
    }
    view = simple_view.View(template_path=os.path.join(current_path, 'templates/model.py'))
    output_path = os.path.join(call_path, app, 'models', f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, 'models', f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"\nAGREGADO: {partial_output_path}\n")
    print(f"from {app}.models.{nombre_archivo} import {nombre}\n")
    print()


def crear_admin_class(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace('-', ' ').replace('_', ' ')
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)
    
    data = {
        'modelo': nombre,
        'nombre_archivo': nombre_archivo,
        'app': app
    }
    view = simple_view.View(template_path=os.path.join(current_path, 'templates/admin.py'))
    output_path = os.path.join(call_path, app, 'admin_class', f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, 'admin_class', f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"\nAGREGADO: {partial_output_path}\n")
    print(f"from {app}.admin_class.{nombre_archivo} import {nombre}\n")
    print()

def crear_serializer(app, nombre, nombre_plural):
    nombre_archivo = nombre_plural.replace('-', ' ').replace('_', ' ')
    nombre_archivo = simple_view.pascal_case(nombre_archivo)
    nombre_archivo = simple_view.to_pascal(nombre_archivo)
    
    data = {
        'modelo': nombre,
        'nombre_archivo': nombre_archivo,
        'app': app
    }
    component_ = 'serializers'
    view = simple_view.View(template_path=os.path.join(current_path, 'templates/serializer.py'))
    output_path = os.path.join(call_path, app, component_, f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, component_, f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"\nAGREGADO: {partial_output_path}\n")
    print(f"from {app}.{component_}.{nombre_archivo} import {nombre}\n")
    print()
