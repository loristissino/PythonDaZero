#!/usr/bin/env python3

'''
Questo programma gestisce doverse somme di denaro a disposizione in
diversi "depositi".
Le funzioni aggiungi() e preleva() servono ad aggiungere o togliere un
determinato importo da uno dei depositi in cui si trova.

Il motivo per cui il programma, nella versione contab0.py, non funziona
è che i parametri numerici sono oggetti immutabili, per cui qualsiasi
variazione al loro valore all'interno della funzione non ha ripercussioni
sull'esterno (sul programma chiamante).

Una soluzione potrebbe essere quella di avere una lista di depositi,
come nell'esempio che segue. (Si potrebbe fare di meglio, usando dei 
dizionari o delle classi, ma non ci siamo ancora arrivati...)

'''

def aggiungi(importo, depositi, indice):
    depositi[indice] += importo
    print ("Sono stati aggiunti %d euro." % importo)
    print ("Questo deposito contiene ora %d euro." % depositi[indice])

def preleva(importo, depositi, indice):
    prelevabile = min(importo, depositi[indice])
    depositi[indice] -= prelevabile
    print ("Sono stati prelevati %d euro." % prelevabile)
    print ("Questo deposito contiene ora %d euro." % depositi[indice])
    return prelevabile

depositi = [25, 200, 30]
# abbiamo una lista di depositi: il primo (indice 0) è il portafoglio,
# il secondo (indice 1) è il conto bancario, il terzo (indice 2) il
# conto postale

valore = preleva(20, depositi, 0)  
# prelievo di 20 euro dal portafoglio
aggiungi(valore, depositi, 1)
# versamento dell'importo nel conto bancario

print("In portafoglio ci sono ora %d euro." % depositi[0])
# ci si aspetta di avere ora 5 euro

print("Sul conto corrente bancario ci sono ora %d euro." % depositi[1])
# ci si aspetta di avere ora 220 euro

