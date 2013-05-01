#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 27.04.2013

@author: deadpadre

For God's sake, don't change this file!
'''

import xml.etree.ElementTree as ET
import Strings.Strings as Strings

class Defaults:
    def __init__(self):
        self.tree = ET.parse(Strings.settingsFile)
        self.defaultDict = self.tree.getroot().find('fileSettings/defaultDict').text
        self.defaultPath = self.tree.getroot().find('fileSettings/defaultPath').text
        self.defaultMode = self.tree.getroot().find('quizSettings/defaultMode').text
        self.defaultModeIndex = -1
        if (self.defaultMode == Strings.modeAuto):
            self.defaultModeIndex = 0
        if (self.defaultMode == Strings.modeRusEng):
            self.defaultModeIndex = 1
        if (self.defaultMode == Strings.modeEngRus):
            self.defaultModeIndex = 2
    def setDefaultDict(self, dictName):
        self.tree.getroot().find('fileSettings/defaultDict').text = str(dictName)
        self.defaultDict = str(dictName)
        self.saveDefaults()
    def setDefaultPath(self, pathName):
        self.tree.getroot().find('fileSettings/defaultPath').text = str(pathName)
        self.defaultPath = str(pathName)
        self.saveDefaults()
    def setDefaultMode(self, modeName):
        self.tree.getroot().find('quizSettings/defaultMode').text = str(modeName)
        self.defaultMode = str(modeName)
        self.saveDefaults()
    def saveDefaults(self):
        self.tree.write(Strings.settingsFile, "UTF-8") 