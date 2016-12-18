#!/usr/bin/env python3

import usefulmodule.usefulfunctions

if __name__ == '__main__':
    print("Ho importato un modulo che si chiama «%s»" % usefulmodule.__name__)
    print("Adesso richiamerò una funzione di quel modulo:")
    usefulmodule.usefulfunctions.show_sys_paths()
    
