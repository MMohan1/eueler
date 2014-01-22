def prime_no(no):
	flag=1
	for i in range(2,int(no**0.5)+1):
		if no%i==0:
			flag=0
			break
	if flag:
		return True
	else:
		return False
def circule_no(no):
	list11=[no]
	a=str(no)
	list1=list(a)
	for i in range(len(list1)-1):
		l=list1[1::1]
		l.append(list1[0])
		list1=l
		str_no=''.join(list1)
		no1=int(str_no)
		list11.append(no1)
	return list11
def prob35():
	list4=[]
	#print circule_no(78)
	for i in range(2,2000000):
		list3=circule_no(i)
		for no in list3:
			if prime_no(no):
				if no==list3[-1]:
					list4.append(list3[0])
			else: 
				break
	list4.sort()
	for no2 in list4:
		a=list4.count(no2)
		if a>1:
			for i in range(1,a):
				list4.remove(no2)
	print list4
	print len(list4)
			

if __name__=='__main__':
	prob35()
