from time import time
start_time = time()
def is_prime(n):
	flag = 1
	for i in range(2, long(n**0.5)+1):
		if n % i == 0:
			flag = 0
			return False
	if flag:
		return True
def less_then_prime(n=100000):
	prime_set = set()
	for i in range(2, n):
		if is_prime(i):
			prime_set.add(i)
	return sum(prime_set)


def prob133():
	s = set()
	i =1
	while i < 20:
		n = 7
		q = 10**i
		while True:
			if n > 100000:
					break 
			if is_prime(n) and pow(10,q,n) == 1:
				s.add(n)
			n += 2
		i += 1
	print s
	print "Answer to PE133 =",less_then_prime(100000) - sum(s)


if __name__ == "__main__":
	prob133()
	print time() - start_time,'Seconds'
