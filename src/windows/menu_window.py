from PyQt5 import QtCore, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(400, 300)

        self.btnRegistroAlumnos = QtWidgets.QPushButton(MainMenu)
        self.btnRegistroAlumnos.setGeometry(QtCore.QRect(120, 20, 160, 28))
        self.btnRegistroAlumnos.setObjectName("btnRegistroAlumnos")

        self.btnRegistroNotas = QtWidgets.QPushButton(MainMenu)
        self.btnRegistroNotas.setGeometry(QtCore.QRect(120, 60, 160, 28))
        self.btnRegistroNotas.setObjectName("btnRegistroNotas")

        self.btnRegistroAsistencia = QtWidgets.QPushButton(MainMenu)
        self.btnRegistroAsistencia.setGeometry(QtCore.QRect(120, 100, 160, 28))
        self.btnRegistroAsistencia.setObjectName("btnRegistroAsistencia")

        self.btnReporteAlumnos = QtWidgets.QPushButton(MainMenu)
        self.btnReporteAlumnos.setGeometry(QtCore.QRect(120, 140, 160, 28))
        self.btnReporteAlumnos.setObjectName("btnReporteAlumnos")

        self.btnReporteNotas = QtWidgets.QPushButton(MainMenu)
        self.btnReporteNotas.setGeometry(QtCore.QRect(120, 180, 160, 28))
        self.btnReporteNotas.setObjectName("btnReporteNotas")

        self.btnReporteAsistencia = QtWidgets.QPushButton(MainMenu)
        self.btnReporteAsistencia.setGeometry(QtCore.QRect(120, 220, 160, 28))
        self.btnReporteAsistencia.setObjectName("btnReporteAsistencia")

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Menú Principal"))
        self.btnRegistroAlumnos.setText(_translate("MainMenu", "Registro de Alumnos"))
        self.btnRegistroNotas.setText(_translate("MainMenu", "Registro de Notas"))
        self.btnRegistroAsistencia.setText(_translate("MainMenu", "Registro de Asistencia"))
        self.btnReporteAlumnos.setText(_translate("MainMenu", "Reporte de Alumnos"))
        self.btnReporteNotas.setText(_translate("MainMenu", "Reporte de Notas"))
        self.btnReporteAsistencia.setText(_translate("MainMenu", "Reporte de Asistencia"))
