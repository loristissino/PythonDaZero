#!/usr/bin/env python3

print("Secondo esempio")

a=5

def qualcosa():
    global a
    print(a)
    a=7   

qualcosa()
print(a)

