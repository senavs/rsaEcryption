from ..exceptions import *


class PublicKey(object):
    
    def __init__(self, key, key_id):
        self._e = key
        self._n = key_id
    
    def authenticate(self, text):
        try:
            getattr(text, '__iter__')
        except:
            raise NotAnIterableObject("text must to be an iterator")
        else:
            for data in text:
                yield chr(pow(data, self._e) % self._n)

    def encrypt(self, text):
        if not isinstance(text, str):
            raise NotATextMensage("text must to be a string (str)")
        for data in text:
            yield pow(ord(data), self._e) % self._n
    
    def __repr__(self):
        return 'PublicKey(%s, %s)' % (self._e, self._n)
