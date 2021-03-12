from  PyQt5 import QtWidgets
import ui_mainForm
from ui_Class_loginForm import LoginForm
from ui_Class_dictForm import DictForm


class MainForm(QtWidgets.QMainWindow, ui_mainForm.Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_userChange.clicked.connect(self.btn_userChange_clicked)
        self.btn_dict.clicked.connect(self.btn_dict_clicked)

        self.form_ini()

    def btn_dict_clicked(self):
        self.dictForm = DictForm()
        self.dictForm.show()
        pass

    def btn_userChange_clicked(self):
        self.loginForm = LoginForm(self)
        self.loginForm.frame_FullName.setVisible(False)
        self.loginForm.show()

    def form_ini(self):
        self.dataTable.setColumnHidden(0, True)
        self.dataTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        import app_data
        self.setWindowTitle(f"{app_data.AppData.app_name} {app_data.AppData.get_app_version()}")