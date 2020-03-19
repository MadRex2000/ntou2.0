from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA


class createToken():
    def __init__(self):
        pass

    def token():
        random_generator = Random.new().read
        rsa = RSA.generate(1024, random_generator)
        private_pem = rsa.exportKey()
        return(private_pem)
