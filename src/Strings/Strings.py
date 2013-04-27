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
questions       = Argument(keys = ['--questions', '-q'], typed = int, default = 10, h = 'Количество вопросов, которое задаст программа.')
auto            = Argument(keys = ['--auto', '-a'], action = 'store_true', default = False, h = 'Выберите этот аргумент для автоматической работы программы: случайной выбор режима для каждого слова, число слов равно двадцати')
terminal        = Argument(keys = ['--terminal', '-t'], action = 'store_true', default = False, h = 'Выберите этот аргумент для запуска в терминале.')
ranswer         = 'Правильный ответ - '
yanswer         = 'Ваш ответ - '
console         = 'terminal'
window          = 'window'
endString       = 'Вопросы кончились'
selectFile      = 'Выберите файл'
settingsFile    = 'Files/settings.xml'