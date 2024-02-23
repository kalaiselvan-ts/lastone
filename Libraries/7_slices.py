# [1: -1] this is how the package get splitted

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1: -1]:
    print("hello, my name is", arg)