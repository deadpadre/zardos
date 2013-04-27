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

class QuizWindow(QtGui.QMainWindow, gui_zardos.Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
        QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("UTF-8"))
        QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
        self.setupUi(self)
        self.connect(self.zopen, QtCore.SIGNAL("triggered()"),  self.openFile)
        self.connect(self.btnOk, QtCore.SIGNAL("clicked()"),    self.testFunc)
    def prepareQuiz(self, filename):
        self.quiz = Core.Quiz(filename)
        self.currentQuestion = self.quiz.askQuestion()
        self.translateLabel.setText(self.currentQuestion.ask())
        self.connect(self.inputLine, QtCore.SIGNAL("returnPressed()"), self.proceedQuestion)
    def proceedQuestion(self):
        answer = self.inputLine.text()
        self.inputLine.selectAll()
        self.answerLabel.setText(self.currentQuestion.check(answer))
        self.currentQuestion = self.quiz.askQuestion()
        self.translateLabel.setText(self.currentQuestion.ask())
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.btnEnterrupt.setEnabled(True)
        self.btnOk.setEnabled(True)
        self.btnSkip.setEnabled(True)
        self.prepareQuiz(filename)
    def testFunc(self):
        temp_str = self.inputLine.text()
        print temp_str
    