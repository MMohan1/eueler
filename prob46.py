import prob41
def solu(n):
	a = 1
	for i in range(3,n):
		if a == n:
			break
		if prob41.is_prime(i):
			for j in range(1,int(n**0.5)):
				a = i + 2 * j**2			
				if a == n:
					return [i,j]
					break
				
				
def prob46():
	dict1 = {}
	for i in range(1000, 10000):
		if prob41.is_prime(i):
			continue
		elif i % 2 == 1:
			if solu(i) == None:
				print i
				break
	'''print dict1
	if None in dict1.values():
		
	else:
		print sorry'''		



if __name__ == '__main__':
	prob46()
