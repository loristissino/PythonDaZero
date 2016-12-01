#!/usr/bin/env python3

def inputNumber(message):
    """Permette l'inserimento di un numero in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, verifica
    che la stringa contenga un valore numerico e restituisce il valore
    corrispondente. Se viene inserito un valore che non è un numero,
    viene richiesto di nuovo l'inserimento.
    """
    
    tuttoOk = False
    while not tuttoOk:
        v=input(message)
        tuttoOk = True
        if not v.isnumeric():
            tuttoOk = False
            print("A quanto pare, non hai inserito un numero…")
    return float(v)

# Prima di convertire una stringa nel suo valore numerico, controlliamo
# che l'operazione sia possibile.
# Si applica il principio LBYL (Look before you leap, Guarda prima di saltare)
# Funziona, ma si può migliorare...

# Richiamiamo la funzione...

k=inputNumber("Inserisci un numero: ")
print(k)
