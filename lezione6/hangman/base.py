#!/usr/bin/env python3

import random

random.seed()

listaparole = ['tavolo','mela','linux','corso','farfalla']

indice_casuale = random.randint(0,len(listaparole)-1)
parola = listaparole[indice_casuale]

print(parola)
