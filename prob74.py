import sys
def factorial(n):
	if n == 0:
		return 1
	else:
		#print reduce(lambda x,y:x*y,range(1,n+1))
		return reduce(lambda x,y:x*y,range(1,n+1))
def num(n):
	p = 0
	for no in str(n):
		p += factorial(int(no))
	#print p
	return p

def prob74():
	count = 0
	for i in range(1,1000000):
		list1 = []
		list1.append(i)
		#print list1
		a = num(i)
		#print a
		while a not in list1 and len(list1) < 61:
			list1.append(a)
			#print list1
			a = num(a)
			#print a
		if len(list1)==60:
			print list1
			count += 1
	print count
	

if __name__ == "__main__":
	prob74()
	#num(int(sys.argv[1]))
	#factorial(int(sys.argv[1]))
