import os


def limpiar_pantalla():
    """
    Clear the console screen.
    Works on Windows and Linux.
    """

    os.system(
        "cls" if os.name == "nt"
        else "clear"
    )


def pausar():
    """
    Pause program execution until
    the user presses ENTER.
    """

    input(
        "\nPress ENTER to continue..."
    )


def mostrar_estrellas(valoracion):
    """
    Convert a numeric rating into stars.

    Example:
    5 -> ⭐⭐⭐⭐⭐
    3 -> ⭐⭐⭐☆☆
    """

    return (

        "⭐" * valoracion

        +

        "☆" * (5 - valoracion)

    )
