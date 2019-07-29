# password generator

import string
import random

def generate_sequence(length, chars):
    x = random.sample(chars, length)

    return "".join(x)



pwd = generate_sequence(3, string.ascii_uppercase) + generate_sequence(3, string.ascii_lowercase) + generate_sequence(6, string.digits)+ generate_sequence(1, string.punctuation)

print("Password = "+pwd)


