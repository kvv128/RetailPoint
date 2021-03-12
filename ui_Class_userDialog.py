from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog
from peewee import JOIN

from DB_App import User
from ui_Class_selectDialog import SelectDialog, DictionaryName

import ui_userDialog
import DB_App

class UserDialog(QtWidgets.QDialog, ui_userDialog.Ui_userDialog):
    def __init__(self, open_form, data_id: str = None):
        super().__init__()
        self.setupUi(self)

        self.edit_mode = False
        self.post_id = ""

        if data_id is not None:
            self.data_id = data_id
            self.edit_mode = True
            UA = DB_App.User.alias()
            query = (User.select(User.user_fio, User.id_user_post, UA.post_name)
                     .join(UA, JOIN.LEFT_OUTER, on=(User.id_user_post == UA.post_id)))
            # print("print data...\n", query)
            for row in query:
                print(row.user_fio, row.id_user_post, row.post.post_name)


            db_user = DB_App.User.get(DB_App.User.user_id == data_id)
            self.txt_userName.setText(db_user.user_name)

        self.buttonBox.accepted.connect(self.btn_Ok_clicked)
        # self.buttonBox.rejected.connect(self.btn_Cancel_clicked)
        self.pBtn_Post.clicked.connect(self.pBtn_Post_clicked)

    def pBtn_Post_clicked(self):
        select_dialog = SelectDialog(self, DictionaryName.Post)
        dialog_result = select_dialog.exec_()
        if dialog_result == QDialog.Accepted:
            # sel_model = select_dialog.tbl_data.selectionModel()
            self.pBtn_Post.setText(select_dialog.select_post_name)
            self.post_id = select_dialog.select_post_id

    def btn_Ok_clicked(self):
        # Проверяем форму назаполнение
        if len(self.txt_userName.text()) == 0 or len(self.txt_Login.text()) == 0 or len(self.txt_Password.text()) == 0 or len(self.pBtn_Post.text()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Добавление записи")
            msg.setText(f"Необходимо заполнить все поля!")
            msg.exec_()
            return

        # Проверяем есть ли в бд такой пользователь
        db_data_name = DB_App.User.select().where(User.user_name == self.txt_userName.text())
        if len(db_data_name) != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Добавление записи")
            msg.setText(f"Пользователь с ФИО '{self.txt_postName.text()}' уже существует!")
            msg.exec_()
            return

        db_data_login = DB_App.User.select().where(User.user_login == self.txt_Login.text())
        if len(db_data_login) != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Добавление записи")
            msg.setText(f"Пользователь с логином '{self.txt_postName.text()}' уже существует!")
            msg.exec_()
            return

        if self.edit_mode:
            pass
            # query = DB_App.Post.update(post_name = self.txt_postName.text()).where(DB_App.Post.post_id == self.data_id)
            # query.execute()
        else:
            if len(self.post_id) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Добавление записи")
                msg.setText(f"Необходимо выбрать должность!")
                msg.exec_()
                return
            else:
                DB_App.User.create(user_login =self.txt_Login.text(),
                                   user_psswd = self.txt_Password.text(),
                                   user_name = self.txt_userName.text(),
                                   id_user_post = self.post_id)

        super().accept()

