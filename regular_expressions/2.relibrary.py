# Regular expression operations - https://docs.python.org/3/library/re.html#

import re

email = input ("What's your email? "). strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
          