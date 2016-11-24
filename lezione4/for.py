#!/usr/bin/env python3

iscritti = ('Mario', 'Giovanni', 'Luigi')


# ciclo `for`
for corsista in iscritti:
    print(corsista)


# equivalente funzionale con `while`
c = 0
while c < len(iscritti):
    corsista=iscritti[c]    
    print(corsista)
    c+=1


# esempio di uso con `range()`
for i in range(20,3, -3):
    print(i)


'''

Per elaborare tutti gli elementi di un elenco, l'equivalente in altri
linguaggi potrebbe essere simile a quello di questi esempi.


# VB.Net
For i = 0 To iscritti.Length -1:
    corsista=iscritti[i]    
    print(corsista)
Next i

# C / C++ / Java / JavaScript / C#
for (i=0; i < count(iscritti); i++)   // assumendo che esista una funzione count()
{
    corsista=iscritti[i];    
    print(corsista);
}

// PHP
foreach ($iscritti as $corsista)
{  
    print($corsista);
}

'''


