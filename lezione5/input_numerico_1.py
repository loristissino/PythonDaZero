#!/usr/bin/env python3

def inputNumber(message):
    """Permette l'inserimento di un numero in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, verifica
    che la stringa contenga un valore numerico e restituisce il valore
    corrispondente. Se viene inserito un valore che non è un numero,
    viene richiesto di nuovo l'inserimento.
    """
    
    while(True):
        v=input(message)
        if v.isnumeric():
            return float(v)
        else:
            print("A quanto pare, non hai inserito un numero…")

# Meccanismo di base simile al precedente, ma codice leggermente
# semplificato, con uscita anticipata dal ciclo quando abbiamo un
# valore da restituire.
# Si applica ancora il principio LBYL


# richiamiamo la funzione...

k=inputNumber("Inserisci un numero: ")
print(k)
