from collections import *
def is_prime(n):
	flag = 1
	for i in range(2, long(n**0.5)+1):
		if n % i == 0:
			flag = 0
			return False
	if flag:
		return True

def prob134():
	a = 5
	m = set()
	dict1 = OrderedDict({})
	for i in range(7,100000,2):
		num_str = ''
		x = 1
		if is_prime(i):
			p = a
			q = i
			a = q
			num_str += str(x)
			num_str += str(p)
			y = int(num_str)
			while y % q != 0:
				num_str = ''
				x += 1
				num_str += str(x)
				num_str += str(p)
				y = int(num_str)
			#dict1[y] = [p,q] 
			m.add(y)	
	print sum(m)

if __name__ == '__main__':
	prob134()
			
