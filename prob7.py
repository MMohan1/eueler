def p10001n0():
	count=0
	sum1=0
	for i in range(2,2000000):
		flag=1
		for j in range(2,(int(i**0.5)+1)):
			if i%j==0:
				flag=0
				break
		if flag:
			count+=1
			print count,'==>',i
			sum1+=i
	print sum1
			
