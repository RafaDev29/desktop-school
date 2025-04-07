from PyQt5 import QtCore, QtWidgets

class Ui_RegistroAsistencia(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.txtDNI = QtWidgets.QLineEdit(Form)
        self.txtDNI.setGeometry(QtCore.QRect(100, 30, 200, 22))
        self.txtDNI.setPlaceholderText("DNI")
        self.txtDNI.setObjectName("txtDNI")

        self.dateFecha = QtWidgets.QDateEdit(Form)
        self.dateFecha.setGeometry(QtCore.QRect(100, 70, 200, 22))
        self.dateFecha.setCalendarPopup(True)
        self.dateFecha.setDate(QtCore.QDate.currentDate())
        self.dateFecha.setObjectName("dateFecha")

        self.radioPresente = QtWidgets.QRadioButton(Form)
        self.radioPresente.setGeometry(QtCore.QRect(100, 110, 100, 20))
        self.radioPresente.setText("Presente")
        self.radioPresente.setChecked(True)

        self.radioAusente = QtWidgets.QRadioButton(Form)
        self.radioAusente.setGeometry(QtCore.QRect(200, 110, 100, 20))
        self.radioAusente.setText("Ausente")

        self.btnRegistrarAsistencia = QtWidgets.QPushButton(Form)
        self.btnRegistrarAsistencia.setGeometry(QtCore.QRect(140, 160, 120, 28))
        self.btnRegistrarAsistencia.setObjectName("btnRegistrarAsistencia")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Asistencia"))
        self.btnRegistrarAsistencia.setText(_translate("Form", "Registrar Asistencia"))
