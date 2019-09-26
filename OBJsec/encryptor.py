from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import random
import sys

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def intkey_to_aeskey(key):
    key = int_to_bytes(key)
    hash_object = hashlib.md5(key)
    key = hash_object.hexdigest()
    return key[0:16]

def intkey_to_aesiv(key):
    key = int_to_bytes(key)
    hash_object = hashlib.md5(key)
    key = hash_object.hexdigest()
    return key[16:32]

def str_padding(message):
    data = bytes(message, 'utf-8')
    length = 16 - (len(data) % 16)
    data += bytes([length])*length
    return data

def str_depadding(data):
    data = data[:-data[-1]]
    message = str(data, 'utf-8')
    return message

def aes_encrypt(key, iv, message):
    data = str_padding(message)
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(data)
    return ciphertext

def aes_decrypt(key, iv, ciphertext):
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.decrypt(ciphertext)
    message = str_depadding(ciphertext)
    return message