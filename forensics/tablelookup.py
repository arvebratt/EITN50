tempfat1list = list()
tempfat2list = list()
fat1list = list()
fat2list = list()

def init_sequence():
	file = open('image.dat', 'rb')
	bootsector = file.read(512)
	
	i = 0
	while i < 4608:
		tempfat1list.append(file.read(3).hex())
		i += 3
	
	i = 0
	while i < 4608:
		tempfat2list.append(file.read(3).hex())
		i += 3 
	
	for x in tempfat1list:
		temp = x[3] + x[0] + x[1] + x[4] + x[5] + x[2]
		fat1list.append(temp[0:3])
		fat1list.append(temp[3:6])

	for x in tempfat2list:
		temp = x[3] + x[0] + x[1] + x[4] + x[5] + x[2]
		fat2list.append(temp[0:3])
		fat2list.append(temp[3:6])

def amountofentries(num):
	i = 0
	while i < num:
		print('No.' + str(i+1) + ': ' + fat1list[i])
		i += 1


init_sequence()
amountofentries(int(input('Amount of entries? ', )))
