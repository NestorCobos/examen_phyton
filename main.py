from archivo_json import cargar_datos

from utilidades import (
    limpiar_pantalla,
    pausar
)

from coleccion import (

    agregar_elemento,

    listar_elementos,

    buscar_elemento,

    editar_elemento,

    eliminar_elemento,

    mostrar_recomendados

)

from reporte_sin_valoracion import reporte_sin_valoracion_z




def mostrar_menu():
    """
    Display the main menu.
    """

    print("\n" + "=" * 50)

    print(
        "📚 COLLECTION MANAGER 📚"
    )

    print("=" * 50)

    print(
        "1. Add item"
    )

    print(
        "2. List items"
    )

    print(
        "3. Search item"
    )

    print(
        "4. Edit item"
    )

    print(
        "5. Delete item"
    )

    print(
        "6. Show recommended items"
    )

    print(
        "7. Report items without rating"
    )

    print(
        "0. Exit"
    )

    print("=" * 50)


def main():
    """
    Main program function.
    """

    coleccion = cargar_datos()

    while True:

        try:

            limpiar_pantalla()

            mostrar_menu()

            opcion = input(

                "\nSelect an option: "

            ).strip()

            if opcion == "1":

                agregar_elemento(
                    coleccion
                )

            elif opcion == "2":

                listar_elementos(
                    coleccion
                )

            elif opcion == "3":

                buscar_elemento(
                    coleccion
                )

            elif opcion == "4":

                editar_elemento(
                    coleccion
                )

            elif opcion == "5":

                eliminar_elemento(
                    coleccion
                )

            elif opcion == "6":

                mostrar_recomendados(
                    coleccion
                )

            elif opcion == "7":

                reporte_sin_valoracion_z(coleccion)

            elif opcion == "0":

                print(
                    "\nThanks for using the system."
                )

                break

            else:

                print(
                    "\nInvalid option."
                )

            pausar()

        except KeyboardInterrupt:

            print(
                "\n\nProgram interrupted by user."
            )

            break

        except Exception as error:

            print(
                f"\nUnexpected error: {error}"
            )

            pausar()


# Program entry point
if __name__ == "__main__":

    main()
