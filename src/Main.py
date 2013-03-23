#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 08.03.2013

@author: deadpadre
'''

from random import randint
from PyQt4 import QtCore, QtGui
import sys
import ConsoleArguments.ConsoleArguments as CLArgs
import GUI.GUI as GUI
import Files.Files as Files

class Question:
    def __init__(self, d, k, mode):
        self.q = d[k][mode]
        self.a = d[k][(mode + 1) % 2]
    def check(self, a):
        print 'Правильный ответ - %s' % self.a
        print '\n'
    def ask(self):
        print self.q
        self.check(raw_input());

def main():
    dictionary = Files.makeDictionary('dictionary.txt')
    targs       = CLArgs.getArgs()
    number      = targs['questions']
    for i in xrange(number):
        temp = Question(dictionary, randint(0, len(dictionary) - 1), randint(0, 1))
        temp.ask()

if __name__ == '__main__':
    targs       = CLArgs.getArgs()
    if targs['terminal']:
        main()
    else:
        app         = QtGui.QApplication(sys.argv)
        window      = GUI.MainWindow()
        window.move((app.desktop()).availableGeometry(window).center() - window.rect().center())
        window.show()
        sys.exit(app.exec_())