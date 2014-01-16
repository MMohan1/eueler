def prime_fac(n):
	flag=1
	list1=[]
	for i in range(2,n+1):
		if n%i==0:
			for j in range(2,int(i**0.5)+1):
				if i%j==0:
					flag=0
					break
			if flag:
				list1.append(i)
	if list1:
		print max(list1)
	else:
		print 'empty'
				 
