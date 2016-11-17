#!/usr/bin/env python3

# Scrivere un programma che chieda in input un numero intero,
# insistendo a richiederlo fino a che il numero sia diverso da zero.

n=0 # È importante inizializzare la variabile

while n==0:
    n=int(input("Inserisci un numero pari diverso da zero: "))

print("Hai inserito il valore %d." % n)
