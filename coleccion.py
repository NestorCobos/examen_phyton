from tabulate import tabulate

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from archivo_json import guardar_datos
from utilidades import mostrar_estrellas


def obtener_titulos(coleccion):
    """
    Return all titles from the collection.
    """

    return [

        elemento["titulo"]

        for elemento in coleccion

    ]


def obtener_generos(coleccion):
    """
    Return all genres from the collection.
    """

    return list(

        set(

            elemento["genero"]

            for elemento in coleccion

        )

    )


def obtener_responsables(coleccion):
    """
    Return all authors/directors/artists.
    """

    return list(

        set(

            elemento["responsable"]

            for elemento in coleccion

        )

    )


def agregar_elemento(coleccion):
    """
    Add a new item to the collection.
    """

    try:

        print(
            "\n===== ADD ITEM ====="
        )

        titulo = input(
            "Title: "
        ).strip()

        if titulo == "":

            print(
                "Title cannot be empty."
            )

            return

        for elemento in coleccion:

            if (

                elemento["titulo"].lower()

                ==

                titulo.lower()

            ):

                print(
                    "This title already exists."
                )

                return

        print(
            "\nSelect category:"
        )

        print("1. Book")
        print("2. Movie")
        print("3. Music")

        opcion = input(
            "Option: "
        ).strip()

        tipos = {

            "1": "Libro",

            "2": "Película",

            "3": "Música"

        }

        if opcion not in tipos:

            print(
                "Invalid option."
            )

            return

        tipo = tipos[opcion]

        responsable = input(
            "Author / Director / Artist: "
        ).strip()

        genero = input(
            "Genre: "
        ).strip()

        valoracion = input(
            "Rating (1-5, optional): "
        ).strip()

        if valoracion == "":

            valoracion = None

        else:

            try:

                valoracion = int(
                    valoracion
                )

                if (

                    valoracion < 1

                    or

                    valoracion > 5

                ):

                    print(
                        "Rating must be between 1 and 5."
                    )

                    return

            except ValueError:

                print(
                    "Invalid rating."
                )

                return

        nuevo_elemento = {

            "titulo": titulo,

            "tipo": tipo,

            "responsable": responsable,

            "genero": genero,

            "valoracion": valoracion

        }

        coleccion.append(
            nuevo_elemento
        )

        guardar_datos(
            coleccion
        )

        print(
            "\nItem added successfully."
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )


def listar_elementos(coleccion):
    """
    Display all items.
    """

    try:

        if len(coleccion) == 0:

            print(
                "No items found."
            )

            return

        tabla = []

        for elemento in coleccion:

            valoracion = elemento[
                "valoracion"
            ]

            if valoracion is None:

                valoracion = (
                    "No rating"
                )

            else:

                valoracion = (
                    mostrar_estrellas(
                        valoracion
                    )
                )

            tabla.append([

                elemento["titulo"],

                elemento["tipo"],

                elemento["responsable"],

                elemento["genero"],

                valoracion

            ])

        print(

            tabulate(

                tabla,

                headers=[

                    "Title",

                    "Category",

                    "Responsible",

                    "Genre",

                    "Rating"

                ],

                tablefmt="grid"

            )

        )

    except Exception as error:

        print(
            f"Error: {error}"
        )


def buscar_elemento(coleccion):
    """
    Search by title,
    responsible or genre.
    """

    try:

        print(
            "\n===== SEARCH ====="
        )

        print("1. Title")
        print("2. Responsible")
        print("3. Genre")

        opcion = input(
            "Option: "
        ).strip()

        if opcion == "1":

            datos = obtener_titulos(
                coleccion
            )

        elif opcion == "2":

            datos = obtener_responsables(
                coleccion
            )

        elif opcion == "3":

            datos = obtener_generos(
                coleccion
            )

        else:

            print(
                "Invalid option."
            )

            return

        completer = WordCompleter(

            datos,

            ignore_case=True

        )

        criterio = prompt(

            "Search: ",

            completer=completer

        ).strip().lower()

        resultados = []

        for elemento in coleccion:

            encontrado = False

            if (

                opcion == "1"

                and

                criterio

                in

                elemento["titulo"].lower()

            ):

                encontrado = True

            elif (

                opcion == "2"

                and

                criterio

                in

                elemento["responsable"].lower()

            ):

                encontrado = True

            elif (

                opcion == "3"

                and

                criterio

                in

                elemento["genero"].lower()

            ):

                encontrado = True

            if encontrado:

                valoracion = elemento[
                    "valoracion"
                ]

                if valoracion is None:

                    valoracion = (
                        "No rating"
                    )

                else:

                    valoracion = (
                        mostrar_estrellas(
                            valoracion
                        )
                    )

                resultados.append([

                    elemento["titulo"],

                    elemento["tipo"],

                    elemento["responsable"],

                    elemento["genero"],

                    valoracion

                ])

        if len(resultados) == 0:

            print(
                "No results found."
            )

            return

        print(

            tabulate(

                resultados,

                headers=[

                    "Title",

                    "Category",

                    "Responsible",

                    "Genre",

                    "Rating"

                ],

                tablefmt="grid"

            )

        )

    except Exception as error:

        print(
            f"Error: {error}"
        )
def editar_elemento(coleccion):
    """
    Edit any field of an item.
    """

    try:

        titulos = obtener_titulos(
            coleccion
        )

        completer = WordCompleter(

            titulos,

            ignore_case=True

        )

        titulo = prompt(

            "Title to edit: ",

            completer=completer

        ).strip().lower()

        for elemento in coleccion:

            if (

                elemento["titulo"].lower()

                ==

                titulo

            ):

                print(
                    "\n===== EDIT ITEM ====="
                )

                print("1. Title")
                print("2. Category")
                print("3. Responsible")
                print("4. Genre")
                print("5. Rating")
                print("6. Edit all")

                opcion = input(
                    "\nOption: "
                ).strip()

                if opcion == "1":

                    nuevo_titulo = input(
                        "New title: "
                    ).strip()

                    if nuevo_titulo != "":

                        elemento[
                            "titulo"
                        ] = nuevo_titulo

                elif opcion == "2":

                    print(
                        "\n1. Libro"
                    )

                    print(
                        "2. Película"
                    )

                    print(
                        "3. Música"
                    )

                    categoria = input(
                        "Option: "
                    ).strip()

                    tipos = {

                        "1": "Libro",

                        "2": "Película",

                        "3": "Música"

                    }

                    if categoria in tipos:

                        elemento[
                            "tipo"
                        ] = tipos[
                            categoria
                        ]

                elif opcion == "3":

                    elemento[
                        "responsable"
                    ] = input(
                        "New responsible: "
                    ).strip()

                elif opcion == "4":

                    elemento[
                        "genero"
                    ] = input(
                        "New genre: "
                    ).strip()

                elif opcion == "5":

                    try:

                        valoracion = int(

                            input(
                                "New rating (1-5): "
                            )

                        )

                        if (

                            1 <= valoracion <= 5

                        ):

                            elemento[
                                "valoracion"
                            ] = valoracion

                        else:

                            print(
                                "Rating must be between 1 and 5."
                            )

                            return

                    except ValueError:

                        print(
                            "Invalid rating."
                        )

                        return

                elif opcion == "6":

                    nuevo_titulo = input(
                        "New title: "
                    ).strip()

                    if nuevo_titulo != "":

                        elemento[
                            "titulo"
                        ] = nuevo_titulo

                    print(
                        "\n1. Libro"
                    )

                    print(
                        "2. Película"
                    )

                    print(
                        "3. Música"
                    )

                    categoria = input(
                        "Category option: "
                    ).strip()

                    tipos = {

                        "1": "Libro",

                        "2": "Película",

                        "3": "Música"

                    }

                    if categoria in tipos:

                        elemento[
                            "tipo"
                        ] = tipos[
                            categoria
                        ]

                    responsable = input(
                        "New responsible: "
                    ).strip()

                    if responsable != "":

                        elemento[
                            "responsable"
                        ] = responsable

                    genero = input(
                        "New genre: "
                    ).strip()

                    if genero != "":

                        elemento[
                            "genero"
                        ] = genero

                    valoracion = input(
                        "New rating (1-5): "
                    ).strip()

                    if valoracion != "":

                        try:

                            valoracion = int(
                                valoracion
                            )

                            if (

                                1 <= valoracion <= 5

                            ):

                                elemento[
                                    "valoracion"
                                ] = valoracion

                        except ValueError:

                            pass

                else:

                    print(
                        "Invalid option."
                    )

                    return

                guardar_datos(
                    coleccion
                )

                print(
                    "\nItem updated successfully."
                )

                return

        print(
            "Item not found."
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )
def eliminar_elemento(coleccion):
    """
    Delete an item from the collection.
    """

    try:

        titulos = obtener_titulos(
            coleccion
        )

        completer = WordCompleter(

            titulos,

            ignore_case=True

        )

        titulo = prompt(

            "Title to delete: ",

            completer=completer

        ).strip().lower()

        for i, elemento in enumerate(
            coleccion
        ):

            if (

                elemento["titulo"].lower()

                ==

                titulo

            ):

                confirmar = input(

                    "Are you sure? (s/n): "

                ).lower()

                if confirmar == "s":

                    coleccion.pop(i)

                    guardar_datos(
                        coleccion
                    )

                    print(
                        "Item deleted successfully."
                    )

                else:

                    print(
                        "Operation cancelled."
                    )

                return

        print(
            "Item not found."
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )
def mostrar_recomendados(coleccion):
    """
    Show items with maximum rating.
    """

    try:

        recomendados = []

        for elemento in coleccion:

            if (

                elemento.get(
                    "valoracion"
                )

                == 5

            ):

                recomendados.append([

                    elemento["titulo"],

                    elemento["tipo"],

                    elemento["responsable"],

                    elemento["genero"],

                    "⭐⭐⭐⭐⭐"

                ])

        if len(recomendados) == 0:

            print(
                "No recommended items found."
            )

            return

        print(
            "\n===== RECOMMENDED ITEMS ====="
        )

        print(

            tabulate(

                recomendados,

                headers=[

                    "Title",

                    "Category",

                    "Responsible",

                    "Genre",

                    "Rating"

                ],

                tablefmt="grid"

            )

        )

    except Exception as error:

        print(
            f"Error: {error}"
        )
