def factorial(n):
	if n==0:
		return 1
	else:
		return reduce(lambda x,y:x*y,range(1,n+1))
def prob34():
	list1=[]
	for i in range(3,99999):
		p=str(i)
		sum1=0
		for j in range(len(p)):
			sum1+=factorial(int(p[j]))
		if sum1==i:
			list1.append(i)
	print list1
	print sum(list1)
			


if __name__=='__main__':
	prob34()
