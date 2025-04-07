from PyQt5.QtWidgets import QMainWindow, QMessageBox
from src.windows.login_window import Ui_Form
from src.controllers.menu_controller import MenuController

class LoginController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.ui.txtUsuario.text()
        contrasena = self.ui.txtContrasena.text()

        if usuario == "admin" and contrasena == "123":
            self.menu = MenuController()
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña inválidos")
