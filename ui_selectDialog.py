# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectDialog(object):
    def setupUi(self, selectDialog):
        selectDialog.setObjectName("selectDialog")
        selectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        selectDialog.resize(491, 269)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        selectDialog.setFont(font)
        selectDialog.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(selectDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_filter = QtWidgets.QLineEdit(selectDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.txt_filter.setFont(font)
        self.txt_filter.setText("")
        self.txt_filter.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_filter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_filter.setPlaceholderText("")
        self.txt_filter.setClearButtonEnabled(True)
        self.txt_filter.setObjectName("txt_filter")
        self.verticalLayout_2.addWidget(self.txt_filter)
        self.tbl_data = QtWidgets.QTableWidget(selectDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tbl_data.setFont(font)
        self.tbl_data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_data.setObjectName("tbl_data")
        self.tbl_data.setColumnCount(0)
        self.tbl_data.setRowCount(0)
        self.tbl_data.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tbl_data)
        self.buttonBox = QtWidgets.QDialogButtonBox(selectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(selectDialog)
        self.buttonBox.rejected.connect(selectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(selectDialog)

    def retranslateUi(self, selectDialog):
        _translate = QtCore.QCoreApplication.translate
        selectDialog.setWindowTitle(_translate("selectDialog", "Карточка пользователя"))