#!/usr/bin/env python3

parola = "tavolo"
carattere = 'o'
SEGNAPOSTO = '.'

i = 0
trovato = ''
while i < len(parola):
    trovato += parola[i] if parola[i] == carattere else SEGNAPOSTO
    i += 1
    
print(trovato) 



