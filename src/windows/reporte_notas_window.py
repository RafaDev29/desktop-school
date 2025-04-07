from PyQt5 import QtCore, QtWidgets

class Ui_ReporteNotas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)

        self.tableNotas = QtWidgets.QTableWidget(Form)
        self.tableNotas.setGeometry(QtCore.QRect(20, 20, 460, 250))
        self.tableNotas.setObjectName("tableNotas")
        self.tableNotas.setColumnCount(4)
        self.tableNotas.setHorizontalHeaderLabels(["DNI", "Nota 1", "Nota 2", "Nota 3"])
        self.tableNotas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableNotas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reporte de Notas"))
