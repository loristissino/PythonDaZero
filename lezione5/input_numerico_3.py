#!/usr/bin/env python3

def inputNumber(message, acceptFloat=False):
    """Permette l'inserimento di un numero in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, poi
    tenta la conversione in numero e restituisce il numero
    convertito. Se viene inserito un valore che non è un numero,
    viene richiesto di nuovo l'inserimento.
    Se *accept_float* è vero, accetta anche numeri in virgola mobile.
    """
    
    while(True):
        v=input(message)
        try:
            if acceptFloat:
                return float(v)
            else:
                return int(v)
        except ValueError as err:
            print("A quanto pare, non hai inserito un numero intero…")

# Una versione più raffinata, in cui si introduce un parametro nella
# funzione che ci permette di indicare se vogliamo o meno valori interi

# Qui vogliamo solo numeri interi, per cui non è necessario specificare
# il secondo parametro (che corrisponde già al default)
k1=inputNumber("Inserisci un numero intero: ")
print(k1, type(k1))

# Qui ci va bene anche un numero con posizioni decimali
k2=inputNumber("Inserisci un numero, anche con decimali: ", True)
print(k2, type(k2))
