def pytho():
	for i in range(1,500):
		for j in range(1,500):
			k=1000-i-j
			if i**2+j**2==k**2:
				print i*j*k
				break
