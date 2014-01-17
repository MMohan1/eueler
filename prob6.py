def diffrence():
	sum1=0
	for i in range(1,101):
		sum1+=i*i
	sum2=sum(range(101))**2
	print sum2-sum1
