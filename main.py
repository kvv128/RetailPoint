# import peewee
import sys
from PyQt5 import QtWidgets
import DB_App

from ui_Class_mainForm import MainForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    from app_data import AppData,DBType
    AppData.app_name = "RetailPoint"
    AppData.app_version = "0.1"
    AppData.app_build_version = "20210311"
    DB_App.check_db_file()
    DB_App.save_start_param()

    # DB_App.test_def()

    mainForm = MainForm()
    mainForm.show()

app.exec()

