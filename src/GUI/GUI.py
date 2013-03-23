'''
Created on 10.03.2013

@author: deadpadre
'''
import gui_zardos
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow, gui_zardos.Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.zopen, QtCore.SIGNAL("triggered()"),  self.openFile)
        self.connect(self.btnOk, QtCore.SIGNAL("clicked()"),    self.testFunc)
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.btnEnterrupt.setEnabled(True)
        self.btnOk.setEnabled(True)
        self.btnSkip.setEnabled(True)
        return filename
    def testFunc(self):
        temp_str = self.inputLine.text()
        print temp_str
    