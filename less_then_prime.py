def is_prime(n):
	flag = 1
	for i in range(2, long(n**0.5)+1):
		if n % i == 0:
			flag = 0
			return False
	if flag:
		return True

def less_then_prime(n=2000000):
	prime_set = set()
	for i in range(2, n):
		if is_prime(i):
			prime_set.add(i)
	print prime_set
	print sum(prime_set)


if __name__ == "__main__":
	less_then_prime()
