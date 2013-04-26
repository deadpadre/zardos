'''
Created on 24.03.2013

@author: deadpadre
'''

import Strings.Strings as Strings
import random

MAX_QUESTIONS = 100

def isAlpha(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        return True
    else:
        return False

class Dictionary:
    def __init__(self, srcfile):
        sfile = open(srcfile, 'r');
        lines = sfile.readlines()
        sfile.close();
        
        rdictionary = []
        for i in xrange(len(lines)):
            if (len(lines[i].split()) != 0 and lines[i][0] != '/'):
                rdictionary.append(lines[i].split())
        
        self.dictionary = []
        for i in xrange(len(rdictionary)):
            self.dictionary.append([])
            for j in xrange(len(rdictionary[i])):
                if not isAlpha(rdictionary[i][j][0]):
                    self.dictionary[i].append(' '.join(rdictionary[i][:j]))
                    self.dictionary[i].append(' '.join(rdictionary[i][j:]))
                    break
                if j == len(rdictionary[i]) - 1:
                    print 'ERROR LE FATALE AT LINE %d IN AFTERFILE' % i
                    exit(0)

class Question:
    def __init__(self, dictionary, newQuestionNumber, mode):
        self.question = dictionary[newQuestionNumber][mode]
        self.answer = dictionary[newQuestionNumber][(mode + 1) % 2]
    def check(self, answer):
        return Strings.yanswer + answer + '\n' + Strings.ranswer + self.answer + '\n' 
    def ask(self):
        return self.question

class Quiz:
    def __init__(self, srcname):
        self.questionsNumber = random.randint(0, MAX_QUESTIONS)
        self.currentProceeded = 0
        self.dictionary = Dictionary(srcname).dictionary
        self.quiz = []
        for i in xrange(self.questionsNumber):
            self.quiz.append(Question(self.dictionary, random.randint(0, len(self.dictionary) - 1), random.randint(0, 1)))
    def hasQuestions(self):
        return (self.currentProceeded < self.questionsNumber);
    def askQuestion(self):
        self.currentProceeded += 1
        return self.quiz[self.currentProceeded - 1]
        return 