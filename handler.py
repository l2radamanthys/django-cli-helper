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
    }
    view = simple_view.View(template_path=os.path.join(current_path, 'templates/view.py'))
    output_path = os.path.join(call_path, app, 'views', f"{nombre_archivo}.py")
    partial_output_path = os.path.join(app, 'views', f"{nombre_archivo}.py")
    view.build_and_save(data, output_path)
    print(f"\nAGREGADO: {partial_output_path}\n")
    print(f"from {app}.views.{nombre_archivo} import {nombre}ViewSet\n")
    print()


