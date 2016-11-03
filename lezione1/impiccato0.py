#!/usr/bin/env python3
# La prima riga, qui sopra, dal punto di vista dell'interprete python
# è un commento. Serve alla shell per sapere quale interprete usare
# per l'esecuzione del programma.
# Tecnicamente, si tratta di una shabang
# (vedi https://it.wikipedia.org/wiki/Shabang)                             

# questo è un commento su una riga

# (tutto ciò che segue un simbolo # è considerato commento)

# il seguente può essere considerato un commento su più righe...
'''
Questo programma è stato svuiluppato
dal PNLUG in occasione del corso "Programmazione da 0"
su Python
'''
# ... ma in realtà è una stringa multilinea che, non essendo stata
# assegnata ad una variabile, non causa nessun effetto sull'esecuzione
# del programma.

# creiamo una variabile e le assegniamo un valore
nomeDelGioco = "L'impiccato"
# il nome della variabile non può contenere spazi e deve iniziare con
# una lettera oppure con il simbolo "underscore" (_)

versioneProgramma = 1
numeroMassimoTentativi = 8
numeroTentativiEffettuati = 0

# creiamo un'altra variabile e le assegniamo un valore
# concatenando due stringhe, una costante e una variabile
messaggio = "Benvenuto al gioco " + nomeDelGioco

# produzione di output
print (messaggio)  # visualizza messaggio di benvenuto
print ("messaggio")  # visualizza la scritta "messaggio"

# output su più righe di una stringa che contiene sequenze di escape
# \n per andare a capo
# \" per mostrare un doppio apice
# \' per mostrare un apice singolo
# \\ per mostrare una barra
print("Nel gioco dell'\"impiccato\" ti verrà mostrata una sequenza di trattini\ne dovrai indovinare una parola della stessa lunghezza.")

# output multinea
# le sequenze di caratteri delimitate da tre apici (singoli o doppi)
# possono essere comode:
print("""Nel gioco dell'"impiccato" ti verrà mostrata una sequenza di trattini
e dovrai indovinare una parola della stessa lunghezza.""")

print("Avrai a disposizione " + str(numeroMassimoTentativi) + " tentativi.")




