# calling custom library

import sys

from 11_custom.library import Unit_test.hello as hello

if len(sys.argv) == 2:
    hello(sys.argv[1])