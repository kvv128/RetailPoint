# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dictForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_DictForm(object):
    def setupUi(self, DictForm):
        DictForm.setObjectName("DictForm")
        DictForm.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(DictForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(11, 0, 11, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_toMainForm = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_toMainForm.setFont(font)
        self.btn_toMainForm.setObjectName("btn_toMainForm")
        self.gridLayout.addWidget(self.btn_toMainForm, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.lbl_selectDictName = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_selectDictName.setFont(font)
        self.lbl_selectDictName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_selectDictName.setObjectName("lbl_selectDictName")
        self.gridLayout.addWidget(self.lbl_selectDictName, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txt_dictFind = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_dictFind.setFont(font)
        self.txt_dictFind.setObjectName("txt_dictFind")
        self.verticalLayout_4.addWidget(self.txt_dictFind)
        self.tbl_dictList = QtWidgets.QTableWidget(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tbl_dictList.setFont(font)
        self.tbl_dictList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_dictList.setObjectName("tbl_dictList")
        self.tbl_dictList.setColumnCount(0)
        self.tbl_dictList.setRowCount(0)
        self.tbl_dictList.horizontalHeader().setVisible(False)
        self.tbl_dictList.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tbl_dictList)
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_data = QtWidgets.QTableWidget(self.frame_13)
        self.tbl_data.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tbl_data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_data.setObjectName("tbl_data")
        self.tbl_data.setColumnCount(0)
        self.tbl_data.setRowCount(0)
        self.tbl_data.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tbl_data)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.frame)
        DictForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(DictForm)
        QtCore.QMetaObject.connectSlotsByName(DictForm)

    def retranslateUi(self, DictForm):
        _translate = QtCore.QCoreApplication.translate
        DictForm.setWindowTitle(_translate("DictForm", "Справочники"))
        self.btn_toMainForm.setText(_translate("DictForm", "< НА ГЛАВНУЮ"))
        self.lbl_selectDictName.setText(_translate("DictForm", "СПРАВОЧНИК НЕ ВЫБРАН..."))
