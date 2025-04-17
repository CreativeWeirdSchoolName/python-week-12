import string
import random

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

password = ''

i = 1
while 1 < 13:
    random_letter = random.choice(string.ascii_lowercase)

    password = random_letter
    i += 1
