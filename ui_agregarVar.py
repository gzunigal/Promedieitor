# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarVar.ui'
#
# Created: Fri Aug  3 02:07:35 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AgregarVariable(object):
    def setupUi(self, AgregarVariable):
        AgregarVariable.setObjectName(_fromUtf8("AgregarVariable"))
        AgregarVariable.resize(295, 304)
        self.textEdit_4 = QtGui.QTextEdit(AgregarVariable)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(140, 130, 111, 51))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.buttonBox = QtGui.QDialogButtonBox(AgregarVariable)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.radioButton = QtGui.QRadioButton(AgregarVariable)
        self.radioButton.setGeometry(QtCore.QRect(20, 110, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(AgregarVariable)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 130, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(AgregarVariable)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(AgregarVariable)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 170, 82, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.label = QtGui.QLabel(AgregarVariable)
        self.label.setGeometry(QtCore.QRect(20, 90, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AgregarVariable)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(AgregarVariable)
        self.comboBox.setGeometry(QtCore.QRect(170, 60, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit = QtGui.QLineEdit(AgregarVariable)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QSpinBox(AgregarVariable)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(120, 220, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(AgregarVariable)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setGeometry(QtCore.QRect(30, 220, 62, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_3 = QtGui.QLabel(AgregarVariable)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AgregarVariable)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AgregarVariable)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(AgregarVariable)
        self.label_6.setGeometry(QtCore.QRect(170, 40, 31, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(AgregarVariable)
        QtCore.QMetaObject.connectSlotsByName(AgregarVariable)

    def retranslateUi(self, AgregarVariable):
        AgregarVariable.setWindowTitle(QtGui.QApplication.translate("AgregarVariable", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("AgregarVariable", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("AgregarVariable", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("AgregarVariable", "Condicion", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("AgregarVariable", "Promedio", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgregarVariable", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AgregarVariable", "Nueva Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AgregarVariable", "Ponderacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AgregarVariable", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AgregarVariable", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AgregarVariable", "Padre", None, QtGui.QApplication.UnicodeUTF8))
