import sys
def factorial(n):
	if n == 0:
		return 1
	else:
		return reduce(lambda x,y:x*y,range(1,n+1))
def num(n):

	p = 0
	for i in str(n):
		p += factorial(int(i))
	return p
def produce_list():
	count = 0
	for i in range(1,1000000):
		list1 = []
		x = 0
		list1.append(i)
		a = num(i)
		while a not in list1 and len(list1) < 61:
			list1.append(a)
			a = num(a)
		if len(list1) == 60:
			count += 1
			print list1
	print count


if __name__ == '__main__':
	produce_list()

