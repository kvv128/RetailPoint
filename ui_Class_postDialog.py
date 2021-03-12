from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import ui_postDialog
import DB_App

class PostDialog(QtWidgets.QDialog, ui_postDialog.Ui_postDialog):
    def __init__(self, open_form, data_id: str = None):
        super().__init__()
        self.setupUi(self)

        self.edit_mode = False

        if data_id is not None:
            self.data_id = data_id
            self.edit_mode = True

            db_post = DB_App.Post.get(DB_App.Post.post_id == data_id)
            self.txt_postName.setText(db_post.post_name)

        self.buttonBox.accepted.connect(self.btn_Ok_clicked)
        # self.buttonBox.rejected.connect(self.btn_Cancel_clicked)


    def btn_Ok_clicked(self):
        # Проверяем есть ли в бд такая должность
        db_data = DB_App.Post.select().where(DB_App.Post.post_name == self.txt_postName.text())
        if len(db_data) != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Добавление записи")
            msg.setText(f"Должность '{self.txt_postName.text()}' уже существует!")
            msg.exec_()
            return

        if self.edit_mode:
            query = DB_App.Post.update(post_name = self.txt_postName.text()).where(DB_App.Post.post_id == self.data_id)
            query.execute()
        else:
                DB_App.Post.create(post_name=self.txt_postName.text())

        super().accept()

