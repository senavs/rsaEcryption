from ..exceptions.exceptions import *


class PublicKey(object):
    
    def __init__(self, key, key_id):
        self._e = key
        self._n = key_id
    
    def authenticate(self, text, as_string=False):

        def return_not_as_string(text):
            for data in text:
                yield chr(pow(data, self._e) % self._n)

        def return_as_string(text):
            string = str()
            for data in text:
                string += chr(pow(data, self._e) % self._n)
            return string

        try:
            getattr(text, '__iter__')
        except:
            raise NotAnIterableObject("text must to be an iterator")
        else:
            if as_string:
                return return_as_string(text)
            else:
                return return_not_as_string(text)

    def encrypt(self, text):
        if not isinstance(text, str):
            raise NotATextMensage("text must to be a string (str)")
        for data in text:
            yield pow(ord(data), self._e) % self._n
    
    def __repr__(self):
        return 'PublicKey(%s, %s)' % (self._e, self._n)
