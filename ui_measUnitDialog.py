# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_measUnitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_measUnitDialog(object):
    def setupUi(self, measUnitDialog):
        measUnitDialog.setObjectName("measUnitDialog")
        measUnitDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        measUnitDialog.resize(400, 150)
        measUnitDialog.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(measUnitDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_FullName = QtWidgets.QFrame(measUnitDialog)
        self.frame_FullName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_FullName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_FullName.setObjectName("frame_FullName")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_FullName)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_FullName)
        self.label_3.setMinimumSize(QtCore.QSize(86, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txt_measUnitName = QtWidgets.QLineEdit(self.frame_FullName)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_measUnitName.setFont(font)
        self.txt_measUnitName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_measUnitName.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_measUnitName.setPlaceholderText("")
        self.txt_measUnitName.setClearButtonEnabled(True)
        self.txt_measUnitName.setObjectName("txt_measUnitName")
        self.verticalLayout.addWidget(self.txt_measUnitName)
        self.verticalLayout_2.addWidget(self.frame_FullName)
        self.buttonBox = QtWidgets.QDialogButtonBox(measUnitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(measUnitDialog)
        self.buttonBox.rejected.connect(measUnitDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(measUnitDialog)

    def retranslateUi(self, measUnitDialog):
        _translate = QtCore.QCoreApplication.translate
        measUnitDialog.setWindowTitle(_translate("measUnitDialog", "Единица измерения"))
        self.label_3.setText(_translate("measUnitDialog", "Единица измерения"))
