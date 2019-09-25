import random, binascii
"""This script is intended to test the Diffie-Hellman Key
exchange. This computer is key exchanging with itself. The data is stored in plaintext and not encrypted yet"""

#base, modulo, clientX, serverX = 0

# def init_dh():
#     #Part 1, create random Y and P
#     base = random.randint(2, 99999) #public values, base
#     modulo = random.randint(2, 99999) #public values, modulo
#     clientX = random.randint(2, 999) #private value, client
#     serverX = random.randint(2, 999) #private values, server

#     #Make sure Y is < P, in order for diffie-hellman to work
#     while base > modulo :
#         base = random.randint(2, 99999)

def clientValues():
    val = random.randint(2, 999) #private value, client
    return val

def serverValues():
    val = random.randint(2, 999) #private values, server
    return val

def sharedValues(base, modulo):
    base = random.randint(2, 99999) #public values, base
    modulo = random.randint(2, 99999) #public values, modulo
    return base, modulo

def calc_dh(first, second, third):
    return int((first ** second) % third)

def encrypt_DH(self, message):
    print("hej")

def decrypt_DH(self, message):
    print("hej")

#print("Shared Y: " + str(base))
#print("Shared P: " + str(modulo))
#print("My X: " + str(clientX) + " (Private)")
#print("His X: " + str(serverX) + " (Private)")
#
##Part 2: solving the equation
#print("\nY to the X mod P || (Y ** X) % P")
#
#myAns = (base ** clientX) % modulo
#print("My answer: " + str(myAns))
#
#hisAns = (base ** serverX) % modulo
#print("His answer: " + str(hisAns))
#
#print("\nHis answer raised to my X mod P")
#myKey = (hisAns ** clientX) % modulo
#print("My key: decimal " + str(myKey))
#
#print("\nMy answer raised to his X mod P")
#hisKey = (myAns ** serverX) % modulo
#print("His key: decimal " + str(hisKey))
#
##After this, implement AES encryption algorithm from PyCrypto for ensuring safe transfer of data