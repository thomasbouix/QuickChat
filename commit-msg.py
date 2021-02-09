#!/usr/bin/python

import sys
import re

def main():
    """ Description : verification du format du nom du commit """
    with open(sys.argv[1], "r") as fp:
        ligne = fp.readlines()

    message = str(ligne[0]).rstrip()
    print(message)

    pattern = re.compile("\[(US|DO)([1-9]+)\](\s{1})([a-z]{1,}|\s)*")
    result = pattern.match(message)
    if result == None :
        print("Le format du commit n'est pas valide.\nExemple de format valide : \"[US100] mon message\"")
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
