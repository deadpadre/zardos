# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsNew.ui'
#
# Created: Thu May  2 01:15:13 2013
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
        settings.resize(389, 352)
        self.translation = QtGui.QWidget()
        self.translation.setObjectName(_fromUtf8("translation"))
        self.usualButtonBox = QtGui.QDialogButtonBox(self.translation)
        self.usualButtonBox.setGeometry(QtCore.QRect(0, 280, 381, 27))
        self.usualButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.usualButtonBox.setCenterButtons(False)
        self.usualButtonBox.setObjectName(_fromUtf8("usualButtonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.translation)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 351, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.modeTipLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.modeTipLabel.setObjectName(_fromUtf8("modeTipLabel"))
        self.horizontalLayout.addWidget(self.modeTipLabel)
        self.modeBox = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBox.sizePolicy().hasHeightForWidth())
        self.modeBox.setSizePolicy(sizePolicy)
        self.modeBox.setObjectName(_fromUtf8("modeBox"))
        self.modeBox.addItem(_fromUtf8(""))
        self.modeBox.addItem(_fromUtf8(""))
        self.modeBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.modeBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.dictionaryTipLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.dictionaryTipLabel.setObjectName(_fromUtf8("dictionaryTipLabel"))
        self.horizontalLayout_3.addWidget(self.dictionaryTipLabel)
        self.dictionaryCurrentLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.dictionaryCurrentLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dictionaryCurrentLabel.setObjectName(_fromUtf8("dictionaryCurrentLabel"))
        self.horizontalLayout_3.addWidget(self.dictionaryCurrentLabel)
        self.dictionaryChooseButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.dictionaryChooseButton.setObjectName(_fromUtf8("dictionaryChooseButton"))
        self.horizontalLayout_3.addWidget(self.dictionaryChooseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.questionNumberTipLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.questionNumberTipLabel.setObjectName(_fromUtf8("questionNumberTipLabel"))
        self.horizontalLayout_4.addWidget(self.questionNumberTipLabel)
        self.questionNumberBox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.questionNumberBox.setObjectName(_fromUtf8("questionNumberBox"))
        self.horizontalLayout_4.addWidget(self.questionNumberBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.questionNumberWarningLabel = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.questionNumberWarningLabel.setFont(font)
        self.questionNumberWarningLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.questionNumberWarningLabel.setObjectName(_fromUtf8("questionNumberWarningLabel"))
        self.verticalLayout.addWidget(self.questionNumberWarningLabel)
        settings.addTab(self.translation, _fromUtf8(""))
        self.text = QtGui.QWidget()
        self.text.setObjectName(_fromUtf8("text"))
        settings.addTab(self.text, _fromUtf8(""))

        self.retranslateUi(settings)
        settings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "Настройки", None, QtGui.QApplication.UnicodeUTF8))
        self.modeTipLabel.setText(QtGui.QApplication.translate("settings", "Режим перевода:", None, QtGui.QApplication.UnicodeUTF8))
        self.modeBox.setItemText(0, QtGui.QApplication.translate("settings", "Авто", None, QtGui.QApplication.UnicodeUTF8))
        self.modeBox.setItemText(1, QtGui.QApplication.translate("settings", "Русский -> Английский", None, QtGui.QApplication.UnicodeUTF8))
        self.modeBox.setItemText(2, QtGui.QApplication.translate("settings", "Английский -> Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionaryTipLabel.setText(QtGui.QApplication.translate("settings", "Файл словаря:", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionaryCurrentLabel.setText(QtGui.QApplication.translate("settings", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.dictionaryChooseButton.setText(QtGui.QApplication.translate("settings", "Обзор...", None, QtGui.QApplication.UnicodeUTF8))
        self.questionNumberTipLabel.setText(QtGui.QApplication.translate("settings", "Число вопросов:", None, QtGui.QApplication.UnicodeUTF8))
        self.questionNumberWarningLabel.setText(QtGui.QApplication.translate("settings", "Выберите 0 для случайного числа вопросов.", None, QtGui.QApplication.UnicodeUTF8))
        settings.setTabText(settings.indexOf(self.translation), QtGui.QApplication.translate("settings", "Перевод", None, QtGui.QApplication.UnicodeUTF8))
        settings.setTabText(settings.indexOf(self.text), QtGui.QApplication.translate("settings", "Текст", None, QtGui.QApplication.UnicodeUTF8))

