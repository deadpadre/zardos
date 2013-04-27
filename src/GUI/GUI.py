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

class QuizWindow(QtGui.QMainWindow, gui_zardos.Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
        QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("UTF-8"))
        QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
        self.setupUi(self)
        self.defaults = Files.Defaults()
        self.connect(self.openFile, QtCore.SIGNAL("triggered()"),  self.openDict)
        if (os.path.exists(self.defaults.defaultDict)):
            self.openDict(self.defaults.defaultDict)
    def prepareQuiz(self, filename):
        self.quiz = Core.Quiz(filename)
        self.currentQuestion = self.quiz.askQuestion()
        self.translateLabel.setText(self.currentQuestion.ask())
        self.connect(self.inputLine, QtCore.SIGNAL("returnPressed()"), self.proceedQuestion)
        self.connect(self.btnOk, QtCore.SIGNAL("clicked()"), self.proceedQuestion)
        self.connect(self.btnInterrupt, QtCore.SIGNAL("clicked()"), self.interruptQuiz)
    def proceedQuestion(self):
        try:
            answer = self.inputLine.text()
            self.inputLine.selectAll()
            self.answerLabel.setText(self.currentQuestion.check(answer))
            self.currentQuestion = self.quiz.askQuestion()
            self.translateLabel.setText(self.currentQuestion.ask())
        except AttributeError:
            self.answerLabel.setText(Strings.endString)
    def interruptQuiz(self):
        self.quiz.interrupt()
        self.proceedQuestion()
    def openDict(self, existedFilename = None):
        if (existedFilename == None):
            filename = QtGui.QFileDialog.getOpenFileName(self, Strings.selectFile, self.defaults.defaultPath)
            self.defaults.setDefaultDict(filename)
            self.defaults.setDefaultPath("/".join(str(filename).split('/')[:-1]))
            print filename
            print "/".join(str(filename).split('/')[:-1])
        else:
            filename = existedFilename
        self.btnInterrupt.setEnabled(True)
        self.btnOk.setEnabled(True)
        self.btnSkip.setEnabled(True)
        self.prepareQuiz(filename)