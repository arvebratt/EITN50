#How to encrypt strings in python
from cryptography.fernet import Fernet

key = Fernet.generate_key() #creates a random key everytime being called upon

#Save the key so you can encrypt/decrypt with the same key
file = open('key.key', 'wb')
file.write(key)  #the key is type bytes, bytes object, therefore 'b'
file.close()
print("\nOur key is: " + str(key))

#Encode the message
message = "my deep dark secret"
encoded = message.encode()
print("\nMessage to encrypt is: " + str(message))

#Encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)
print("\nMessage is now encrypted into: " + str(encrypted))

#decrypt
f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)

#Decode the message
original_message = decrypted.decode()
print ("\nThis is the message decoded: " + str(original_message))
