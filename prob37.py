def prime_no(n):
	flag=1
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			flag=0
			break
	if flag:
		return True
	else:
		return False


def prob37():
	list1=[]
	list2=[]
	for a in range(11,1000000):
		i=a
		while(len(str(i))>1):
			if prime_no(i):
				b=list(str(i))
				d=b.pop()
				i=int(''.join(b))
				if len(b)==1 and i in [1,2,3,5,7] and int(b[0])!=1:
					list1.append(a)
			else:
				break
	print list1

	for a in list1:
		i=a
		while(len(str(i))>1):
			if prime_no(i):
				b=list(str(i))
				d=b.pop(0)
				i=int(''.join(b))
				if len(b)==1 and i in [1,2,3,5,7] and int(b[0])!=1:
					list2.append(a)
			else:
				break
		if len(list2)==11:
			break

	print sum(list2)

'''def fun2(a):
	i=a
	while(len(str(i))>1):
		if prime_no(i):
			b=list(str(i))
			b.pop(0)
			i=int(''.join(b))
			if len(b)==1 and i in [1,2,3,5,7]:
				return True
			else:
				return False
				break


def prob37():
	list1=[]
	for a in range(13,15):
		if fun1(a) and fun2(a):
			list1.append(a)
	print list1'''
		


if __name__=='__main__':
	prob37()
