#!/usr/bin/env python3

import sys

def show_sys_paths():
    print("Mi chiamo «%s»." % __name__)
    print("I percorsi di ricerca di python sono:")
    for p in sys.path:
        print("   * %s" % p)

if __name__ == '__main__':
    show_sys_paths()
    
