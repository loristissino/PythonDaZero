#!/usr/bin/env python3

import random

random.seed()

def scegli_parola_casuale_da_array_interno():
    listaparole = ['tavolo','mela','linux','corso','farfalla']
    indice_casuale = random.randint(0,len(listaparole)-1)
    return listaparole[indice_casuale]

def scegli_parola_casuale_da_un_dizionario_esterno():
    # non ancora implementato
    # per ora restituiamo sempre la parola "sedia"
    return "sedia"

if __name__ == '__main__':
    scegli_parola_casuale = scegli_parola_casuale_da_array_interno
    # la funzione generica "scegli_parola_casuale" è associata
    # a quella specifica "scegli_parola_casuale_da_array_interno"
    print(scegli_parola_casuale())
