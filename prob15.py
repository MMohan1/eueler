import sys
import time
start_time = time.time()
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))

def prob15(m,n):
	print factorial(m+n) / (factorial(m) * factorial(n))
	

if __name__ == '__main__':
	prob15(int(sys.argv[1]),int(sys.argv[2]))
	print time.time() - start_time,'seconds'
