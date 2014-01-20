def prob23():
	list2=[]
	list4=range(1,28124)
	for i in range(1,28124):
		list1=[]
		for j in range(1,int(i/2)+1):
			if i%j==0:
				list1.append(j)
		total=sum(list1)
		if i<total:
			list2.append(i)	
	print list2
	list3=[]
	for i in range(20,28124):
		for j in list2:
			for k in list2:
				if (j+k)==i:
					if (j+k) in list3:
						continue
					else:
						list3.append(i)
					list4.remove(i)
			
	print list3
	print list4
	print sum(list4)



if __name__=='__main__':
	prob23()
