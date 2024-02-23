# . : any character except a newline
# * : 0 or more repititions
# + : 1 or more repititions
# ? : 0 or 1 repitition
# {m} : m repititions
# {m,n} : m-n repititions



import re

email = input ("What's your email? "). strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid") 