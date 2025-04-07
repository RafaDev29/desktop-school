from PyQt5.QtWidgets import QMainWindow
from src.windows.menu_window import Ui_MainMenu
from src.controllers.registro_alumno_controller import RegistroAlumnoController
from src.controllers.registro_notas_controller import RegistroNotasController
from src.controllers.reporte_notas_controller import ReporteNotasController
from src.controllers.registro_asistencia_controller import RegistroAsistenciaController
from src.controllers.reporte_asistencia_controller import ReporteAsistenciaController
from src.controllers.reporte_alumno_controller import ReporteAlumnosController

class MenuController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        # Acciones de cada botón
        self.ui.btnRegistroAlumnos.clicked.connect(self.ir_a_registro_alumnos)
        self.ui.btnRegistroNotas.clicked.connect(self.ir_a_registro_notas)
        self.ui.btnRegistroAsistencia.clicked.connect(self.ir_a_registro_asistencia)
        self.ui.btnReporteAlumnos.clicked.connect(self.ir_a_reporte_alumnos)
        self.ui.btnReporteNotas.clicked.connect(self.ir_a_reporte_notas)
        self.ui.btnReporteAsistencia.clicked.connect(self.ir_a_reporte_asistencia)

    def ir_a_registro_alumnos(self):
        self.ventanaRegistro = RegistroAlumnoController()
        self.ventanaRegistro.show()


    def ir_a_registro_notas(self):
        self.ventanaNotas = RegistroNotasController()
        self.ventanaNotas.show()


    def ir_a_registro_asistencia(self):
        self.ventanaAsistencia = RegistroAsistenciaController()
        self.ventanaAsistencia.show()


    def ir_a_reporte_alumnos(self):
        self.ventanaReporteAlumnos = ReporteAlumnosController()
        self.ventanaReporteAlumnos.show()


    def ir_a_reporte_notas(self):
        self.ventanaReporteNotas = ReporteNotasController()
        self.ventanaReporteNotas.show()


    def ir_a_reporte_asistencia(self):
        self.ventanaReporteAsistencia = ReporteAsistenciaController()
        self.ventanaReporteAsistencia.show()
