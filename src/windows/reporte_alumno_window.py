from PyQt5 import QtCore, QtWidgets

class Ui_ReporteAlumnos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)

        self.tableAlumnos = QtWidgets.QTableWidget(Form)
        self.tableAlumnos.setGeometry(QtCore.QRect(20, 20, 460, 250))
        self.tableAlumnos.setObjectName("tableAlumnos")
        self.tableAlumnos.setColumnCount(2)
        self.tableAlumnos.setHorizontalHeaderLabels(["DNI", "Nombre"])
        self.tableAlumnos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAlumnos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reporte de Alumnos"))
