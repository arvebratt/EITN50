#How to encrypt strings in python
from cryptography.fernet import Fernet

key = Fernet.generate_key() #creates a random key everytime being called upon

print("\nOur key is: " + str(key))

#Encode the message
message = "my deep dark secret"
encoded = message.encode()
print("\n1. Message to encrypt is: " + str(message))

#Encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)
print("\n2. Message is now encrypted into: " + str(encrypted))

#decrypt
f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)

#Decode the message
original_message = decrypted.decode()
print ("\n3. This is the message decoded and decrypted: " + str(original_message))
