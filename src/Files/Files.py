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
        self.defaultQuestionNumber  = int(self.tree.getroot().find('quizSettings/defaultQuestionNumber').text)
        self.modeIndexMapper = {Strings.modeAuto: 0, Strings.modeRusEng: 1, Strings.modeEngRus: 2}
        self.indexModeMapper = {0: Strings.modeAuto, 1: Strings.modeRusEng, 2: Strings.modeEngRus}
        self.defaultModeIndex = self.modeIndexMapper[self.defaultMode]
    def setDefaultDict(self, dictName):
        self.tree.getroot().find('fileSettings/defaultDict').text = str(dictName)
        self.defaultDict = str(dictName)
    def setDefaultPath(self, pathName):
        self.tree.getroot().find('fileSettings/defaultPath').text = str(pathName)
        self.defaultPath = str(pathName)
    def setDefaultMode(self, modeName):
        self.tree.getroot().find('quizSettings/defaultMode').text = str(modeName)
        self.defaultMode = unicode(modeName)
        self.defaultModeIndex = self.modeIndexMapper[self.defaultMode]
    def setDefaultQuestionNumber(self, number):
        self.tree.getroot().find('quizSettings/defaultQuestionNumber').text = str(number)
        self.defaultQuestionNumber = number
    def saveDefaults(self):
        self.tree.write(Strings.settingsFile, "UTF-8") 