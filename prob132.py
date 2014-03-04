def factor(n=10):
	print n
	factor = set(reduce(list.__add__,[[i,n/i] for i in xrange(1,long(n**0.5)+1) if n % i == 0]))
	print factor
	return factor



def is_prime(n):
	flag = 1
	for i in range(2, long(n**0.5)+1):
		if n % i == 0:
			flag = 0
			break
	if flag:
		return True
	else:
		return False 
def prob132():
	s = set()
	n, q = 7, 10**9
	 
	while len(s) < 40:
		if is_prime(n) and pow(10, q, n) == 1: 
			s.add(n)
		n += 2
	print s 
	print "Answer to PE132 =", sum(s)


if __name__ == '__main__':
	prob132()
