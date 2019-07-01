import random

from ..keys.private_key import PrivateKey
from ..keys.public_key import PublicKey
from ..keys.pair_key import PairKey
from ..exceptions.exceptions import *

class Locksmith(object):
    
    def new_key(self, length):
        if length < 3:
            raise ValueError("Length must be greater than 2")
        while True:
            p = self.random_prime_number(length)
            q = self.random_prime_number(length)
            if p != q:
                break
        n = p * q        
        z = (p - 1) * (q - 1)
        for e in range(2, z):
            if self.mdc(z, e) == 1:
                break
        d = 1
        while True:
            if (d * e) % z == 1:
                break
            d += 1
        return PairKey(d, e, n)

    def cast(self, pair_key, to):
        if not isinstance(pair_key, PairKey):
            raise CastError("You can only cast an PairKey to a PrivateKey or PublicKey")
        if to.lower() == 'private':
            return PrivateKey(pair_key._d, pair_key._n)
        elif to.lower() == 'public':
            return PublicKey(pair_key._e, pair_key._n)
        else:
            raise CastError(f"{to} is not an key type. Try 'public' or 'private'")
    
    @staticmethod
    def prime_number(number):
        if number == 1:
            return False
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True
    
    @classmethod
    def random_prime_number(cls, length):
        while True:
            n = random.randint(1 * pow(10, length - 1), 9 * pow(10, length - 1))
            if cls.prime_number(n):
                return n
    
    @staticmethod
    def mdc(a, b):
        while b != 0:
            rest = a % b
            a = b
            b = rest
        return a
