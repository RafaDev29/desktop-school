from PyQt5 import QtCore, QtWidgets

class Ui_RegistroNotas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.txtDNI = QtWidgets.QLineEdit(Form)
        self.txtDNI.setGeometry(QtCore.QRect(100, 30, 200, 22))
        self.txtDNI.setPlaceholderText("DNI")
        self.txtDNI.setObjectName("txtDNI")

        self.txtNota1 = QtWidgets.QLineEdit(Form)
        self.txtNota1.setGeometry(QtCore.QRect(100, 70, 200, 22))
        self.txtNota1.setPlaceholderText("Nota 1")
        self.txtNota1.setObjectName("txtNota1")

        self.txtNota2 = QtWidgets.QLineEdit(Form)
        self.txtNota2.setGeometry(QtCore.QRect(100, 110, 200, 22))
        self.txtNota2.setPlaceholderText("Nota 2")
        self.txtNota2.setObjectName("txtNota2")

        self.txtNota3 = QtWidgets.QLineEdit(Form)
        self.txtNota3.setGeometry(QtCore.QRect(100, 150, 200, 22))
        self.txtNota3.setPlaceholderText("Nota 3")
        self.txtNota3.setObjectName("txtNota3")

        self.btnRegistrarNota = QtWidgets.QPushButton(Form)
        self.btnRegistrarNota.setGeometry(QtCore.QRect(140, 200, 120, 28))
        self.btnRegistrarNota.setObjectName("btnRegistrarNota")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Notas"))
        self.btnRegistrarNota.setText(_translate("Form", "Registrar Nota"))
