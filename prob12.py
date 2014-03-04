def factor(n=10):
	factor = set(reduce(list.__add__,[[i,n/i] for i in range(1,int(n**0.5)+1) if n % i == 0]))
	return factor

def prob12():
	a = 1
	x = 1
	y = 1
	while x:
		a += 1
		y += a
		if len(factor(y)) > 500:
			print y
			break

if __name__ == '__main__':
	prob12()	
	#factor()
