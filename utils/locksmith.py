from ..keys.private_key import PrivateKey
from ..keys.public_key import PublicKey
from ..keys.pair_key import PairKey
from ..exceptions.exceptions import *
from .functions import random_prime_number, mdc

class Locksmith(object):
    
    def new_key(self, length):
        if length < 3:
            raise ValueError("Length must be greater than 2")
        while True:
            p = random_prime_number(length)
            q = random_prime_number(length)
            if p != q:
                break
        n = p * q        
        z = (p - 1) * (q - 1)
        for e in range(2, z):
            if mdc(z, e) == 1:
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
