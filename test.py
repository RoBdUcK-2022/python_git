#! /bin/python

# Made by Sarthak
import random
import string

low_let = string.ascii_lowercase
upp_let = string.ascii_uppercase
numbers = string.digits

all_pass = low_let + upp_let + numbers

length = 8

password = ''.join(random.sample(all_pass, length))

print(password)