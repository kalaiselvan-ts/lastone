# https://docs.python.org/3/library/sys.html

import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# Adding conditional for alternate way for a defensive output

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
