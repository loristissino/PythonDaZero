#!/usr/bin/env python3

import random

random.seed()

def scegli_parola_casuale():
    listaparole = ['tavolo','mela','linux','corso','farfalla']
    indice_casuale = random.randint(0,len(listaparole)-1)
    return listaparole[indice_casuale]

def scegli_un_nome():
    listaparole = ['antonio','paolo','lucia','beatrice','nicola']
    indice_casuale = random.randint(0,len(listaparole)-1)
    return listaparole[indice_casuale]

scelta_origine_dati = scegli_parola_casuale

#scelta_origine_dati = scegli_parola_casuale() #!!! sbagliato perche' esegue la chiamata invece di assegnare il nome

print(scelta_origine_dati())
