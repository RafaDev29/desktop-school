from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from src.windows.reporte_alumno_window import Ui_ReporteAlumnos
import os

class ReporteAlumnosController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReporteAlumnos()
        self.ui.setupUi(self)
        self.cargar_tabla()

    def cargar_tabla(self):
        archivo = "data/Alum_Reg.txt"
        self.ui.tableAlumnos.setRowCount(0)

        if not os.path.exists(archivo):
            return

        with open(archivo, "r", encoding="utf-8") as f:
            for row_idx, line in enumerate(f):
                datos = line.strip().split(",", 1)
                self.ui.tableAlumnos.insertRow(row_idx)
                for col_idx, valor in enumerate(datos):
                    self.ui.tableAlumnos.setItem(row_idx, col_idx, QTableWidgetItem(valor))
