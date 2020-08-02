import argparse
import handler


current_version = 'v0.0.1'


def main():
    parser = argparse.ArgumentParser(
        description='Django Cli Helper'
    )

    parser.add_argument(
        'g',
        '--generate',
        action='store_true',
        default=False,
        dest='generar',
    )

    parser.add_argument(
        'path-app',
        action='store_true',
        default=False,
        dest='path_app',
    )

    parser.add_argument(
        '-cv',
        '--create-view',
        action='store_true',
        dest='view',
        help='crear una vista'
    )

    parser.add_argument(
        '-n',
        '--nombre',
        action='store',
        default=False,
        dest='nombre',
        help='Nombre del archivo'
    )

    parser.add_argument(
        '-np',
        '--nombre-plural',
        action='store',
        dest='nombre_plural',
        help='Nombre plural'
    )

    parser.add_argument(
        '-a',
        '--app',
        action='store',
        dest='app_name',
        help='nombre de la aplicación'
    )

    args = parser.parse_args()
    nombre_plural = None

    if not args.nombre:
        print("Error falta parametro -n nombre")
        return -1

    if not args.app_name:
        print("Error falta parametro -a app")
        return -1

    if args.nombre_plural:
        nombre_plural = args.nombre_plural
    else:
        nombre_plural = args.nombre

    if args.view:
        handler.crear_vista(args.app_name, args.nombre, nombre_plural)

    print()

if __name__ == '__main__':
    main()

