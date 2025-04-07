import os

ARCHIVO_NOTAS = "data/Alum_Notas.txt"

def guardar_notas(dni, nota1, nota2, nota3):
    with open(ARCHIVO_NOTAS, "a", encoding="utf-8") as f:
        f.write(f"{dni},{nota1},{nota2},{nota3}\n")
