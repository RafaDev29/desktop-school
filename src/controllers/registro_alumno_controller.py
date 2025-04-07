from PyQt5.QtWidgets import QMainWindow, QMessageBox
from src.windows.registro_alumno_window import Ui_RegistroAlumno
from src.services.alumno_service import guardar_alumno, buscar_alumno_por_dni
from PyQt5 import QtWidgets

class RegistroAlumnoController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroAlumno()
        self.ui.setupUi(self)
        self.cargar_tabla()
        self.ui.btnRegistrar.clicked.connect(self.registrar)
        self.ui.btnVerTodos.clicked.connect(self.cargar_tabla)


    def registrar(self):
        dni = self.ui.txtDNI.text().strip()
        nombre = self.ui.txtNombre.text().strip()

        if not dni or not nombre:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return

        ya_existe = buscar_alumno_por_dni(dni)
        if ya_existe:
            QMessageBox.information(self, "Ya existe", f"El alumno con DNI {dni} ya está registrado como: {ya_existe}")
            return

        guardar_alumno(dni, nombre)
        QMessageBox.information(self, "Éxito", "Alumno registrado correctamente.")

        self.ui.txtDNI.clear()
        self.ui.txtNombre.clear()
        self.cargar_tabla()


    def cargar_tabla(self):
        from src.services.alumno_service import ARCHIVO_ALUMNOS
        self.ui.tableAlumnos.setRowCount(0)

        try:
            with open(ARCHIVO_ALUMNOS, "r", encoding="utf-8") as f:
                for row_idx, line in enumerate(f):
                    dni, nombre = line.strip().split(",", 1)
                    self.ui.tableAlumnos.insertRow(row_idx)
                    self.ui.tableAlumnos.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(dni))
                    self.ui.tableAlumnos.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(nombre))
        except FileNotFoundError:
            pass

