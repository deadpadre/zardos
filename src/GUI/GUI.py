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
import editDictionaryWindow

class QuizWindow(QtGui.QMainWindow, gui_zardos.Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.defaults = Files.Defaults()
        self.settingsWindow = None
        self.editDictionaryWindow = None
        self.connect(self.openFile,     QtCore.SIGNAL("triggered()"), self.openDict)
        self.connect(self.closeProgram, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.openSettings, QtCore.SIGNAL("triggered()"), self.reviewSettings)
        self.connect(self.openDictionaryEdit, QtCore.SIGNAL("triggered()"), self.reviewEditDictionaryWindow)
        if (os.path.exists(self.defaults.defaultDict)):
            self.openDict(self.defaults.defaultDict)
    def reviewEditDictionaryWindow(self):
        self.editDictionaryWindow = EditDictionaryWindow(self)
        self.editDictionaryWindow.show()
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
            EditDictionaryWindow.firstOpened = True
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
        EditDictionaryWindow.firstOpened = True
        self.dictionaryCurrentLabel.setText(filename)
        self.parent.defaults.setDefaultPath("/".join(str(filename).split('/')[:-1]))
        self.parent.defaults.saveDefaults()
    def saveSettings(self):
        self.parent.defaults.setDefaultDict(self.dictionaryCurrentLabel.text())
        self.parent.defaults.setDefaultQuestionNumber(self.questionNumberBox.value())
        self.parent.defaults.setDefaultMode(self.parent.defaults.indexModeMapper[self.modeBox.currentIndex()])
        self.parent.defaults.saveDefaults()
    def saveAndGo(self):
        self.saveSettings()
        self.close()
    def __init__(self, parentWindow = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parentWindow
        self.dictionaryCurrentLabel.setText(self.parent.defaults.getDefaultDict())
        self.modeBox.setCurrentIndex(self.parent.defaults.getDefaultModeIndex())
        self.questionNumberBox.setValue(self.parent.defaults.getDefaultQuestionNumber())
        self.connect(self.dictionaryChooseButton, QtCore.SIGNAL("clicked()"), self.chooseDictionary)
        self.connect(self.usualButtonBox.button(QtGui.QDialogButtonBox.Apply), QtCore.SIGNAL("clicked()"), self.saveSettings)
        self.connect(self.usualButtonBox.button(QtGui.QDialogButtonBox.Ok), QtCore.SIGNAL("clicked()"), self.saveAndGo)

class EditDictionaryWindow(QtGui.QWidget, editDictionaryWindow.Ui_editDictionaryWindow):
    firstOpened = True;
    def __init__(self, parentWindow = None):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.parent = parentWindow
        self.connect(self.addNewWordButton, QtCore.SIGNAL("clicked()"), self.addNewWord)
        if not EditDictionaryWindow.firstOpened:
            self.dictionaryFile = Files.DictionaryFile(Strings.dictionaryFile, True)
        else:
            self.dictionaryFile = Files.DictionaryFile(self.parent.defaults.getDefaultDict())
        EditDictionaryWindow.firstOpened = False
        words = self.dictionaryFile.tree.getroot()
        for i in xrange(len(words)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(words[i][0].text)))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(words[i][1].text)))
    def accept(self):
        for i in xrange(self.tableWidget.rowCount()):
            try:
                (self.dictionaryFile.tree.getroot().findall('word')[i]).find('eng').text = str(self.tableWidget.item(i, 0).text())
                (self.dictionaryFile.tree.getroot().findall('word')[i]).find('rus').text = str(self.tableWidget.item(i, 1).text())
            except IndexError:
                self.dictionaryFile.addNewWord([str(self.tableWidget.item(i, 0).text()), str(self.tableWidget.item(i, 1).text())])
            #print (self.dictionaryFile.tree.getroot().findall('word')[i]).find('rus').text
        self.dictionaryFile.saveChanges()
        #self.dictionaryFile.saveToTXT(self.parent.defaults.getDefaultDict())
        self.close()
    def reject(self):
        self.close()
    def addNewWord(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setCurrentCell(self.tableWidget.rowCount() - 1, 0)