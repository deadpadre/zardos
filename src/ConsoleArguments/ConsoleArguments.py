#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 08.03.2013

@author: deadpadre
'''
import argparse
import Strings.Strings as Strings

def getArgs():
    parser = argparse.ArgumentParser(description = Strings.description, epilog = Strings.epilog, prog = Strings.prog)
    parser.add_argument(Strings.questions.keys[0],  Strings.questions.keys[1],  type = int,                         default = -1,                       help = Strings.questions.h)
    parser.add_argument(Strings.mode.keys[0],       Strings.mode.keys[1],       type = int,                         default = 0,                        help = Strings.mode.h)
    parser.add_argument(Strings.terminal.keys[0],   Strings.terminal.keys[1],   action = Strings.terminal.action,   default = Strings.terminal.default, help = Strings.terminal.h)
    targs = vars(parser.parse_args())
    return targs