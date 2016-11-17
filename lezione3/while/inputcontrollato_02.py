#!/usr/bin/env python3

# Scrivere un programma che chieda in input un numero intero,
# insistendo a richiederlo fino a che il numero abbia le seguenti
# caratteristiche:
# a) deve essere diverso da 0
# b) deve essere pari
# Applicare il principio DRY


# Una prima versione potrebbe essere la seguente (però viola il
# il principio DRY):
'''

n=0

while n==0 or n%2==1:
    n=int(input("Inserisci un numero pari diverso da zero: "))
    if n==0:
        print("Il numero non può essere 0.")
    if n%2==1:
        print("Il numero deve essere pari.")

'''

# Questa è migliore:

tuttoOk = False

while not tuttoOk:
    n=int(input("Inserisci un numero pari diverso da zero: "))
    tuttoOk = True
    if n==0:
        print("Il numero non può essere 0.")
        tuttoOk = False
    if n%2!=0:
        print("Il numero deve essere pari.")
        tuttoOk = False


print("Hai inserito il valore %d." % n)
