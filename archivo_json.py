import json

# JSON file name
ARCHIVO = "coleccion.json"


def cargar_datos():
    """
    Load data from the JSON file.
    Returns a list.
    """

    try:

        with open(
            ARCHIVO,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(
                archivo
            )

    except FileNotFoundError:

        # If the file does not exist,
        # return an empty list
        return []

    except json.JSONDecodeError:

        print(
            "Error: Corrupted JSON file."
        )

        return []

    except Exception as error:

        print(
            f"Unexpected error: {error}"
        )

        return []


def guardar_datos(coleccion):
    """
    Save the collection to the JSON file.
    """

    try:

        with open(
            ARCHIVO,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(

                coleccion,

                archivo,

                indent=4,

                ensure_ascii=False

            )

    except Exception as error:

        print(
            f"Error saving data: {error}"
        )
