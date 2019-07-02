import random

def prime_number(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def random_prime_number(length):
    while True:
        n = random.randint(1 * pow(10, length - 1), 9 * pow(10, length - 1))
        if prime_number(n):
            return n

def mdc(a, b):
    while b != 0:
        rest = a % b
        a = b
        b = rest
    return a
