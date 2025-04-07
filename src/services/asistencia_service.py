import os

ARCHIVO_ASISTENCIA = "data/Alum_Asis.txt"

def guardar_asistencia(dni, fecha, estado):
    with open(ARCHIVO_ASISTENCIA, "a", encoding="utf-8") as f:
        f.write(f"{dni},{fecha},{estado}\n")
