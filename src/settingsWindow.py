# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sun Apr 28 21:18:05 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName(_fromUtf8("settings"))
        settings.resize(400, 300)
        self.translation = QtGui.QWidget()
        self.translation.setObjectName(_fromUtf8("translation"))
        self.widget = QtGui.QWidget(self.translation)
        self.widget.setGeometry(QtCore.QRect(30, 20, 331, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.multipleTranslationButton = QtGui.QPushButton(self.widget)
        self.multipleTranslationButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.multipleTranslationButton.setObjectName(_fromUtf8("multipleTranslationButton"))
        self.horizontalLayout.addWidget(self.multipleTranslationButton)
        settings.addTab(self.translation, _fromUtf8(""))
        self.text = QtGui.QWidget()
        self.text.setObjectName(_fromUtf8("text"))
        settings.addTab(self.text, _fromUtf8(""))

        self.retranslateUi(settings)
        settings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "Настройки", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settings", "Режим перевода:", None, QtGui.QApplication.UnicodeUTF8))
        self.multipleTranslationButton.setText(QtGui.QApplication.translate("settings", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        settings.setTabText(settings.indexOf(self.translation), QtGui.QApplication.translate("settings", "Перевод", None, QtGui.QApplication.UnicodeUTF8))
        settings.setTabText(settings.indexOf(self.text), QtGui.QApplication.translate("settings", "Текст", None, QtGui.QApplication.UnicodeUTF8))

