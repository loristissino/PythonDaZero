#!/usr/bin/env python3

parola = "tavolo"
carattere = 'o'
SEGNAPOSTO = '.'

i = 0
trovato = ''
while i < len(parola):
    if parola[i] == carattere:
        trovato += parola[i]
    else:
        trovato += SEGNAPOSTO
    i += 1
print(trovato) 
