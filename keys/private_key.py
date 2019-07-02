from ..exceptions.exceptions import *


class PrivateKey(object):
    
    def __init__(self, key, key_id):
        self._d = key
        self._n = key_id
    
    def sign(self, text):
        if not isinstance(text, str):
            raise NotATextMensage("text must to be a string (str)")
        for data in text:
            yield pow(ord(data), self._d) % self._n

    def decrypt(self, text, as_string=False):

        def return_not_as_string(text):
            for data in text:
                yield chr(pow(data, self._d) % self._n)

        def return_as_string(text):
            string = str()
            for data in text:
                string += chr(pow(data, self._d) % self._n)
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
            
    def __repr__(self):
        return 'PrivateKey(%s, %s)' % (self._d, self._n)
