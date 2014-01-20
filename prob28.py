def prob28():
	list1=[]
	for i in xrange(2,101):
		for j in range(2,101):
			list1.append(i**j)
	#print list1
	#print len(list1)
	list1.sort()
	for no in list1:
		x=list1.count(no)
		if x>1:
			for i in range(1,x):
				list1.remove(no)
	#list1.sort()
	#print list1
	print len(list1)


if __name__=='__main__':
	prob28()
