#!/usr/bin/env python3

def elabora(**kwargs):
    print("Ho ricevuto %d parametri con nome." % len(kwargs))
    for k in kwargs:
        print(k)
    for k in kwargs:
        print('%s => %s' % (k, kwargs[k]))
        
elabora(a=20, b=30)

myoptions={'a':200, 'b':300}  # dizionario
elabora(**myoptions)
