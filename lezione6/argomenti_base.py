#!/usr/bin/env python3

def elabora(*args):
    print("Ho ricevuto %d valori." % len(args))
    for a in args:
        print(a)
        

elabora(2,3,5,7,11,13)
elabora(2,10,12,17,18)
