from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from src.windows.reporte_notas_window import Ui_ReporteNotas
import os

class ReporteNotasController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReporteNotas()
        self.ui.setupUi(self)
        self.cargar_tabla()

    def cargar_tabla(self):
        archivo = "data/Alum_Notas.txt"
        self.ui.tableNotas.setRowCount(0)

        if not os.path.exists(archivo):
            return

        with open(archivo, "r", encoding="utf-8") as f:
            for row_idx, line in enumerate(f):
                datos = line.strip().split(",")
                self.ui.tableNotas.insertRow(row_idx)
                for col_idx, valor in enumerate(datos):
                    self.ui.tableNotas.setItem(row_idx, col_idx, QTableWidgetItem(valor))
