"""
Funciones utilitarias para procesamiento y análisis de datos
"""

def validar_numeros(lista):
    """
    Valida que todos los elementos de una lista sean numéricos
    """
    return all(isinstance(x, (int, float)) for x in lista)


def media(lista):
    """
    Calcula la media aritmética de una lista de números
    """
    if not validar_numeros(lista):
        raise ValueError("La lista contiene valores no numéricos")
    return sum(lista) / len(lista)


def varianza(lista):
    """
    Calcula la varianza poblacional
    """
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / len(lista)
