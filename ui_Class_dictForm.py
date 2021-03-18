from enum import Enum

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QTableWidgetItem, QMenu, QMessageBox, QDialog
from peewee import JOIN

import ui_dictForm
from ui_Class_postDialog import PostDialog
from ui_Class_userDialog import UserDialog

import DB_App


class DictionaryName(Enum):
    NoSelect = 0
    User = "Сотрудники"
    Post = "Должности"
    Location = "Склады"
    Сounterparty = "Контрагенты"
    Product = "Товар"
    ProductGroup = "Группа товара"
    ProductType = "Вид товара"
    AppData = "Параметры приложения"


class DictForm(QtWidgets.QMainWindow, ui_dictForm.Ui_DictForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_record_id = ""
        self.current_row_index = ""
        self.current_dict = DictionaryName.NoSelect
        self.tbl_dictList.clicked.connect(self.tbl_dictList_clicked)

        self.btn_toMainForm.clicked.connect(self.btn_toMainForm_clicked)

        # context menu
        self.context_menu = QMenu(self)
        self.add_action = self.context_menu.addAction("Добавить")
        self.edit_action = self.context_menu.addAction("Редактировать")
        self.dell_action = self.context_menu.addAction("Удалить")
        self.tbl_data.customContextMenuRequested.connect(self.table_contex_menu_action)

        # Обрабатываем события
        self.tbl_data.itemSelectionChanged.connect(self.set_current_row_param)


        # Подготовка и вывод списка справочника
        self.dict_list_model = QtGui.QStandardItemModel()
        self.txt_dictFind.textChanged.connect(self.txt_dictFind_textChange)
        self.update_dict_list()

    def txt_dictFind_textChange(self, text):
        if len(text) == 0:
            self.tbl_dictList.setModel(self.dict_list_model)
            return

        filter_model = QSortFilterProxyModel()
        filter_model.setSourceModel(self.dict_list_model)
        filter_model.setFilterKeyColumn(0)

        regex = "^{}".format(text)
        filter_model.setFilterRegExp(QtCore.QRegExp(regex, QtCore.Qt.CaseInsensitive))

        self.tbl_dictList.setModel(filter_model)
        pass

    def set_current_row_param(self):
        """Устанавливает current_row_index и current_record_id"""
        sel_model = self.tbl_data.selectionModel()
        self.current_row_index = sel_model.currentIndex().row()
        self.current_record_id = sel_model.model().index(self.current_row_index, 0).data()

    def tbl_dictList_clicked(self):
        self.tbl_data.clear()
        self.current_record_id = None

        for curr_dict in DictionaryName:
            if curr_dict.value == self.tbl_dictList.selectionModel().:
                self.current_dict = curr_dict
                break

        self.lbl_selectDictName.setText(self.current_dict.value)

        # Обновляем поля
        self.tbl_data.setColumnCount(0)
        self.tbl_data.setRowCount(0)

        if self.current_dict == DictionaryName.AppData:
            self.tbl_data.setColumnCount(3)
            self.tbl_data.setHorizontalHeaderLabels([DB_App.ParamData.param_id.verbose_name,
                                                     DB_App.ParamData.param_name.verbose_name,
                                                     DB_App.ParamData.param_value.verbose_name])
            self.tbl_data.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        if self.current_dict == DictionaryName.Post:
            self.tbl_data.setColumnCount(2)
            self.tbl_data.setHorizontalHeaderLabels([DB_App.Post.post_id.verbose_name,
                                                     DB_App.Post.post_name.verbose_name])
            self.tbl_data.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        if self.current_dict == DictionaryName.User:
            self.tbl_data.setColumnCount(4)
            self.tbl_data.setHorizontalHeaderLabels([DB_App.User.user_id.verbose_name,
                                                     DB_App.User.id_user_post.verbose_name,
                                                     DB_App.User.user_login.verbose_name,
                                                     DB_App.User.user_name.verbose_name])
            self.tbl_data.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


        self.tbl_data.setColumnHidden(0, True)
        self.update_table_data()

    def update_table_context_menu(self):
        if self.current_dict == DictionaryName.AppData:
            self.add_action.setVisible(False)
            self.edit_action.setVisible(False)
            self.dell_action.setVisible(False)
        elif self.current_record_id is None or len(self.current_record_id) == 0:
            self.add_action.setVisible(True)
            self.edit_action.setVisible(False)
            self.dell_action.setVisible(False)
        else:
            self.add_action.setVisible(True)
            self.edit_action.setVisible(True)
            self.dell_action.setVisible(True)


    def table_contex_menu_action(self, position):
        if self.current_dict == DictionaryName.NoSelect:
            return

        self.update_table_context_menu()

        action = self.context_menu.exec_(self.tbl_data.mapToGlobal(position))

        # Обработка событий ContextMenu
        dialog_result = None

        if action == self.add_action:
            if self.current_dict == DictionaryName.Post:
                post_dialog = PostDialog(self)
                dialog_result = post_dialog.exec_()

                if dialog_result == QDialog.Accepted:
                    self.update_table_data()

            if self.current_dict == DictionaryName.User:
                user_dialog = UserDialog(self)
                dialog_result = user_dialog.exec_()
                if dialog_result == QDialog.Accepted:
                    self.update_table_data()
        #-------------------------------------------
        if action == self.edit_action:
            if self.current_dict == DictionaryName.Post:
                post_dialog = PostDialog(self, self.current_record_id)
                dialog_result = post_dialog.exec_()

            if self.current_dict == DictionaryName.User:
                user_dialog = UserDialog(self, self.current_record_id)
                dialog_result = user_dialog.exec_()


            if dialog_result == QDialog.Accepted:
                self.update_current_row()
        # -------------------------------------------
        if action == self.dell_action:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Удаление записи")
            msg.setText("Удалить текущую запись?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg_answer = msg.exec_()
            if msg_answer == QMessageBox.Ok:

                if self.current_dict == DictionaryName.Post:
                    DB_App.Post.delete_by_id(self.current_record_id)

                if self.current_dict == DictionaryName.User:
                    DB_App.User.delete_by_id(self.current_record_id)

                self.tbl_data.removeRow(self.tbl_data.currentRow())

    def table_column_stretch_reset(self):

        if self.dataTable.columnCount() == 0:
            return

        # обнуляем stretching колонок
        row_num = self.dataTable.columnCount()
        i = 0
        while i < row_num:
            self.dataTable.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            i += 1

    def update_dict_list(self):
        self.dict_list_model.setColumnCount(1)

        row_num = 0
        for dict_name in DictionaryName:
            if dict_name == DictionaryName.NoSelect:
                continue
            itm_dict = QStandardItem(dict_name.value)
            self.dict_list_model.setItem(row_num, 0, itm_dict)
            row_num += 1

        self.tbl_dictList.setModel(self.dict_list_model)

        # self.tbl_dictList.setColumnCount(1)
        # self.tbl_dictList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #
        # self.tbl_dictList.setRowCount(len(DictionaryName) - 1)
        #
        # row_num = 0
        # for dict_name in DictionaryName:
        #     if dict_name == DictionaryName.NoSelect:
        #         continue
        #     self.tbl_dictList.setItem(0, row_num, QTableWidgetItem(dict_name.value))
        #     row_num += 1

    def update_table_data(self):
        row_num = 0

        if self.current_dict == DictionaryName.AppData:
            for db_data in DB_App.ParamData.select():
                self.tbl_data.setRowCount(row_num+1)
                self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.param_id)))
                self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.param_name)))
                self.tbl_data.setItem(row_num, 2, QTableWidgetItem(str(db_data.param_value)))
                row_num += 1

        if self.current_dict == DictionaryName.Post:
            for db_data in DB_App.Post.select():
                self.tbl_data.setRowCount(row_num+1)
                self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.post_id)))
                self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.post_name)))
                row_num += 1

        if self.current_dict == DictionaryName.User:
            MA = DB_App.Post.alias()
            query = (DB_App.User.select(DB_App.User.user_id,
                                        DB_App.User.user_login,
                                        DB_App.User.user_name,
                                        MA.post_name)
                     .join(MA, DB_App.JOIN.LEFT_OUTER, on=(DB_App.User.id_user_post == MA.post_id)))
            # print("print data...\n", query)
            # for row in query:
            #     print(row.user_fio, row.id_user_post, row.post.post_name)
            for db_data in query:
                self.tbl_data.setRowCount(row_num+1)
                self.tbl_data.setItem(row_num, 0, QTableWidgetItem(str(db_data.user_id)))
                self.tbl_data.setItem(row_num, 1, QTableWidgetItem(str(db_data.post.post_name)))
                self.tbl_data.setItem(row_num, 2, QTableWidgetItem(str(db_data.user_login)))
                self.tbl_data.setItem(row_num, 3, QTableWidgetItem(str(db_data.user_name)))
                row_num += 1

    def update_current_row(self):
        if self.current_dict == DictionaryName.Post:
            db_data = DB_App.Post.get(DB_App.Post.post_id == self.current_record_id)
            self.tbl_data.setItem(self.current_row_index, 1, QTableWidgetItem(db_data.post_name))

        if self.current_dict == DictionaryName.User:
            PA = DB_App.Post.alias()
            query = (DB_App.User.select(DB_App.User.user_name,
                                        DB_App.User.user_login,
                                        DB_App.User.id_user_post,
                                        PA.post_name).where(DB_App.User.user_id == self.current_record_id)
                     .join(PA, JOIN.LEFT_OUTER, on=(DB_App.User.id_user_post == PA.post_id)))
            for row in query:
                self.tbl_data.setItem(self.current_row_index, 1, QTableWidgetItem(row.post.post_name))
                self.tbl_data.setItem(self.current_row_index, 2, QTableWidgetItem(row.user_login))
                self.tbl_data.setItem(self.current_row_index, 3, QTableWidgetItem(row.user_name))

    def btn_toMainForm_clicked(self):
        self.close()