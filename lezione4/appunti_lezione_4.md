# Appunti quarta lezione

## Esercizio di riscaldamento

Scrivere un programma che chiede in input
una stringa e la riproduca un po' alla volta, come nel seguente esempio:

    input:
    LINUX
    output:
    L
    LI
    LIN
    LINU
    LINUX

Suggerimento: usare un ciclo while inizializzando un contatore a 0 e 
incrementandone il valore ad ogni passo.

(soluzione nel file `riscaldamento.py`)

## Uscita anticipata da un ciclo `while`

È possibile un'uscita anticipata da un ciclo `while`, come nell'esempio
`while_break.py`. Vedi anche la rappresentazione nel diagramma 
`diagramma_while_break.png`.

## Il ciclo `for`

Quasi sempre i linguaggi di programmazione mettono a disposizione un
costrutto per gestire i casi in cui un ciclo di tipo `while` abbia 
bisogno di incrementare/decrementare un contatore fino al raggiungimento
di una determinata soglia e/o per prendere in considerazione tutti gli 
elementi di una lista o di un elenco.

In genere esistono due costrutti diversi:

1. un ciclo `for` per la gestione di un contatore, basato su numeri interi;
2. un ciclo `foreach` per la gestione di tutti i valori di un elenco. 

In python esiste solo il ciclo `for`, che si basa sul secondo approccio e
delega l'eventuale generazione di valori numerici ad un apposito generatore,
`range()`.

Vedi `for.py`. 


## Esercizio sui cicli

Scrivere un programma che, data una parola nascosta e un carattere da
cercare, scriva una stringa che espone dei segnaposto per i caratteri 
non trovati e il carattere corretto nel caso di carattere trovato.

Ad esempio se ho la parola "tavolo" e cerco il carattere "o" 
ottengo: `___o_o`.

(soluzioni possibili nei file `hang0.py`, `hang1.py`, `hang2.py`, `hang3.py`)

## Il concetto di "eleganza"

Il programma `hang1.py` è migliore di `hang0.py` perché usa una 
costante per segnaposto e assegna `parola[i]` invece di `carattere`
(vedremo che questo facilita le cose se la ricerca avviene tra gli
elementi di un insieme).

Il programma `hang2.py` è ancora migliore perché sfrutta più a fondo 
le caratteristiche del linguaggio python che mette a disposizione
l'operatore ternario.

Infine, in `hang3.py` abbiamo un esempio di funzione.


