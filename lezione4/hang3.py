#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def inputstring(prompt, minlen=1, maxlen=20):
    """ Questa funzione serve per contollare la dimensione di una stringa in input
    Si inserisce la spiegazione del valore da inserire ed eventualmente le dimensioni
    minime e massime.
    """
    ok = False
    while not ok:
        ok = True
        valore = input(prompt)
        if len(valore) < minlen:
            print("La parola inserita è più corta di %d caratteri" % minlen)
            ok = False
        if len(valore) > maxlen:
            print("La parola inserita è più lunga di %d caratteri" % maxlen)
            ok = False
    return valore

parola = inputstring("Inserisci la parola nascosta: ", minlen=4)
carattere = inputstring("Inserisci il carattere da cercare: ", maxlen=1)
SEGNAPOSTO = '.'

i = 0
trovato = ''
while i < len(parola):
    trovato += parola[i] if parola[i] == carattere else SEGNAPOSTO
    i += 1

print(trovato)
