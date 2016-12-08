#!/usr/bin/env python3

def title(s, level):
    if level>1:
        print()
    print(s)
    print(('=', '-')[level-1]*len(s))


title("Quarto esempio", 1)

def qualcosa(v):
    a=None
    try:
        a=1/int(v)
        #raise ValueError("Something wrong")
    except ZeroDivisionError as err:
        print("Tentativo di divisione per zero")
    except ValueError as err:
        print("Tentativo di conversione di valore non numerico")
    return a

title("Prima esecuzione", 2)
#print(qualcosa("50"))


title("Seconda esecuzione", 2)
#print(qualcosa("0"))


title("Terza esecuzione", 2)
print(qualcosa("cat"))

