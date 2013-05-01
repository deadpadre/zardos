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
import settingsNew

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
        self.quiz = Core.Quiz(filename, self.defaults.defaultMode)
        self.currentQuestion = self.quiz.askQuestion()
        self.answerLabel.setText(Strings.defaultAnswer)
        self.translateLabel.setText(self.currentQuestion.ask())
    def proceedQuestion(self, answer = None):
        try:
            if (answer == None):
                answer = self.inputLine.text()
                self.inputLine.selectAll()
            self.answerLabel.setText(self.currentQuestion.check(answer))
            self.currentQuestion = self.quiz.askQuestion()
            self.translateLabel.setText(self.currentQuestion.ask())
        except AttributeError:
            self.disconnect(self.btnOk,         QtCore.SIGNAL("clicked()"),         self.proceedQuestion)
            self.disconnect(self.inputLine,     QtCore.SIGNAL("returnPressed()"),   self.proceedQuestion)
            self.disconnect(self.btnInterrupt,  QtCore.SIGNAL("clicked()"),         self.interruptQuiz)
            self.disconnect(self.btnSkip,       QtCore.SIGNAL("clicked()"),         self.skipQuestion)
            self.answerLabel.setText(Strings.endString + '\n' + " ".join(str(self.answerLabel.text()).split()[3:]))
    def interruptQuiz(self):
        self.quiz.interrupt()
        self.proceedQuestion('')
    def skipQuestion(self):
        self.quiz.skipQuestion()
        self.proceedQuestion(Strings.skippedQuestion)
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
        self.connect(self.inputLine,    QtCore.SIGNAL("returnPressed()"),   self.proceedQuestion)
        self.connect(self.btnOk,        QtCore.SIGNAL("clicked()"),         self.proceedQuestion)
        self.connect(self.btnInterrupt, QtCore.SIGNAL("clicked()"),         self.interruptQuiz)
        self.connect(self.btnSkip,      QtCore.SIGNAL("clicked()"),         self.skipQuestion)
        self.btnInterrupt.setEnabled(True)
        self.btnOk.setEnabled(True)
        self.btnSkip.setEnabled(True)
        self.prepareQuiz(filename)

class SettingsWindow(QtGui.QTabWidget, settingsNew.Ui_settings):
    def chooseDictionary(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, Strings.selectFile, self.parent.defaults.defaultPath)
        if filename == u'':
            return
        print 'HELLO FUCKERS IM IN DA FUNC'
        self.dictionaryCurrentLabel.setText(filename)
    def __init__(self, parentWindow = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parentWindow
        self.dictionaryCurrentLabel.setText(self.parent.defaults.defaultDict)
        self.modeBox.setCurrentIndex(self.parent.defaults.defaultModeIndex)
        self.connect(self.dictionaryChooseButton, QtCore.SIGNAL("clicked()"), self.chooseDictionary)