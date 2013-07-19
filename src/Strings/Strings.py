#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 08.03.2013

@author: deadpadre
'''

class Argument:
    def __init__(self, keys, h, action = '', default = None, typed = None):
        self.keys       = keys
        self.action     = action
        self.h          = h
        self.default    = default
        self.typed      = typed
        

description     = u'Тренировка английской лексики.'
epilog          = u'Спасибо за использование %(prog)s'
prog            = u'Zardos'
questions       = Argument(keys = [u'-q', u'--questions'],                          default = 10,       h = u'Количество вопросов, которое задаст программа.')
mode            = Argument(keys = [u'-m', u'--mode'     ],                          default = False,    h = u'0 - Автоматический режим.\n1 - Русско-английский перевод.\n2 - Англо-Русский перевод.')
terminal        = Argument(keys = [u'-t', u'--terminal' ], action = u'store_true',   default = False,    h = u'Консольный режим.')
ranswer         = u'Правильный ответ - '
yanswer         = u'Ваш ответ - '
console         = u'terminal'
window          = u'window'
endString       = u'Вопросы кончились.'
selectFile      = u'Выберите файл'
settingsFile    = u'Files/settings.xml'
defaultAnswer   = u'Здесь будут отображаться правильные ответы.'
modeAuto        = u'Авто'
modeRusEng      = u'Русский -> Английский'
modeEngRus      = u'Английский -> Русский'
skippedQuestion = u'N/A'
dictionaryFile  = u'Files/dictionary.xml'