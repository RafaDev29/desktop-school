from PyQt5 import QtCore, QtWidgets

class Ui_ReporteAsistencia(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)

        self.tableAsistencia = QtWidgets.QTableWidget(Form)
        self.tableAsistencia.setGeometry(QtCore.QRect(20, 20, 460, 250))
        self.tableAsistencia.setObjectName("tableAsistencia")
        self.tableAsistencia.setColumnCount(3)
        self.tableAsistencia.setHorizontalHeaderLabels(["DNI", "Fecha", "Estado"])
        self.tableAsistencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAsistencia.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reporte de Asistencia"))
