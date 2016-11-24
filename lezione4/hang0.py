#!/usr/bin/env python3

parola = "tavolo"
carattere = 'o'
i = 0
trovato = ''
while i < len(parola):
    if parola[i] == carattere:
        trovato += carattere
    else:
        trovato += '_'
    i += 1
print(trovato)

