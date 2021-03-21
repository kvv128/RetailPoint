from enum import Enum

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView

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
    def __init__(self, open_form, dict_name: DictionaryName, filter_name=""):
        super().__init__()
        self.setupUi(self)

        self.current_dict = dict_name

        self.tbl_data.cellDoubleClicked.connect(self.tbl_data_cellDoubleClicked)
        self.txt_filter.textChanged.connect(self.txt_filter_textChange)

        self.update_table_column()

    def txt_filter_textChange(self, text):
        if len(text) == 0:
            self.tbl_data.setModel(self.model)
            return
        self.update_table_data()

    def tbl_data_cellDoubleClicked(self):
        sel_model = self.tbl_data.selectionModel()
        current_row_index = sel_model.currentIndex().row()
        self.select_post_id = sel_model.model().index(current_row_index, 0).data()
        self.select_post_name = sel_model.model().index(current_row_index, 1).data()
        super().accept()

    def update_table_column(self):
        self.tbl_data.setColumnCount(2)
        self.tbl_data.setHorizontalHeaderLabels([DB_App.Post.post_id.verbose_name,
                                                 DB_App.Post.post_name.verbose_name])
        self.tbl_data.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.tbl_data.setColumnHidden(0, True)
        self.update_table_data()

    def update_table_data(self, filter_string = ""):
        row_num = 0
        selected_data = None

        if self.current_dict == DictionaryName.Post:
            if len(filter_string) == 0:
                selected_data = DB_App.Post.select()
            else:
                selected_data = DB_App.Post.select().where(DB_App.Post.post_name == f"%{filter_string}%")

            for db_data in DB_App.Post.select():
                self.tbl_data.setRowCount(row_num+1)
                self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.post_id)))
                self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.post_name)))
                row_num += 1

    # def update_data_table(self):
    #     row_num = 0
    #
    #     if self.current_dict == DictionaryName.Post:
    #         for db_data in DB_App.Post.select():
    #             itm_id = QStandardItem(str(db_data.post_id))
    #             itm_name = QStandardItem(str(db_data.post_name))
    #             # itm = QStandardItem(str(db_data.post_id), str(db_data.post_name))
    #             self.model.setItem(row_num, 0, itm_id)
    #             self.model.setItem(row_num, 1, itm_name)
    #             # self.model.insertRow(row_num, itm)
    #             # self.tbl_data.setRowCount(row_num+1)
    #             # self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.post_id)))
    #             # self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.post_name)))
    #             row_num += 1
    #
    #         self.tbl_data.setModel(self.model)
    #     # self.tbl_data.setColumnHidden(0, True)
    #     self.tbl_data.hideColumn(0)

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
