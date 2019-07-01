class RSAEcryptionException(Exception):
	pass

class NotAnIterableObject(RSAEcryptionException):
	pass

class NotATextMensage(RSAEcryptionException):
	pass

class CastError(RSAEcryptionException):
	pass

class NotAKey(RSAEcryptionException):
	pass

class LoadKeyDictError(RSAEcryptionException):
	pass