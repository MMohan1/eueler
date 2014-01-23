def smallest():
	flag=1
	for i in range(10,10000):
		for j in range(2,11):
			flag=1
			if i%j!=0:
				flag=0
				break
			
	 	if flag:
			print i
			break
		
		
		
		
	
'''this is best way to short out this problem'''
	

def gcd(a,b):
	if a<0 or b<0:
		return -1
	elif a>b:
		a,b=b,a
		
	while a:
		p=a
		a=b%a
		b=p
	return b

def fun1():
	no=1
	for i in range(1,20):
		no=(no*i)/gcd(i,no)
	print no




if __name__=="__main__":
	fun1()
