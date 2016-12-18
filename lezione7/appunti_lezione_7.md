# Appunti settima lezione

La lezione è stata dedicata principalmente allo sviluppo del programma
previsto.

## Organizzazione dei moduli

Su richiesta di qualche corsista, sono stati presentati alcuni modi in
cui si possono organizzare i moduli e, nell'ambito degli stessi, le
funzioni.

Le cartelle `esempio{1..4}` contengono alcuni esempi.

La struttura è la seguente:

    .
    ├── esempio1
    │   ├── myprogram.py
    │   └── usefulfunctions.py
    ├── esempio2
    │   ├── myprogram.py
    │   └── usefulmodule
    │       ├── __init__.py
    │       └── usefulfunctions.py
    ├── esempio3
    │   ├── myprogram.py
    │   └── usefulmodule
    │       ├── __init__.py
    │       └── usefulfunctions.py
    └── esempio4
        ├── myprogram.py
        └── usefulmodule
            └── usefulfunctions.py


In tutti gli esempi, il programma `myprogram.py` richiama la funzione
`show_sys_paths()`.


### Esempio1

Il richiamo avviene specificando il nome del file e il nome della
funzione:

    usefulfunctions.show_sys_paths()

### Esempio 2 
   
Il richiamo avviene specificando il nome del modulo, il nome del file 
e il nome della funzione:

    usefulmodule.usefulfunctions.show_sys_paths()

Va notato che il modulo è una directory al cui interno è presente il 
file `__init__.py` che specifica quali file devono essere importati.

### Esempio 3

Il richiamo avviene specificando il nome del modulo e il nome della 
funzione:

    usefulmodule.show_sys_paths()

Ciò è possibile in quanto il file `__init__.py` è impostato in maniera
diversa.

### Esempio 4

Il richiamo avviene dopo aver importanto direttamente il file specifico
contenente la funzione che interessa: 

    usefulmodule.usefulfunctions.show_sys_paths()
    
