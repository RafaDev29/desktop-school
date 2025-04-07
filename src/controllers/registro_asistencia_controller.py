from PyQt5.QtWidgets import QMainWindow, QMessageBox
from src.windows.registro_asistencia_window import Ui_RegistroAsistencia
from src.services.asistencia_service import guardar_asistencia

class RegistroAsistenciaController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegistroAsistencia()
        self.ui.setupUi(self)

        self.ui.btnRegistrarAsistencia.clicked.connect(self.registrar)

    def registrar(self):
        dni = self.ui.txtDNI.text().strip()
        fecha = self.ui.dateFecha.date().toString("yyyy-MM-dd")
        estado = "Presente" if self.ui.radioPresente.isChecked() else "Ausente"

        if not dni:
            QMessageBox.warning(self, "Campo vacío", "Debes ingresar el DNI.")
            return

        guardar_asistencia(dni, fecha, estado)
        QMessageBox.information(self, "Éxito", "Asistencia registrada correctamente.")

        self.ui.txtDNI.clear()
        self.ui.radioPresente.setChecked(True)
