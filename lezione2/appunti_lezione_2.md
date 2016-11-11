# Appunti seconda lezione

## Risorse

Documentazione di python: [docs.python.org/3](https://docs.python.org/3/)

Editor geany: [geany.org](https://www.geany.org/)

Percorso delle librerie: `/usr/lib/py*`


## Conversione implicita non supportata

    >>> s = "ok"

    >>> s+1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

    >>> 1+s
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    >>> 3*s
    'okokok'
    >>> s*3
    'okokok'

    >>> s/2
    >>> s-1


## Formattazione di stringhe ("vecchio" metodo)

    >>> welcome = "Benvenuti al corso di programmazione da" + 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

    >>> welcome = "Benvenuti al corso di programmazione da %d"
    >>> version = 0
    >>> print( welcome % version )
    Benvenuti al corso di programmazione da 0

    >>> welcome = "Benvenuti al corso di %s da %d"
    >>> corso = "programmazione"
    >>> print( welcome % corso, version )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: not enough arguments for format string

    >>> print( welcome % (corso, version) )
    Benvenuti al corso di programmazione da 0
    >>> corso = "linux"
    >>> print( welcome % (corso, version) )
    Benvenuti al corso di linux da 0

    >>> version = 1.1
    >>> print( welcome % (corso, version) )
    Benvenuti al corso di linux da 1

    >>> welcome = "Benvenuti al corso di %s da %f"
    >>> print( welcome % (corso, version) )
    Benvenuti al corso di linux da 1.100000

    >>> welcome = "Benvenuti al corso di %s da %.2f"
    >>> print( welcome % (corso, version) )
    Benvenuti al corso di linux da 1.10


## Metodi sulle stringhe

    >>> welcome[:9]
    'Benvenuti'
    >>> welcome[0:9]
    'Benvenuti'

    >>> welcome[13]
    'l'
    >>> welcome[13:]
    'corso di %s da %.2f'

    >>> welcome[13:18]
    'corso'
    >>> welcome[13:18].capitalize()
    'Corso'
    >>> welcome[13:18].upper()
    'CORSO'

    >>> len(welcome)
    32

## Promozione di tipi

    >>> num = 1

    >>> type(num) is int
    True
    >>> type(num)
    <class 'int'>

    >>> num = num + 1
    >>> type(num)
    <class 'int'>

    >>> num = num + 1.1
    >>> type(num)
    <class 'float'>

    >>> num = num - 1.1
    >>> type(num)
    <class 'float'>

    >>> num
    2.0
    >>> num = int(num)
    >>> type(num)
    <class 'int'>
    >>>

## Import

    >>> import random
    >>> dir(random)

    >>> random.randint(0,100)
    >>> random.randint(0,100)
    >>> random.randint(0,100)

    >>> from random import randint
    >>> randint(0,100)

    >>> dir()
    >>> help(random)



