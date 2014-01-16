def smallest():
	flag=1
	for i in range(10,10000):
		for j in range(2,11):
			flag=1
			if i%j!=0:
				flag=0
				break
			
	 	if flag:
			print i
			break
