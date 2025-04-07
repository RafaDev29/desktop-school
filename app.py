import sys
from PyQt5.QtWidgets import QApplication
from src.controllers.login_controller import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginController()
    login.show()
    sys.exit(app.exec_())
