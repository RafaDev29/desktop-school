from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 200)
        self.txtUsuario = QtWidgets.QLineEdit(Form)
        self.txtUsuario.setGeometry(QtCore.QRect(90, 30, 151, 22))
        self.txtUsuario.setPlaceholderText("Usuario")
        self.txtUsuario.setObjectName("txtUsuario")

        self.txtContrasena = QtWidgets.QLineEdit(Form)
        self.txtContrasena.setGeometry(QtCore.QRect(90, 70, 151, 22))
        self.txtContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtContrasena.setPlaceholderText("Contraseña")
        self.txtContrasena.setObjectName("txtContrasena")

        self.btnLogin = QtWidgets.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(110, 110, 93, 28))
        self.btnLogin.setObjectName("btnLogin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.btnLogin.setText(_translate("Form", "Iniciar sesión"))