#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import lib1

if __name__ == '__main__':
    print("I just imported a module called: %s\n" % lib1.__name__)
    print("And I call a function from it\n")
    lib1.func1()
    
