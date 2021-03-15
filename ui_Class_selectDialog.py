from enum import Enum

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import ui_selectDialog
import DB_App

class DictionaryName(Enum):
    User = "Сотрудники"
    Post = "Должности"
    Location = "Склады"
    Сounterparty = "Контрагенты"
    Product = "Товар"
    ProductGroup = "Группа товара"
    ProductType = "Вид товара"


class SelectDialog(QtWidgets.QDialog, ui_selectDialog.Ui_selectDialog):
    def __init__(self, open_form, dict_name: DictionaryName, filter_name = ""):
        super().__init__()
        self.setupUi(self)

        self.current_dict = dict_name

        self.tbl_data.cellDoubleClicked.connect(self.tbl_data_cellDoubleClicked)

        self.update_table_column()

        # filter proxy model
        filter_proxy_model = QtGui.QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(self.tbl_data.model())
        filter_proxy_model.setFilterKeyColumn(2)  # third column

        # line edit for filtering
        self.txt_filter.textChanged.connect(filter_proxy_model.setFilterRegExp)

        # self.edit_mode = False

        # if data_id is not None:
        #     self.data_id = data_id
        #     self.edit_mode = True
        #
        #     db_post = DB_App.Post.get(DB_App.Post.post_id == data_id)
        #     self.txt_postName.setText(db_post.post_name)
        #
        # self.buttonBox.accepted.connect(self.btn_Ok_clicked)
        # self.buttonBox.rejected.connect(self.btn_Cancel_clicked)

    def tbl_data_cellDoubleClicked(self):
        sel_model = self.tbl_data.selectionModel()
        current_row_index = sel_model.currentIndex().row()
        self.select_post_id = sel_model.model().index(current_row_index, 0).data()
        self.select_post_name = sel_model.model().index(current_row_index, 1).data()
        super().accept()

    def update_table_column(self):
        if self.current_dict == DictionaryName.Post:
            self.tbl_data.setColumnCount(2)
            self.tbl_data.setHorizontalHeaderLabels([DB_App.Post.post_id.verbose_name,
                                                     DB_App.Post.post_name.verbose_name])
            self.tbl_data.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.tbl_data.setColumnHidden(0, True)
        self.update_data_table()

    def update_data_table(self):
        row_num = 0

        if self.current_dict == DictionaryName.Post:
            for db_data in DB_App.Post.select():
                self.tbl_data.setRowCount(row_num+1)
                self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.post_id)))
                self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.post_name)))
                row_num += 1


    # def btn_Ok_clicked(self):
    #     # Проверяем есть ли в бд такая должность
    #     db_data = DB_App.Post.select().where(DB_App.Post.post_name == self.txt_postName.text())
    #     if len(db_data) != 0:
    #         msg = QMessageBox()
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setWindowTitle("Добавление записи")
    #         msg.setText(f"Должность '{self.txt_postName.text()}' уже существует!")
    #         msg.exec_()
    #         return
    #
    #     if self.edit_mode:
    #         query = DB_App.Post.update(post_name = self.txt_postName.text()).where(DB_App.Post.post_id == self.data_id)
    #         query.execute()
    #     else:
    #             DB_App.Post.create(post_name=self.txt_postName.text())
    #
    #     super().accept()

