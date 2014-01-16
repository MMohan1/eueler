def febbonic(n):
	list1=[]
	sum=0
	a,b=1,1
	c=b
	while(c<n):
		#print c
		if c%2==0:
			sum+=c
		c=a+b
		a,b=b,c
	print sum
	
