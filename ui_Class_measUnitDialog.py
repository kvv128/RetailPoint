from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import ui_measUnitDialog
import DB_App

class MeasUnitDialog(QtWidgets.QDialog, ui_measUnitDialog.Ui_measUnitDialog):
    def __init__(self, open_form, data_id: str = None):
        super().__init__()
        self.setupUi(self)

        self.edit_mode = False

        if data_id is not None:
            self.data_id = data_id
            self.edit_mode = True

            db_meas_unit = DB_App.MeasUnit.get(DB_App.MeasUnit.measunit_id == data_id)
            self.txt_measUnitName.setText(db_meas_unit.measunit_name)

        self.buttonBox.accepted.connect(self.btn_Ok_clicked)
        # self.buttonBox.rejected.connect(self.btn_Cancel_clicked)


    def btn_Ok_clicked(self):
        # Проверяем есть ли в бд такая должность
        db_data = DB_App.MeasUnit.select().where(DB_App.MeasUnit.measunit_name == self.txt_measUnitName.text())
        if len(db_data) != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Добавление записи")
            msg.setText(f"Единица измерения '{self.txt_measUnitName.text()}' уже существует!")
            msg.exec_()
            return

        if self.edit_mode:
            query = DB_App.MeasUnit.update(measunit_name = self.txt_measUnitName.text()).where(DB_App.MeasUnit.measunit_id == self.data_id)
            query.execute()
        else:
                DB_App.MeasUnit.create(measunit_name=self.txt_measUnitName.text())

        super().accept()

