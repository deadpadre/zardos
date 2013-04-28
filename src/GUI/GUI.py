#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 10.03.2013

@author: deadpadre
'''
import gui_zardos
from PyQt4 import QtCore, QtGui
import Core.Core as Core
import Strings.Strings as Strings
import os.path
import Files.Files as Files
import settingsWindow

class QuizWindow(QtGui.QMainWindow, gui_zardos.Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.defaults = Files.Defaults()
        self.settingsWindow = None
        self.connect(self.openFile,     QtCore.SIGNAL("triggered()"), self.openDict)
        self.connect(self.closeProgram, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.openSettings, QtCore.SIGNAL("triggered()"), self.reviewSettings)
        if (os.path.exists(self.defaults.defaultDict)):
            self.openDict(self.defaults.defaultDict)
    def reviewSettings(self):
        self.settingsWindow = SettingsWindow(self)
        self.settingsWindow.show()
    def prepareQuiz(self, filename):
        self.quiz = None
        self.quiz = Core.Quiz(filename)
        self.currentQuestion = self.quiz.askQuestion()
        self.answerLabel.setText(Strings.defaultAnswer)
        self.translateLabel.setText(self.currentQuestion.ask())
    def proceedQuestion(self):
        try:
            answer = self.inputLine.text()
            self.inputLine.selectAll()
            self.answerLabel.setText(self.currentQuestion.check(answer))
            self.currentQuestion = self.quiz.askQuestion()
            self.translateLabel.setText(self.currentQuestion.ask())
        except AttributeError:
            self.disconnect(self.btnOk, QtCore.SIGNAL("clicked()"), self.proceedQuestion)
            self.disconnect(self.inputLine, QtCore.SIGNAL("returnPressed()"), self.proceedQuestion)
            self.disconnect(self.btnInterrupt, QtCore.SIGNAL("clicked()"), self.interruptQuiz)
            self.answerLabel.setText(Strings.endString + '\n' + " ".join(str(self.answerLabel.text()).split()[3:]))
    def interruptQuiz(self):
        self.quiz.interrupt()
        self.proceedQuestion()
    def openDict(self, existedFilename = None):
        if (existedFilename == None):
            filename = QtGui.QFileDialog.getOpenFileName(self, Strings.selectFile, self.defaults.defaultPath)
            if (filename == u''):
                return
            self.defaults.setDefaultDict(filename)
            self.defaults.setDefaultPath("/".join(str(filename).split('/')[:-1]))
            print filename
            print "/".join(str(filename).split('/')[:-1])
        else:
            filename = existedFilename
        self.connect(self.inputLine, QtCore.SIGNAL("returnPressed()"), self.proceedQuestion)
        self.connect(self.btnOk, QtCore.SIGNAL("clicked()"), self.proceedQuestion)
        self.connect(self.btnInterrupt, QtCore.SIGNAL("clicked()"), self.interruptQuiz)
        self.btnInterrupt.setEnabled(True)
        self.btnOk.setEnabled(True)
        self.btnSkip.setEnabled(True)
        self.prepareQuiz(filename)

class SettingsWindow(QtGui.QTabWidget, settingsWindow.Ui_settings):
    def setTranslation(self, translationMode):
        print translationMode
        self.parent.quiz.setTranslation(translationMode)
        self.multipleTranslationButton.setText(translationMode)
    def __init__(self, parentWindow = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.mapper = QtCore.QSignalMapper()
        self.translationModeMenu = QtGui.QMenu()
        self.parent = parentWindow
        translationAuto = QtGui.QAction(Strings.modeAuto, self.translationModeMenu)
        self.connect(translationAuto, QtCore.SIGNAL("triggered()"), self.mapper, QtCore.SLOT("map()"))
        self.mapper.setMapping(translationAuto, Strings.modeAuto)
        self.connect(self.mapper, QtCore.SIGNAL("mapped(const QString &)"), self.setTranslation)
        self.translationModeMenu.addAction(translationAuto)
        #self.translationModeMenu.addAction(Strings.modeRusEng)
        #self.translationModeMenu.addAction(Strings.modeEngRus)
        self.multipleTranslationButton.setMenu(self.translationModeMenu)