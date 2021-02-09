#!/usr/bin/python

import sys

def main():
    print("Number of arguments: %d" % len(sys.argv))
    print("Argument List: %s" % str(sys.argv))

    sys.exit(0)

if __name__ == "__main__":
    main()
