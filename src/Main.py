#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 08.03.2013

@author: deadpadre
'''

from PyQt4 import QtGui, QtCore
import sys
import ConsoleArguments.ConsoleArguments as CLArgs
import GUI.GUI as GUI
import ConsoleMode.ConsoleMode as ConsoleMode

def terminalProgram(questions, mode):
    console     = ConsoleMode.QuizConsole(questions, mode)
    console.run()

def windowProgram():
    app         = QtGui.QApplication(sys.argv)
    window      = GUI.QuizWindow()
    window.move((app.desktop()).availableGeometry(window).center() - window.rect().center())
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    targs       = CLArgs.getArgs()
    reload(sys)
    sys.setdefaultencoding('utf-8') #@UndefinedVariable
    #print sys.getdefaultencoding()
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
    QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("UTF-8"))
    QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
    if targs['terminal']:
        terminalProgram(targs['questions'], targs['mode'])
    else:
        windowProgram()