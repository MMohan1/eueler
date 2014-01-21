def prob31():
	ways = [0]*201
	ways[0] = 1
	for x in [1,2,5,10,20,50,100,200]:
		for i in range(x, 201):
			#print ways[i]
			#print ways[i-x]
			ways[i] += ways[i-x]
			#print ways
			
	#print ways
	print ways[200]





if __name__=='__main__':
	prob31()
