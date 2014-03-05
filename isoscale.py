def fibbonic(n=15):
	a = 1
	b = 1
	count = 2
	while count < n:
		c = a+b
		a,b = b,c
		count += 1
	return c
			

def isoscale():
	print sum([fibbonic(6*n+3)/2 for n in range(1,13)])
if __name__ == '__main__':
	#fibbonic()	
	isoscale()
