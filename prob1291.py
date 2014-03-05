from fractions import *
import sys
def prob(n):
	if gcd(n,10) != 1:
		return None
	else:
		no = 1
		count = 1
		while (no!= 0):
			no = (no*10 + 1) % n
			count += 1
		#print count
		return count

def prob1():
	limit = 1000001
	n = limit
	while prob(n) < limit:
			n += 2
	print n
	
if __name__ == "__main__":
	prob1() 
