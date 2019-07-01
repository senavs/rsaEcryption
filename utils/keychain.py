from ..keys.private_key import PrivateKey
from ..keys.public_key import PublicKey
from ..keys.pair_key import PairKey
from ..exceptions.exceptions import *


class KeyChain(object):
    
    def __init__(self):
        self._data = dict()
    
    def add(self, name, key):
        if not isinstance(key, (PublicKey, PrivateKey, PairKey)):
            raise NotAKey(f"{key} is not an PrivateKey, PublicKey or PairKey")
        self._data["".join(str(name).strip().split())] = key
    
    def remove(self, name):
        del self._data[name]
    
    def save_keys(self):
        save_data = dict()
        for key_name, key in self._data.items():
            data = dict()
            if isinstance(key, PrivateKey) and isinstance(key, PublicKey):
                data['PairKey'] = (key._d, key._e, key._n)
            elif isinstance(key, PrivateKey):
                data['PrivateKey'] = (key._d, key._n)
            elif isinstance(key, PublicKey):
                data['PublicKey'] = (key._e, key._n)
            save_data[key_name] = data
        return save_data
    
    def load_keys(self, keys_data_save, inplace=False):
        if not isinstance(keys_data_save, dict):
            raise LoadKeyDictError("data must be a dict")
        loaded_data = dict()
        for key_name in keys_data_save.keys():
            for key_type, data in keys_data_save[key_name].items():
                if key_type == 'PrivateKey':
                    loaded_data[key_name] = PrivateKey(*data)
                elif key_type == 'PublicKey':
                    loaded_data[key_name] = PublicKey(*data)
                else: 
                    loaded_data[key_name] = PairKey(*data)

        if inplace:
            self._data = loaded_data
            return loaded_data
        return loaded_data       
    
    @property
    def all_keys(self):
        return self._data.keys()

    def __getitem__(self, name):
        return self._data[name]

    def __repr__(self):
        return str(self._data)
