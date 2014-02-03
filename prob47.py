import prob41
'''def prob47():
	dict1 = {}
	for i in range(100000, 140000):
		k = i
		list1 = []
		a = 2
		while(a <= i):
			if i % a == 0:
				list1.append(a)
				i /= a
		
			a += 1
		dict1[k] = list1
	print dict1

	for k,j in dict1.items():
			
			if len(j) == 4 and k > 134045 and len(dict1[k-3]) == len(dict1[k-1]) == len(dict1[k-2]) == len(dict1[k]) == 4:
				if dict1[k-3][1] % dict1[k-3][0] != 0 and dict1[k-2][1] % dict1[k-2][0] != 0 and dict1[k-1][1] % dict1[k-1][0] != 0:
					#print dict1[k-1][1]
					print k-3,'==>',dict1[k-3]
					print k-2,'==>',dict1[k-2]
					print k-1,'==>',dict1[k-1]
					print k,'==>',dict1[k]
					break'''

def factor(i):
	list1 = []
	a = 2
	while(a <= i):
		if i % a == 0:
			list1.append(a)
			i /= a
		a += 1
	if len(list1) == 4:
		if list1[1] % list1[0] != 0 and list1[2] % list1[1] != 0:
			return list1
		else:
			return []
	else:
		return []
	

def prob47():
	counter = 0
	for i in range (100000, 150000):
		if	counter == 4:
			print i - 4
			break
		else:
			#print len(factor(i))
			if len(factor(i)) == 4:
				print factor(i)
				counter += 1
			else:
				counter = 0
			
	


if __name__ == '__main__':
	prob47()
