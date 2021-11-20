import argparse
import handler


current_version = "v0.0.2"


def main():
    parser = argparse.ArgumentParser(description="Django Cli Helper")

    parser.add_argument(
        "-g",
        "--generate",
        action="store_true",
        default=False,
        dest="generar",
    )

    parser.add_argument(
        "-cv", "--create-view", action="store_true", dest="view", help="crear una vista"
    )

    parser.add_argument(
        "-cm",
        "--create-model",
        action="store_true",
        dest="model",
        help="crear un modelo",
    )

    parser.add_argument(
        "-ca",
        "--create-admin-class",
        action="store_true",
        dest="admin",
        help="crear un admin-class",
    )

    parser.add_argument(
        "-ct",
        "--create-test-class",
        action="store_true",
        dest="test",
        help="crear un test-class",
    )

    parser.add_argument(
        "-cs",
        "--create-serializer",
        action="store_true",
        dest="serializer",
        help="crear un serializer",
    )

    parser.add_argument(
        "-n",
        "--nombre",
        action="store",
        default=False,
        dest="nombre",
        help="Nombre del archivo",
    )

    parser.add_argument(
        "-np",
        "--nombre-plural",
        action="store",
        dest="nombre_plural",
        help="Nombre plural",
    )

    parser.add_argument(
        "-a", "--app", action="store", dest="app_name", help="nombre de la aplicación"
    )

    parser.add_argument(
        "-aa",
        "--actualizar-app",
        action="store",
        default=False,
        dest="actualizar_estructura",
        help="Actualizar estructura de la app",
    )

    args = parser.parse_args()
    print()

    if not args.actualizar_estructura and not args.nombre:
        print("Error falta parametro -n nombre")
        return -1

    if not args.actualizar_estructura and not args.app_name:
        print("Error falta parametro -a app")
        return -1

    if not args.actualizar_estructura and not args.nombre_plural:
        print("Error falta parametro -np nombre_plural")
        return -1

    if args.view:
        handler.crear_vista(args.app_name, args.nombre, args.nombre_plural)

    if args.model:
        handler.crear_modelo(args.app_name, args.nombre, args.nombre_plural)

    if args.admin:
        handler.crear_admin_class(args.app_name, args.nombre, args.nombre_plural)

    if args.serializer:
        handler.crear_serializer(args.app_name, args.nombre, args.nombre_plural)

    if args.test:
        handler.crear_test(args.app_name, args.nombre, args.nombre_plural)

    if args.generar:
        handler.crear_admin_class(args.app_name, args.nombre, args.nombre_plural)
        handler.crear_modelo(args.app_name, args.nombre, args.nombre_plural)
        handler.crear_serializer(args.app_name, args.nombre, args.nombre_plural)
        handler.crear_vista(args.app_name, args.nombre, args.nombre_plural)
        handler.crear_test(args.app_name, args.nombre, args.nombre_plural)

    if args.actualizar_estructura:
        handler.actualizar_estructura_app(args.actualizar_estructura)

    print()


if __name__ == "__main__":
    main()
