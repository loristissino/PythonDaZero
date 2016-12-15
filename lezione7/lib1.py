#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys


def func1():
    print("My name is %s \n" % __name__)
    print("The python search paths are \n")
    for i in sys.path:
        print(i)

if __name__ == '__main__':
    func1()
    
