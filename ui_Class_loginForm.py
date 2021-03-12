from PyQt5 import QtWidgets
import ui_loginForm


class LoginForm(QtWidgets.QMainWindow, ui_loginForm.Ui_LoginForm):
    def __init__(self, login_form):
        super().__init__()
        self.setupUi(self)

        self.btn_Cancel.clicked.connect(self.btn_Cancel_clicked)
        self.txt_psswd.returnPressed.connect(self.txt_psswd_returnPressed)

    def txt_psswd_returnPressed(self):
        self.close()

    def btn_Cancel_clicked(self):
        self.close()