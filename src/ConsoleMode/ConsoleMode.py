#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 30.04.2013

@author: deadpadre
'''

import Core.Core as Core
import Strings.Strings as Strings
import Files.Files as Files

class QuizConsole:
    def __init__(self, questions, mode):
        if (mode == 0):
            mode = Strings.modeAuto
        if (mode == 1):
            mode = Strings.modeRusEng
        if (mode == 2):
            mode = Strings.modeEngRus
        self.defaults = Files.Defaults()
        if (questions == -1):
            self.quiz = Core.Quiz(self.defaults.defaultDict, mode)
        else:
            self.quiz = Core.Quiz(self.defaults.defaultDict, mode, questions)
    def run(self):
        while (self.quiz.hasQuestions()):
            currentQuestion = self.quiz.askQuestion()
            print currentQuestion.ask()
            print currentQuestion.check(raw_input())
        print Strings.endString