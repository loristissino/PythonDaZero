#!/usr/bin/env python3

import random

random.seed()

def scegli_parola_casuale():
    listaparole = ['tavolo','mela','linux','corso','farfalla']
    indice_casuale = random.randint(0,len(listaparole)-1)
    return listaparole[indice_casuale]

print(scegli_parola_casuale())
