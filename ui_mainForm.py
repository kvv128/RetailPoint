# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(11, 1, 11, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setEnabled(True)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setContentsMargins(0, 3, -1, 15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_warehouse = QtWidgets.QPushButton(self.frame_10)
        self.btn_warehouse.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_warehouse.setFont(font)
        self.btn_warehouse.setObjectName("btn_warehouse")
        self.horizontalLayout_5.addWidget(self.btn_warehouse)
        self.btn_pricing = QtWidgets.QPushButton(self.frame_10)
        self.btn_pricing.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_pricing.setFont(font)
        self.btn_pricing.setObjectName("btn_pricing")
        self.horizontalLayout_5.addWidget(self.btn_pricing)
        self.btn_loyaltyProgram = QtWidgets.QPushButton(self.frame_10)
        self.btn_loyaltyProgram.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_loyaltyProgram.setFont(font)
        self.btn_loyaltyProgram.setObjectName("btn_loyaltyProgram")
        self.horizontalLayout_5.addWidget(self.btn_loyaltyProgram)
        self.btn_dict = QtWidgets.QPushButton(self.frame_10)
        self.btn_dict.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_dict.setFont(font)
        self.btn_dict.setObjectName("btn_dict")
        self.horizontalLayout_5.addWidget(self.btn_dict)
        self.btn_selling = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_selling.sizePolicy().hasHeightForWidth())
        self.btn_selling.setSizePolicy(sizePolicy)
        self.btn_selling.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_selling.setFont(font)
        self.btn_selling.setObjectName("btn_selling")
        self.horizontalLayout_5.addWidget(self.btn_selling)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_userName = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_userName.sizePolicy().hasHeightForWidth())
        self.lbl_userName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.lbl_userName.setFont(font)
        self.lbl_userName.setTabletTracking(False)
        self.lbl_userName.setAutoFillBackground(False)
        self.lbl_userName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_userName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_userName.setObjectName("lbl_userName")
        self.horizontalLayout_4.addWidget(self.lbl_userName)
        self.btn_userChange = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_userChange.sizePolicy().hasHeightForWidth())
        self.btn_userChange.setSizePolicy(sizePolicy)
        self.btn_userChange.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_userChange.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_userChange.setFont(font)
        self.btn_userChange.setObjectName("btn_userChange")
        self.horizontalLayout_4.addWidget(self.btn_userChange)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(3, 3, 11, 3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.txt_product = QtWidgets.QLineEdit(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_product.setFont(font)
        self.txt_product.setClearButtonEnabled(True)
        self.txt_product.setObjectName("txt_product")
        self.horizontalLayout_2.addWidget(self.txt_product)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_2)
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(8)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(7, item)
        self.dataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.dataTable.horizontalHeader().setSortIndicatorShown(False)
        self.dataTable.horizontalHeader().setStretchLastSection(False)
        self.dataTable.verticalHeader().setVisible(False)
        self.dataTable.verticalHeader().setSortIndicatorShown(False)
        self.dataTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.dataTable)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 3)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_chequeNew = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chequeNew.sizePolicy().hasHeightForWidth())
        self.btn_chequeNew.setSizePolicy(sizePolicy)
        self.btn_chequeNew.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_chequeNew.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_chequeNew.setFont(font)
        self.btn_chequeNew.setAutoDefault(False)
        self.btn_chequeNew.setDefault(False)
        self.btn_chequeNew.setFlat(False)
        self.btn_chequeNew.setObjectName("btn_chequeNew")
        self.horizontalLayout.addWidget(self.btn_chequeNew)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(11)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_goodsReturn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_goodsReturn.sizePolicy().hasHeightForWidth())
        self.btn_goodsReturn.setSizePolicy(sizePolicy)
        self.btn_goodsReturn.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_goodsReturn.setFont(font)
        self.btn_goodsReturn.setObjectName("btn_goodsReturn")
        self.gridLayout_2.addWidget(self.btn_goodsReturn, 0, 2, 1, 1)
        self.btn_chequeCopy = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chequeCopy.sizePolicy().hasHeightForWidth())
        self.btn_chequeCopy.setSizePolicy(sizePolicy)
        self.btn_chequeCopy.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_chequeCopy.setFont(font)
        self.btn_chequeCopy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_chequeCopy.setObjectName("btn_chequeCopy")
        self.gridLayout_2.addWidget(self.btn_chequeCopy, 1, 2, 1, 1)
        self.btn_client = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_client.sizePolicy().hasHeightForWidth())
        self.btn_client.setSizePolicy(sizePolicy)
        self.btn_client.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_client.setFont(font)
        self.btn_client.setObjectName("btn_client")
        self.gridLayout_2.addWidget(self.btn_client, 0, 3, 1, 1)
        self.btn_discount = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_discount.sizePolicy().hasHeightForWidth())
        self.btn_discount.setSizePolicy(sizePolicy)
        self.btn_discount.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_discount.setFont(font)
        self.btn_discount.setObjectName("btn_discount")
        self.gridLayout_2.addWidget(self.btn_discount, 1, 3, 1, 1)
        self.btn_shiftOpen = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_shiftOpen.sizePolicy().hasHeightForWidth())
        self.btn_shiftOpen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_shiftOpen.setFont(font)
        self.btn_shiftOpen.setObjectName("btn_shiftOpen")
        self.gridLayout_2.addWidget(self.btn_shiftOpen, 0, 1, 1, 1)
        self.btn_shiftClose = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_shiftClose.sizePolicy().hasHeightForWidth())
        self.btn_shiftClose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_shiftClose.setFont(font)
        self.btn_shiftClose.setObjectName("btn_shiftClose")
        self.gridLayout_2.addWidget(self.btn_shiftClose, 1, 1, 1, 1)
        self.btn_cashOrderExp = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cashOrderExp.sizePolicy().hasHeightForWidth())
        self.btn_cashOrderExp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_cashOrderExp.setFont(font)
        self.btn_cashOrderExp.setObjectName("btn_cashOrderExp")
        self.gridLayout_2.addWidget(self.btn_cashOrderExp, 1, 0, 1, 1)
        self.btn_cashOrderInc = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cashOrderInc.sizePolicy().hasHeightForWidth())
        self.btn_cashOrderInc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_cashOrderInc.setFont(font)
        self.btn_cashOrderInc.setObjectName("btn_cashOrderInc")
        self.gridLayout_2.addWidget(self.btn_cashOrderInc, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.btn_payment = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_payment.sizePolicy().hasHeightForWidth())
        self.btn_payment.setSizePolicy(sizePolicy)
        self.btn_payment.setMinimumSize(QtCore.QSize(130, 70))
        self.btn_payment.setMaximumSize(QtCore.QSize(130, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_payment.setFont(font)
        self.btn_payment.setObjectName("btn_payment")
        self.horizontalLayout.addWidget(self.btn_payment)
        self.frame_discount = QtWidgets.QFrame(self.frame)
        self.frame_discount.setEnabled(True)
        self.frame_discount.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_discount.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_discount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_discount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_discount.setObjectName("frame_discount")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_discount)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_discount)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lbl_checkDiscount = QtWidgets.QLabel(self.frame_discount)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_checkDiscount.sizePolicy().hasHeightForWidth())
        self.lbl_checkDiscount.setSizePolicy(sizePolicy)
        self.lbl_checkDiscount.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_checkDiscount.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_checkDiscount.setFont(font)
        self.lbl_checkDiscount.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_checkDiscount.setObjectName("lbl_checkDiscount")
        self.verticalLayout_6.addWidget(self.lbl_checkDiscount)
        self.horizontalLayout.addWidget(self.frame_discount)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lbl_checkSumm = QtWidgets.QLabel(self.frame_4)
        self.lbl_checkSumm.setMinimumSize(QtCore.QSize(160, 0))
        self.lbl_checkSumm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lbl_checkSumm.setFont(font)
        self.lbl_checkSumm.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_checkSumm.setObjectName("lbl_checkSumm")
        self.verticalLayout_2.addWidget(self.lbl_checkSumm)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "MainWindow"))
        self.btn_warehouse.setText(_translate("MainForm", "??????????"))
        self.btn_pricing.setText(_translate("MainForm", "??????????????????????????????"))
        self.btn_loyaltyProgram.setText(_translate("MainForm", "?????????????????? ????????????????????"))
        self.btn_dict.setText(_translate("MainForm", "??????????????????????"))
        self.btn_selling.setText(_translate("MainForm", "??????????????"))
        self.lbl_userName.setText(_translate("MainForm", "??????????????????: \n"
"??????"))
        self.btn_userChange.setText(_translate("MainForm", "?????????? ????????????????????????"))
        self.label.setText(_translate("MainForm", "??????????:"))
        self.txt_product.setPlaceholderText(_translate("MainForm", "???????????????????????? ???????????? / ??????????-?????? / ?????? ????????????"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "id"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "???"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainForm", "??????????"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("MainForm", "??????-????"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("MainForm", "????????"))
        item = self.dataTable.horizontalHeaderItem(5)
        item.setText(_translate("MainForm", "????????????"))
        item = self.dataTable.horizontalHeaderItem(6)
        item.setText(_translate("MainForm", "??????????"))
        item = self.dataTable.horizontalHeaderItem(7)
        item.setText(_translate("MainForm", "??????????????"))
        self.btn_chequeNew.setText(_translate("MainForm", "??????????\n"
"??????"))
        self.btn_goodsReturn.setText(_translate("MainForm", "??????????????"))
        self.btn_chequeCopy.setText(_translate("MainForm", "?????????? ????????"))
        self.btn_client.setText(_translate("MainForm", "????????????"))
        self.btn_discount.setText(_translate("MainForm", "????????????"))
        self.btn_shiftOpen.setText(_translate("MainForm", "?????????????? ??????????"))
        self.btn_shiftClose.setText(_translate("MainForm", "?????????????? ??????????"))
        self.btn_cashOrderExp.setText(_translate("MainForm", "??????"))
        self.btn_cashOrderInc.setText(_translate("MainForm", "??????"))
        self.btn_payment.setText(_translate("MainForm", "????????????"))
        self.label_5.setText(_translate("MainForm", "????????????"))
        self.lbl_checkDiscount.setText(_translate("MainForm", "0.00"))
        self.label_4.setText(_translate("MainForm", "??????????"))
        self.lbl_checkSumm.setText(_translate("MainForm", "0.00"))
