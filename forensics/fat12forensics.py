import array
import pprint

hexlist = list()
fat12entrystring = ''

def init_sequence():
	file = open('image.dat', 'rb')
	rawhex = file.read().hex()
	rawhex[511:

	i = 0
	while i < len(rawhex):
		hexlist.append(rawhex[0+i:8+i])
		i += 8

def fat12_find_n(num):
	if num % 2 == 0:
		pass
		temp = hexlist[int(1+(3*num)/2)]
		fat12entrystring = temp[4:]
		temp = hexlist[int((3*num)/2)]
		fat12entrystring += str(temp)
		print(fat12entrystring)
	else:
		pass 
		temp = hexlist[int(1+(3*num)/2)]
		fat12entrystring = temp
		temp = hexlist[int((3*num)/2)]
		fat12entrystring += str(temp[:4])
		print(fat12entrystring)






init_sequence()
fat12_find_n(int(input('which FAT12 entry? ', )))
