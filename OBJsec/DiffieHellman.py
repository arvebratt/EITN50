import random, binascii
"""This script is intended to test the Diffie-Hellman Key
exchange. This computer is key exchanging with itself. The data is stored in plaintext and not encrypted yet"""

#Part 1, create random Y and P
ourY = random.randint(2, 99999) #public values
ourP = random.randint(2, 99999) #public values
myX = random.randint(2, 999) #private values
hisX = random.randint(2, 999) #private values

#Make sure Y is < P, in order for diffie-hellman to work
while ourY > ourP :
    ourY = random.randint(2, 99999)

print("Shared Y: " + str(ourY))
print("Shared P: " + str(ourP))
print("My X: " + str(myX) + " (Private)")
print("His X: " + str(hisX) + " (Private)")

#Part 2: solving the equation
print("\nY to the X mod P || (Y ** X) % P")

myAns = (ourY ** myX) % ourP
print("My answer: " + str(myAns))

hisAns = (ourY ** hisX) % ourP
print("His answer: " + str(hisAns))

print("\nHis answer raised to my X mod P")
myKey = (hisAns ** myX) % ourP
print("My key: decimal " + str(myKey))

print("\nMy answer raised to his X mod P")
hisKey = (myAns ** hisX) % ourP
print("His key: decimal " + str(hisKey))

exit(0)

#After this, implement AES encryption algorithm from PyCrypto for ensuring safe transfer of data
