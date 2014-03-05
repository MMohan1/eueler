from fractions import *
import time
s_t = time.time()
import sys
def prob(n=97):
	
		no = 1
		count = 1
		while (no!= 0):
			no = (no*10 + 1) % n
			count += 1
		return count
	

def factor(n):
	flag = 1
	factor = list(set(reduce(list.__add__,[[i,n/i] for i in xrange(1,long(n**0.5)+1) if n % i == 0])))
	if len(factor) > 2:
		return True
	else:
		return False

def prob1():
	limit = 1000001
	n = 91
	list1 = []
	while len(list1) < 25:
		k = prob(n)
		if ((n-1) % k == 0 and factor(n)):
			list1.append(n)
		n += 2
		if gcd(n,10) != 1:
			n += 2
	print list1
	print sum(list1)

if __name__ == "__main__":
	prob1()
	print time.time() - s_t,'Seconds'
