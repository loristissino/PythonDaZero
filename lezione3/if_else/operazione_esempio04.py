#!/usr/bin/env python3

# Scrivere un programma che chieda in input tre valori: due numeri
# e un carattere ("+" o "-") effettui l'operazione richiesta e scriva
# il messaggio "Il risultato è {valore}."
# Si può dare per scontato che se il terzo input non è "+" allora è "-".

print("Questo programma serve a fare un'operazione a scelta tra somma e differenza tra numeri")

a=float(input("Primo numero: "))
b=float(input("Secondo numero: "))
op=input("Operazione (+ o -): ")

if op=="+":
    r = a+b
else :
    r = a-b

print("Il risultato è %f." % (r))


# Notare che il codice seguente, perfettamente funzionante,
# violerebbe il principio DRY (Don't Repeat Yourself)
# (vedi https://it.wikipedia.org/wiki/Don%27t_Repeat_Yourself)
'''

if op=="+":
    print("Il risultato è %f." % (a+b))
else :
    print("Il risultato è %f." % (a-b))

'''
