#!/usr/bin/env python3

import usefulfunctions

if __name__ == '__main__':
    print("Ho importato un modulo che si chiama «%s»" % usefulfunctions.__name__)
    print("Adesso richiamerò una funzione di quel modulo:")
    usefulfunctions.show_sys_paths()
    
