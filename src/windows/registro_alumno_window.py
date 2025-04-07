from PyQt5 import QtCore, QtWidgets

class Ui_RegistroAlumno(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 200)

        self.txtDNI = QtWidgets.QLineEdit(Form)
        self.txtDNI.setGeometry(QtCore.QRect(100, 30, 200, 22))
        self.txtDNI.setPlaceholderText("DNI")
        self.txtDNI.setObjectName("txtDNI")

        self.txtNombre = QtWidgets.QLineEdit(Form)
        self.txtNombre.setGeometry(QtCore.QRect(100, 70, 200, 22))
        self.txtNombre.setPlaceholderText("Apellidos y Nombres")
        self.txtNombre.setObjectName("txtNombre")

        self.btnRegistrar = QtWidgets.QPushButton(Form)
        self.btnRegistrar.setGeometry(QtCore.QRect(150, 110, 100, 28))
        self.btnRegistrar.setObjectName("btnRegistrar")

        self.btnVerTodos = QtWidgets.QPushButton(Form)
        self.btnVerTodos.setGeometry(QtCore.QRect(260, 110, 100, 28))
        self.btnVerTodos.setObjectName("btnVerTodos")

        
        self.tableAlumnos = QtWidgets.QTableWidget(Form)
        self.tableAlumnos.setGeometry(QtCore.QRect(20, 150, 360, 120))
        self.tableAlumnos.setObjectName("tableAlumnos")
        self.tableAlumnos.setColumnCount(2)
        self.tableAlumnos.setHorizontalHeaderLabels(["DNI", "Nombre"])
        self.tableAlumnos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAlumnos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
       


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Alumnos"))
        self.btnRegistrar.setText(_translate("Form", "Registrar"))
        self.btnVerTodos.setText(_translate("Form", "Ver todos"))