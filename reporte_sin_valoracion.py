import json

from tabulate import tabulate

from archivo_json import guardar_datos


def obtener_sin_valoracion(coleccion):
    """
    Get all items without a rating.
    """

    elementos = []

    for elemento in coleccion:

        if elemento.get(
            "valoracion"
        ) is None:

            elementos.append(
                elemento
            )

    return elementos


def guardar_reporte_sin_valoracion(
    elementos
):
    """
    Generate the file:
    sin_valoracion.json
    """

    datos = []

    for elemento in elementos:

        datos.append({

            "titulo":
            elemento["titulo"],

            "autor":
            elemento["responsable"],

            "categoria":
            elemento["tipo"]

        })

    try:

        with open(

            "sin_valoracion.json",

            "w",

            encoding="utf-8"

        ) as archivo:

            json.dump(

                datos,

                archivo,

                indent=4,

                ensure_ascii=False

            )

    except Exception as error:

        print(
            f"Error creating report: {error}"
        )


def actualizar_valoracion(
    coleccion
):
    """
    Allow the user to update
    ratings from the report.
    """

    elementos = obtener_sin_valoracion(
        coleccion
    )

    if len(elementos) == 0:

        return

    opcion = input(

        "\nDo you want to assign a rating? (s/n): "

    ).lower()

    if opcion != "s":

        return

    try:

        print(
            "\n===== ITEMS WITHOUT RATING ====="
        )

        for i, elemento in enumerate(

            elementos,

            start=1

        ):

            print(
                f"{i}. {elemento['titulo']}"
            )

        indice = int(

            input(
                "\nSelect item number: "
            )

        ) - 1

        if (

            indice < 0

            or

            indice >= len(elementos)

        ):

            print(
                "Invalid option."
            )

            return

        valoracion = int(

            input(
                "New rating (1-5): "
            )

        )

        if 1 <= valoracion <= 5:

            elementos[indice][
                "valoracion"
            ] = valoracion

            guardar_datos(
                coleccion
            )

            print(
                "\nRating updated successfully."
            )

        else:

            print(
                "Rating must be between 1 and 5."
            )

    except ValueError:

        print(
            "You must enter a number."
        )

    except Exception as error:

        print(
            f"Unexpected error: {error}"
        )


def reporte_sin_valoracion_z(coleccion):
    """
    Generate a report of all items
    without rating.
    """

    try:

        elementos = obtener_sin_valoracion(
            coleccion
        )

        if len(elementos) == 0:

            print(
                "\nAll items have a rating."
            )

            return

        tabla = []

        for elemento in elementos:

            tabla.append([

                elemento["titulo"],

                elemento["tipo"],

                elemento["responsable"]

            ])

        print(
            "\n===== ITEMS WITHOUT RATING ====="
        )

        print(

            tabulate(

                tabla,

                headers=[

                    "Title",

                    "Category",

                    "Author / Director / Artist"

                ],

                tablefmt="grid"

            )

        )

        guardar_reporte_sin_valoracion(
            elementos
        )

        print(
            "\nReport generated successfully."
        )

        print(
            "File: sin_valoracion.json"
        )

        actualizar_valoracion(
            coleccion
        )

    except Exception as error:

        print(
            f"Error generating report: {error}"
        )
