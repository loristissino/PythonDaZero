#!/usr/bin/env python3

'''
In questo programma è definita una funzione che conta le occorrenze di
un carattere in un testo, senza distinzione tra maiuscole e minuscole.

Potremmo desiderare, come programmatori, che la chiamata alla funzione
fallisca nel caso in cui il primo parametro sia una stringa vuota
oppure il secondo abbia più di un carattere.

A tale scopo si usano le asserzioni.

'''

def contaOccorrenze(testo, carattere):
#    assert(len(testo)>0)
#    assert(len(carattere)==1)
'''
Notare che questa implementazione non è ottimale, in quanto non sfrutta
il metodo count() della classe str, che fa già il lavoro che ci serve.
Lasciamo una migliore implementazione come esercizio...
'''
    conteggio = 0
    for i in range(0, len(testo)):
        if carattere.upper() == testo[i].upper():
            conteggio += 1
    return conteggio

print(contaOccorrenze ("gatto", "a"))
print(contaOccorrenze ("gatto", "t"))
print(contaOccorrenze ("Cuccia", "c"))
print(contaOccorrenze ("Cuccia", "C"))

print(contaOccorrenze ("", "C"))
print(contaOccorrenze ("Cane", "AB"))

