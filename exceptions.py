class RSAEcryptionException(Exception):
	pass

class NotAnIterableObject(RSAEcryptionException):
	pass

class NotATextMensage(RSAEcryptionException):
	pass
