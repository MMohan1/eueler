def prob14():
	longest = 0
	no = 0
	for i in range(1,1000000):
		n = i
		count = 1
		while n != 1:
			if n % 2 == 0:
				n = n/2
				count += 1
				#print n
			else:
				n = 3*n + 1
				count +=1
				#print n
		if count > longest:
			longest = count
			no = i
	print 'longest==>',longest,no


if __name__ == "__main__":
	prob14()
