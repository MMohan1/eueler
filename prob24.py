import itertools
def prob24():
	x=0
	l=list(itertools.permutations(range(10)))
	print l[1000000]

if __name__=='__main__':
	prob24()
