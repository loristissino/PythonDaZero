#!/usr/bin/env python3

'''
Questo programma gestisce doverse somme di denaro a disposizione in
diversi "depositi".
Le funzioni aggiungi() e preleva() servono ad aggiungere o togliere un
determinato importo da uno dei depositi in cui si trova.

Il programma si comporta correttamente? 
Cercate di capirlo analizzando il codice, prima di eseguirlo.

'''

def aggiungi(importo, deposito):
    deposito += importo
    print ("Sono stati aggiunti %d euro." % importo)
    print ("Questo deposito contiene ora %d euro." % deposito)

def preleva(importo, deposito):
    prelevabile = min(importo, deposito)
    deposito -= prelevabile
    print ("Sono stati prelevati %d euro." % prelevabile)
    print ("Questo deposito contiene ora %d euro." % deposito)
    return prelevabile

# questi sono i depositi, con i loro importi iniziali
portafoglio = 25
contobancario = 200
contopostale = 30

valore = preleva(20, portafoglio)  # prelievo di 20 euro dal portafoglio
aggiungi(valore, contobancario) # versamento dell'importo nel conto bancario

print("In portafoglio ci sono ora %d euro." % portafoglio)
# ci si aspetta di avere ora 5 euro

print("Sul conto corrente bancario ci sono ora %d euro." % contobancario)
# ci si aspetta di avere ora 220 euro
