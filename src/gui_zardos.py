# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zardos.ui'
#
# Created: Sat Apr 27 09:21:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(381, 270)
        MainWindow.setWindowTitle(_fromUtf8("Zardos"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.inputLine = QtGui.QLineEdit(self.centralwidget)
        self.inputLine.setFocusPolicy(QtCore.Qt.TabFocus)
        self.inputLine.setObjectName(_fromUtf8("inputLine"))
        self.gridLayout_3.addWidget(self.inputLine, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOk = QtGui.QPushButton(self.centralwidget)
        self.btnOk.setEnabled(False)
        self.btnOk.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnOk.setCheckable(False)
        self.btnOk.setChecked(False)
        self.btnOk.setAutoDefault(False)
        self.btnOk.setDefault(True)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnSkip = QtGui.QPushButton(self.centralwidget)
        self.btnSkip.setEnabled(False)
        self.btnSkip.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSkip.setDefault(False)
        self.btnSkip.setObjectName(_fromUtf8("btnSkip"))
        self.horizontalLayout.addWidget(self.btnSkip)
        self.btnEnterrupt = QtGui.QPushButton(self.centralwidget)
        self.btnEnterrupt.setEnabled(False)
        self.btnEnterrupt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnEnterrupt.setObjectName(_fromUtf8("btnEnterrupt"))
        self.horizontalLayout.addWidget(self.btnEnterrupt)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.translateLabel = QtGui.QLabel(self.centralwidget)
        self.translateLabel.setTextFormat(QtCore.Qt.RichText)
        self.translateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.translateLabel.setObjectName(_fromUtf8("translateLabel"))
        self.gridLayout.addWidget(self.translateLabel, 0, 0, 1, 1)
        self.answerLabel = QtGui.QLabel(self.centralwidget)
        self.answerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel.setObjectName(_fromUtf8("answerLabel"))
        self.gridLayout.addWidget(self.answerLabel, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.zopen = QtGui.QAction(MainWindow)
        self.zopen.setObjectName(_fromUtf8("zopen"))
        self.zclose = QtGui.QAction(MainWindow)
        self.zclose.setObjectName(_fromUtf8("zclose"))
        self.menu.addAction(self.zopen)
        self.menu.addAction(self.zclose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.btnOk.setText(QtGui.QApplication.translate("MainWindow", "ОК", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSkip.setText(QtGui.QApplication.translate("MainWindow", "Пропустить", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEnterrupt.setText(QtGui.QApplication.translate("MainWindow", "Прервать", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setToolTip(QtGui.QApplication.translate("MainWindow", "Введите перевод в форму ниже.", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setText(QtGui.QApplication.translate("MainWindow", "Переведите то, что здесь написано!", None, QtGui.QApplication.UnicodeUTF8))
        self.answerLabel.setText(QtGui.QApplication.translate("MainWindow", "Здесь будут отображаться правильные ответы.", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.zopen.setText(QtGui.QApplication.translate("MainWindow", "Открыть словарь", None, QtGui.QApplication.UnicodeUTF8))
        self.zopen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.zclose.setText(QtGui.QApplication.translate("MainWindow", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.zclose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))

