def pailendrome(n):
	str_no=str(n)
	if str_no==str_no[::-1]:
		return True
	else:
		return False


def prob36():
	list1=[]
	for i in range(1,1000000):
		if pailendrome(i):
			a=bin(i).replace('0b','')
			if pailendrome(a):
				list1.append(i)
	print list1
	print sum(list1)


if __name__=='__main__':
	prob36()

