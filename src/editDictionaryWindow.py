# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editDictionaryWindow.ui'
#
# Created: Thu Jul 18 17:09:06 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editDictionaryWindow(object):
    def setupUi(self, editDictionaryWindow):
        editDictionaryWindow.setObjectName(_fromUtf8("editDictionaryWindow"))
        editDictionaryWindow.resize(489, 484)
        self.buttonBox = QtGui.QDialogButtonBox(editDictionaryWindow)
        self.buttonBox.setGeometry(QtCore.QRect(110, 430, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.searchLine = QtGui.QLineEdit(editDictionaryWindow)
        self.searchLine.setGeometry(QtCore.QRect(40, 40, 331, 31))
        self.searchLine.setObjectName(_fromUtf8("searchLine"))
        self.tableWidget = QtGui.QTableWidget(editDictionaryWindow)
        self.tableWidget.setGeometry(QtCore.QRect(40, 90, 411, 321))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(editDictionaryWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editDictionaryWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editDictionaryWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(editDictionaryWindow)

    def retranslateUi(self, editDictionaryWindow):
        editDictionaryWindow.setWindowTitle(QtGui.QApplication.translate("editDictionaryWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLine.setText(QtGui.QApplication.translate("editDictionaryWindow", "Поиск слов...", None, QtGui.QApplication.UnicodeUTF8))

