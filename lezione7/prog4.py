#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import lib4.func4

if __name__ == '__main__':
    print("I just imported a module called: %s\n" % lib4.__name__)
    print("And I call a function from it\n")
    lib4.func4.func1()
    
