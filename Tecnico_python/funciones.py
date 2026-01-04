import random
import pandas as pd

# -----------------------------
# Funciones del sistema
# -----------------------------

def formatea_nombre(nombre, paterno, materno):
    return nombre.upper() + " " + paterno.capitalize() + " " + materno.capitalize()

def crea_clave(nombre_completo, anio_nacimiento):
    clave = ""
    for palabra in nombre_completo.split():
        clave += palabra[0]
    return clave + str(anio_nacimiento)[-2:]


# -----------------------------
# Generación de datos sintéticos
# -----------------------------

nombres = ["juan", "maria", "pedro", "ana", "luis", "carlos", "laura", "jose", "andrea", "miguel"]
apellidos = ["hernandez", "jimenez", "perez", "gomez", "ramirez", "diaz", "castillo", "martinez"]

registros = []

cantidad_registros = 100  # puedes aumentar a 1000 o 10000

for _ in range(cantidad_registros):
    nombre = random.choice(nombres)
    paterno = random.choice(apellidos)
    materno = random.choice(apellidos)
    anio_nacimiento = random.randint(1960, 2005)

    nombre_completo = formatea_nombre(nombre, paterno, materno)
    clave = crea_clave(nombre_completo, anio_nacimiento)

    registros.append({
        "nombre": nombre,
        "apellido_paterno": paterno,
        "apellido_materno": materno,
        "anio_nacimiento": anio_nacimiento,
        "nombre_formateado": nombre_completo,
        "clave": clave
    })


# -----------------------------
# Crear DataFrame
# -----------------------------

df = pd.DataFrame(registros)

# Mostrar las primeras filas
df.head()
