def prob30():
	list1=[]
	for i in range(1000,1000000):
		sum1=0
		a=str(i)
		for j in range(len(a)):
			sum1=sum1+int(a[j])**5
		if i==sum1:
			list1.append(i)
	print list1
	print sum(list1)



if __name__=='__main__':
	prob30()
