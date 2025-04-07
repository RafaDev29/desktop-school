import os

ARCHIVO_ALUMNOS = "data/Alum_Reg.txt"

def guardar_alumno(dni, nombre):
    with open(ARCHIVO_ALUMNOS, "a", encoding="utf-8") as f:
        f.write(f"{dni},{nombre}\n")

def buscar_alumno_por_dni(dni):
    if not os.path.exists(ARCHIVO_ALUMNOS):
        return None

    with open(ARCHIVO_ALUMNOS, "r", encoding="utf-8") as f:
        for linea in f:
            parts = linea.strip().split(",")
            if parts[0] == dni:
                return parts[1]  # nombre

    return None
