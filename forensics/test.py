hexcode = open('image.dat', 'rb')

hexstring = hexcode.read().hex()

result = bytearray.fromhex(hexstring)

#for x in hexstring:
#	print('x')
	

print(result)
