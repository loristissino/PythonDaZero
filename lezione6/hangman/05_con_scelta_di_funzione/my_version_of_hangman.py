#!/usr/bin/env python3

import hangman

if __name__ == '__main__':
    scegli_parola_casuale = hangman.scegli_parola_casuale_da_un_dizionario_esterno
    print(scegli_parola_casuale())
