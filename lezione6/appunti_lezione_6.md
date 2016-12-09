# Appunti sesta lezione

## Esercizio di riscaldamento

Analizzare il codice sorgente di `contab0.py` e, prima di eseguirlo,
pensare a che cosa succederà eseguendolo. Successivamente, eseguirlo e 
verificare se le proprie ipotesi risultavano corrette. Infine, confrontare
quel codice con quello di `contab1.py`.

## Funzioni con numero variabili di parametri

Abbiamo visto che le funzioni possono anche essere definite in maniera
tale da accettare un numero variabile di parametri. Questo può essere
utile quando si devono elaborare gruppi di valori. Un esempio minimale
è presente in `argomenti_base.py`.

Si possono avere funzioni definite per accettare un numero variabile di 
parametri con nome. Questo non lo abbiamo visto a lezione, ma ci sono
dei sorgenti a cui si può dare un'occhiata se incuriositi dalla faccenda:
`argomenti_kwargs.py` e `argomenti_args_kwargs.py`.

## Asserzioni

Le asserzioni servono a gestire problemi di programmazione (tipico
esempio: la chiamata di una funzione con parametri errati). Non vanno
confuse con la gestione di errori _run-time_ che si potrebbero
verificare per problemi di input/output o di altro genere (che si 
gestiscono con il costrutto `try... except...`.

Regola di base: ricordarsi che tutte le asserzioni potrebbero essere
eliminate nella versione finale del programma.

I problemi segnalati con asserzioni che falliscono **non vanno** gestite
con blocchy `try... except...`, vanno risolti correggendo il codice sorgente.

Un esempio minimale è presente in `asserzioni.py`.

## Ricorsione

Una funzione può chiamare sé stessa: vedi ad esempio `ricorsione.py`.

## Ambito di visibilità delle variabili

Vedere gli esempi presenti in `scope1.py`, `scope2.py`, `scope3.py`.

## Gestione di diversi tipi di errori con `try... except...`

Vedere l'esempio `try_except.py`.

## Progetto "gioco dell'impiccato"

Nella cartella `hangman` sono presenti cinque versioni diverse di una bozza
di programma che per ora fa solo l'estrazione casuale di una parola da 
una lista di parole.

Nella prima, `01_base`, non si fa uso di funzioni.

Nella seconda, `02_con_funzione`, viene definita una funzione e poi richiamata.

Nella terza, `03_con_esecuzione_solo_nel_caso_di_chiamata_diretta`, viene 
definita una funzione, che è però richiamata solo quando il programma 
è invocato direttamente (e non quando lo stesso codice viene importato
in altro programma).

Nella quarta, `04_con_richiamo_di_modulo`, si vede come il codice della terza
versione può essere importato come modulo in un proprio programma diverso.
Con questa logica si può organizzare il codice in maniera migliore.

Nella quinta, `05_con_scelta_di_funzione`, viene mostrato come si possano
avere due funzioni distinte per ottenere un determinato risultato, e poi
si possa associare un nome generico di funzione ad una di quelle specifiche.



