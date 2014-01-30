'''def prob45():
	h,t,p = 1,2,3
	for i in range(1000, 3000):
		if h == t == p:
			break	
		h = i*(2*i - 1)
		if i == 2999:
			print h
		for j in range(2000, 3500):
			p = (j*(3*j - 1))/2
			if p > h:
				break
			for n in range(3000, 5000):
				t = (n*(n + 1))/2
				if t > p:
					break
				if h == t == p:
					print i,j,n,p
					break
			#break
		#break
		#if h == t == p:
			#break'''
def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def main():
    p = set(pentagonal(n) for n in range(100000))
    h = set(hexagonal(n) for n in range(100000))
    for n in range(100000):
        t = triangle(n)
        if t in p and t in h and t > 40755:
            print t


if __name__ == '__main__':
	main()
	
		
