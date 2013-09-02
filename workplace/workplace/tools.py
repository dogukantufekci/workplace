from random import random
from hashlib import sha512


def generate_key(length, extra=None):
    if length > 128:
        msg = "Length must be less than or equal to 128"
        raise ValueError(msg)
    return sha512(str(random())+str(extra)).hexdigest()[:length]


def generate_digit_key(length):
    if length > 12:
        msg = "Length must be less than or equal to 12"
        raise ValueError(msg)
    return str(random())[2:2+length]