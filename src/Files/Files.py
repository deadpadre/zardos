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
        self.defaultDict = self.tree.getroot().find('fileSystem/defaultDict').text
        self.defaultPath = self.tree.getroot().find('fileSystem/defaultPath').text
    def setDefaultDict(self, dictName):
        self.tree.getroot().find('fileSystem/defaultDict').text = dictName
        self.defaultDict = dictName
        self.saveDefaults()
    def setDefaultPath(self, pathName):
        self.tree.getroot().find('fileSystem/defaultPath').text = pathName
        self.defaultPath = pathName
        self.saveDefaults()
    def saveDefaults(self):
        self.tree.write(Strings.settingsFile, "UTF-8") 