#!/usr/bin/env python3

def elabora(*args, **kwargs):
    print("Ho ricevuto %d valori e %d parametri con nome." % (len(args), len(kwargs)))
    for v in args:
        print(v)
    for k in kwargs.keys():
        print('%s => %s' % (k, kwargs[k]))
        
elabora(42, 44, 46, 48, a=20, b=30)


'''
il richiamo seguente non funziona: gli argomenti con nome devono
seguire quelli senza nome
'''
# elabora(42, 44, c=99, 46, 48, a=20, b=30)
