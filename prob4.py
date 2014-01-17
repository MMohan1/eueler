def lar_palin():
	for i in range(111,1000,1):
		for j in range(111,1000,1):
			no=i*j
			k=str(no)
			if len(k)==6 and k==k[-7:][::-1]:
				print i,j
				
