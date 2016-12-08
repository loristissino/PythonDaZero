#!/usr/bin/env python3

def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

print(fattoriale(5))

