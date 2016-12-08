#!/usr/bin/env python3

print("Terzo esempio")

a=5

def qualcosa():
    b=42
    def qualcosaltro():
        nonlocal b
        b=52
    print(b)
    qualcosaltro()
    print(b)

qualcosa()

