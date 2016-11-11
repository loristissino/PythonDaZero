#!/usr/bin/env python3

'''
Esercizio: scrivere un programma python che chiede in input una stringa,
un valore numerico (posizione del primo carattere da estrarre), un 
secondo valore numerico (numero di caratteri da estrarre) e produce in
output i caratteri estratti.
'''

fraseDiBase = input("inserisci una frase:\n")

posIniziale = int(input("da quale carattere iniziare l'estrazione?\n"))-1
# La posizione iniziale è espressa dall'utente in maniera tradizionale
# Il primo carattere è quello in posizione 1.
# Sta a noi programmatori convertirlo nella posizione 0, per cui
# sottraiamo il valore 1.

numCaratteri = int(input("quanti caratteri vuoi estrarre?\n"))

print(fraseDiBase[posIniziale:posIniziale+numCaratteri])
# L'estrazione avviene specificando il limite inferiore (incluso) e 
# quello superiore (escluso)


