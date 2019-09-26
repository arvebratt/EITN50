from Crypto.Cipher import AES
import hashlib
import random

obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)


obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
obj2.decrypt(ciphertext)

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_to_16_byte_hashstring(key):
    key = int_to_bytes(key)
    hash_object = hashlib.md5(key)
    key = hash_object.hexdigest()
    return key[0:16]

def new_iv():
    return ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

def aes_encrypt():
    print("inget")