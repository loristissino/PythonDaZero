#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import lib2

if __name__ == '__main__':
    print("I just imported a module called: %s\n" % lib2.__name__)
    print("And I call a function from it\n")
#    lib2.func1()  ### non funziona perche' devo indicare il nome del file che contiene le funzioni
    lib2.func2.func1()
    
