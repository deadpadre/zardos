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
        

description     = 'Тренировка английской лексики.'
epilog          = 'Спасибо за использование %(prog)s'
prog            = 'Zardos'
questions       = Argument(keys = ['-q', '--questions'],                          default = 10,       h = 'Количество вопросов, которое задаст программа.')
mode            = Argument(keys = ['-m', '--mode'     ],                          default = False,    h = '0 - Автоматический режим.\n1 - Русско-английский перевод.\n2 - Англо-Русский перевод.')
terminal        = Argument(keys = ['-t', '--terminal' ], action = 'store_true',   default = False,    h = 'Консольный режим.')
ranswer         = 'Правильный ответ - '
yanswer         = 'Ваш ответ - '
console         = 'terminal'
window          = 'window'
endString       = 'Вопросы кончились.'
selectFile      = 'Выберите файл'
settingsFile    = 'Files/settings.xml'
defaultAnswer   = 'Здесь будут отображаться правильные ответы.'
modeAuto        = 'Авто'
modeRusEng      = 'Русский -> Английский'
modeEngRus      = 'Английский -> Русский'
skippedQuestion  = 'N/A'