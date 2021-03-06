#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 27.04.2013

@author: deadpadre

For God's sake, don't change this file!
'''

import xml.etree.ElementTree as ET
import Strings.Strings as Strings
import Core.Core as Core
import os

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
    def getDefaultDict(self):
        return self.defaultDict
    def setDefaultDict(self, dictName):
        self.tree.getroot().find('fileSettings/defaultDict').text = str(dictName)
        self.defaultDict = str(dictName)
    def getDefaultPath(self):
        return self.defaultPath
    def setDefaultPath(self, pathName):
        self.tree.getroot().find('fileSettings/defaultPath').text = str(pathName)
        self.defaultPath = str(pathName)
    def getDefaultModeIndex(self):
        return self.defaultModeIndex
    def getDefaultMode(self):
        return self.defaultMode
    def setDefaultMode(self, modeName):
        self.tree.getroot().find('quizSettings/defaultMode').text = str(modeName)
        self.defaultMode = unicode(modeName)
        self.defaultModeIndex = self.modeIndexMapper[self.defaultMode]
    def getDefaultQuestionNumber(self):
        return self.defaultQuestionNumber
    def setDefaultQuestionNumber(self, number):
        self.tree.getroot().find('quizSettings/defaultQuestionNumber').text = str(number)
        self.defaultQuestionNumber = number
    def saveDefaults(self):
        self.tree.write(Strings.settingsFile, "UTF-8")

class DictionaryFile:
    def __init__(self, filename, fromXML=False):
        if fromXML and ('dictionary.xml' in os.listdir('Files')):
            self.tree = ET.parse(Strings.dictionaryFile)
        else:
            if (fromXML):
                print "XMLDictionaryException: will try to build a new correct one."
            os.remove(Strings.dictionaryFile)
            dictionary = Core.Dictionary(filename)
            os.mknod(Strings.dictionaryFile)
            temp = open(Strings.dictionaryFile, 'w')
            temp.write('<dictionary></dictionary>')
            temp.close()
            self.tree = ET.parse(Strings.dictionaryFile)
            for i in xrange(len(dictionary.dictionary)):
                self.addNewWord(dictionary.dictionary[i])
            self.tree.write(Strings.dictionaryFile, "UTF-8")
    def saveToTXT(self, filename):
        words = self.tree.getroot()
        temp = open(filename, 'w')
        for i in words:
            temp.write(i[0].text + ' ' + i[1].text + '\n')
        temp.close()
    def saveToXML(self, filename):
        self.tree.write(filename, "UTF-8")
    def saveChanges(self):
        self.saveToXML(Strings.dictionaryFile)
    def addNewWord(self, word):
        temp = ET.Element('word')
        temp.append(ET.Element('eng'))
        temp.append(ET.Element('rus'))
        temp.find('eng').text = word[0]#dictionary.dictionary[i][0]
        temp.find('rus').text = word[1]#dictionary.dictionary[i][1]
        self.tree.getroot().append(temp)