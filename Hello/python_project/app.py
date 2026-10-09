
for i in range(1, 10):

	for j in range(1, 10):
		x = i + j
		if x % 2 == 0:
			x = ' '
			print(x, end = ' ')
		print (x, end = ' ')
	print(' ')
