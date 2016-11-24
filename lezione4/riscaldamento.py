#!/usr/bin/env python3

'''
Scrivere un programma che chiede in input
una stringa e la riproduca un po' alla volta, come nel seguente esempio:

input:
LINUX
output:
L
LI
LIN
LINU
LINUX

Suggerimento: usare un ciclo while inizializzando un contatore a 0 e 
incrementandone il valore ad ogni passo.

'''

s = input("Inserisci una parola: ")
c = 0
while c<len(s):
    c+=1
    print(s[:c])




