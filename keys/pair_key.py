from .private_key import PrivateKey
from .public_key import PublicKey


class PairKey(PrivateKey, PublicKey):

    def __init__(self, private_key, public_key, key_id):
        PrivateKey.__init__(self, private_key, key_id)
        PublicKey.__init__(self, public_key, key_id)

    def __repr__(self):
        return 'PairKey(PrivateKey(%s, %s), PublicKey(%s, %s))' % (self._d, self._n, self._e, self._n)

    @property
    def private_key(self):
        return PrivateKey(self._d, self._n)

    @property
    def public_key(self):
        return PublicKey(self._e, self._n)
