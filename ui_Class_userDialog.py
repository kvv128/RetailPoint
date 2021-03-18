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
        self.post_id = data_id

        if data_id is not None:
            self.data_id = data_id
            self.edit_mode = True
            PA = DB_App.Post.alias()
            query = (User.select(User.user_name, User.user_login, User.id_user_post, PA.post_name).where(User.user_id == data_id)
                     .join(PA, JOIN.LEFT_OUTER, on=(User.id_user_post == PA.post_id)))
            for row in query:
                self.txt_userName.setText(row.user_name)
                self.pBtn_Post.setText(row.post.post_name)
                self.txt_Login.setText(row.user_login)
            self.txt_Password.setText("++++++++")


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

        if self.edit_mode:
            query = DB_App.User.update(user_name = self.txt_userName.text(),
                                       user_login = self.txt_Login.text(),
                                       id_user_post = self.post_id).where(DB_App.User.user_id == self.data_id)
            query.execute()

            if self.txt_Password.text() != "++++++++":
                query = DB_App.User.update(user_psswd=self.txt_Password.text()).where(DB_App.User.user_id == self.data_id)
                query.execute()
        else:
            # Проверяем есть ли в бд такой пользователь
            db_data_name = DB_App.User.select().where(User.user_name == self.txt_userName.text())
            if len(db_data_name) != 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Добавление записи")
                msg.setText(f"Пользователь с ФИО '{self.txt_postName.text()}' уже существует!")
                msg.exec_()
                return

            # Проверяем есть ли в бд такой логин
            db_data_login = DB_App.User.select().where(User.user_login == self.txt_Login.text())
            if len(db_data_login) != 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Добавление записи")
                msg.setText(f"Пользователь с логином '{self.txt_postName.text()}' уже существует!")
                msg.exec_()
                return

            DB_App.User.create(user_login=self.txt_Login.text(),
                               user_psswd=self.txt_Password.text(),
                               user_name=self.txt_userName.text(),
                               id_user_post=self.post_id)

        super().accept()

