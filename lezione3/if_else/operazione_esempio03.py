#!/usr/bin/env python3

# Scrivere un programma che chieda in
# input due numeri e scriva in output
# il valore del loro rapporto.
# Nel caso in cui il rapporto risulti 99,
# emettere il messaggio "Hai vinto un premio!"

print("Questo programma serve a calcolare il rapporto tra due numeri")

a=float(input("Primo numero (dividendo): "))
b=float(input("Secondo numero (divisore): "))

if b!=0:
    r = a/b
    print("Il rapporto è %.2f" % r)
    if r==99:
        print("Hai vinto un premio!")
else:
    print("La divisione è impossibile")


