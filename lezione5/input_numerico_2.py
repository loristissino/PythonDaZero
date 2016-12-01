#!/usr/bin/env python3

def inputInt(message):
    """Permette l'inserimento di un numero intero in maniera controllata.

    Chiede in input una stringa usando *message* come prompt, poi
    tenta la conversione in numero intero e restituisce il numero
    convertito. Se viene inserito un valore che non è un numero,
    viene richiesto di nuovo l'inserimento.
    """
    while(True):
        v=input(message)
        try:
            n=int(v)
            return n
        except ValueError as err:
            print("A quanto pare, non hai inserito un numero intero…")

# Applichiamo il principio EAFP: (easier to ask for forgiveness than
# permission, è più facile chiedere il perdono che il permesso)
# Vantaggi:
#   - coerenza (un solo controllo)
#   - resistenza in caso di esecuzione multi-threaded
#   - struttura portabile in caso di esecuzione di codice per cui 
#     non può essere fatto un controllo preventivo (es. su database)

k=inputInt("Inserisci un numero: ")
print(k)
