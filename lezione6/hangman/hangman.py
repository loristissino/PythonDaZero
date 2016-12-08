#!/usr/bin/env python3

import random

random.seed()

def scegli_parola_casuale():
    listaparole = ['tavolo','mela','linux','corso','farfalla']
    indice_casuale = random.randint(0,len(listaparole)-1)
    return listaparole[indice_casuale]

if __name__ == '__main__':
    print(scegli_parola_casuale())
