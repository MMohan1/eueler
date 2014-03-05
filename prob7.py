def is_prime(i):
	flag=1
	for j in range(2,(int(i**0.5)+1)):
		if i%j==0:
			flag=0
			return False
	if flag:
		return True
def p10001n0():
	i = 2
	count = 0
	while count != 600:
			if is_prime(i):
				count += 1
			i += 1
	print i-1
if __name__ == '__main__':
	p10001n0()			
