'''def lar_palin():
	for i in range(111,1000,1):
		for j in range(111,1000,1):
			no=i*j
			k=str(no)
			if len(k)==6 and k==k[-7:][::-1]:
				print i,j'''

def factor(n):
	list3 = []
	factor = list(set(reduce(list.__add__,[[i,n/i] for i in xrange(1,long(n**0.5)+1) if n % i == 0])))
	#print factor
	list2 = [i for i in factor if len(str(i)) == 3 ]
	#print list2
	list2.sort()
	if len(list2) > 1 and list2[-1] > 900 and list2[-2] > 900:
		list3.append(list2[-1])
		list3.append(list2[-2])
		return list3


def number():
	x = 998*999
	m = 1
	while m:
		#print x
		y = str(x)
		if y == y[::-1]:
			j = factor(x)
			if j:
				print j
				print x
				m = 0
		x -= 1


if __name__ == '__main__':
	number()
