#!/usr/bin/env python3

print("Primo esempio")

a=5

def qualcosa():
    print(a)
#    a=7   
    '''
    fare o meno questa assegnazione ha un riflesso
    sull'esistenza di questa variabile nell'ambito di visibilità locale
    '''

qualcosa()
print(a)

