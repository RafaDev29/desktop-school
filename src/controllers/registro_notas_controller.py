from PyQt5.QtWidgets import QMainWindow, QMessageBox
from src.windows.registro_notas_window import Ui_RegistroNotas
from src.services.notas_service import guardar_notas

class RegistroNotasController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroNotas()
        self.ui.setupUi(self)

        self.ui.btnRegistrarNota.clicked.connect(self.registrar_nota)

    def registrar_nota(self):
        dni = self.ui.txtDNI.text().strip()
        nota1 = self.ui.txtNota1.text().strip()
        nota2 = self.ui.txtNota2.text().strip()
        nota3 = self.ui.txtNota3.text().strip()

        if not dni or not nota1 or not nota2 or not nota3:
            QMessageBox.warning(self, "Campos vacíos", "Completa todos los campos.")
            return

        guardar_notas(dni, nota1, nota2, nota3)
        QMessageBox.information(self, "Éxito", "Notas registradas correctamente.")

        self.ui.txtDNI.clear()
        self.ui.txtNota1.clear()
        self.ui.txtNota2.clear()
        self.ui.txtNota3.clear()
