import itertools
def prob24():
	x=0
	for i in list(itertools.permutations(range(10))):
		x+=1
		if(x==1000000):
			print i
			break



if __name__=='__main__':
	prob24()

