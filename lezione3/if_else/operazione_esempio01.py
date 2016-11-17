#!/usr/bin/env python3

# Scrivere un programma che chieda in
# input due numeri e scriva in output
# il valore della loro somma.

print("Questo programma serve a fare la somma tra due numeri")

a=float(input("Primo numero: "))
b=float(input("Secondo numero: "))

r = a+b

print("La somma è %.2f" % r)

# oppure:
print('La somma è {:.2f}'.format(r))

# Esempi di formattazione dell'output con il nuovo e il vecchio
# stile sono disponibili su https://pyformat.info/

