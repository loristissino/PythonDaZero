# Appunti quinta lezione

## Esercizio di riscaldamento

Scrivere un programma che chiede in input un numero e 
che insista a chiederlo fino a che l'input non è valido, senza che il programma si interrompa bruscamente per un errore _run-time_.

Si può usare il metodo isnumeric() della classe str per verificare che
il testo ricevuto sia numerico prima di convertirlo:

    s = input("Dimmi un numero")
    if s.isnumeric():
        n = int(s)

Meglio se viene implementata una funzione da richiamare.

Esempio di interazione desiderata:

    Inserisci un numero: zero
    A quanto pare, non hai inserito un numero…
    Inserisci un numero: linux
    A quanto pare, non hai inserito un numero…
    Inserisci un numero: shell
    A quanto pare, non hai inserito un numero…
    Inserisci un numero: 12
    Ok. Il numero inserito è 12.

## Principi di programmazione: LBYL vs EAFP

Vedi gli esempi (file `input_numerico_*.py`).

## Variabili mutabili e immutabili

Abbiamo visto come non è possibile modificare oggetti immutabili (es. stringhe),
ma solo rimpiazzarne il valore.

    >>> s="ciao"
    >>> s[0]
    'c'
    >>> s[0]="k"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

Abbiamo visto che la funzione `id()` ci consente di vedere a che cosa
"punta" una variabile.

    >>> id(s)
    140110200352696

Abbiamo visto che accodando un valore ad una stringa il suo `id` cambia,
perché viene allocata un'area di memoria completamente nuova:

    >>> s+=", come stai?"
    >>> s
    'ciao, come stai?'
    >>> id(s)
    140110170657104

... e che quindi non è "pythonico" concatenare stringhe accodando valori.

Abbiamo visto che più variabili possono "puntare" allo stesso oggetto
in memoria: 

    >>> id(s)
    140110170657104
    >>> t=s
    >>> id(t)
    140110170657104

## Tuple

Abbiamo introdotto il concetto di "tupla" (`tuple`), una sequenza 
immutabile di valori (anche eterogenei tra loro):

    >>> m = 10, 12, 8, 42, "lunedì"
    >>> # o, meglio:
    >>> m = (10, 12, 8, 42, "lunedì")
    >>> m
    (10, 12, 8, 42, 'lunedì')
    >>> m[0]
    10
    >>> len(m)  # quanti valori contiene la tupla?
    5
    >>> m[0]=99  # impossibile: la tupla è immutabile...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Abbiamo visto che alle tuple si possono assegnare valori prendendoli da
altre sequenze:

    >>> elenco = (12, 20, 40)
    >>> a, b, c = elenco
    >>> (a, b, c) = elenco   # equivalente alla riga precedente
    >>> a
    12
    >>> b
    20
    >>> c
    40

Abbiamo visto che la tupla di sinistra deve essere capiente al punto 
giusto:

    >>> a, b = elenco
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: too many values to unpack (expected 2)
    >>> a, b, c, d = elenco
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: not enough values to unpack (expected 4, got 3)

... e che però esiste la possibilità di avere un elemento pigliatutto:

    >>> elenco = (12, 20, 40, 55, 3, 8, 71)
    >>> a, *b, c= elenco
    >>> a
    12
    >>> b
    [20, 40, 55, 3, 8]
    >>> c
    71
    >>> a, b, *c= elenco
    >>> a
    12
    >>> b
    20
    >>> c
    [40, 55, 3, 8, 71]

Abbiamo visto il modo "pythonico" di scambiare di valore tra loro due
variabili:

    >>> a=20
    >>> b=40
    >>> a,b = b,a
    >>> a
    40
    >>> b
    20

## Liste

Abbiamo visto che, oltre alle tuple, esistono le liste, che a differenza
delle prime sono mutabili:

    >>> altroelenco = [ 30, 40, 12, 80, 99 ]
    >>> altroelenco
    [30, 40, 12, 80, 99]
    >>> altroelenco[0]
    30
    >>> altroelenco[0]=800
    >>> altroelenco
    [800, 40, 12, 80, 99]

Infine, abbiamo accennato al fatto che per fare la copia "vera" di
variabili mutabili sia necessario usare i metodi `copy()` e/o
`deepcopy()` del modulo `copy`.
