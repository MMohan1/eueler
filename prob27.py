import math
def isprime(x):
	flag=1
	for i in range(2,int(x**0.5+1)):
		if x%i==0:
			flag=0
			break
	if flag:
		return True
	else:
		return False
primes=[]
b=[]
for i in range(2,1000):
	if isprime(i):
		primes+=[i]
for no in primes:
	b.append(-1*no)
primes+=b

def fun(a,b,n):
	return n*n+a*n+b
list1=[]
dict1={}

def prob27():
	list1=[]
	dict1={}
	for a in primes:
		for b in primes:
			n=1
			while n:
				pr=fun(a,b,n)
				if isprime(abs(pr)):
					list1.append(n)
					dict1[n]=a*b
					n+=1
				else:
	
					break


	
	output=max(list1)
	print dict1[output]




if __name__=='__main__':
	prob27()


