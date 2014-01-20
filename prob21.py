def prob21():
	dict1={}
	total=0
	for i in range(1,10000):
		list1=[]
		list2=[]
		if i in dict1.values():
			continue
		for j in range(1,(int(i/2)+1)):
			if i%j==0:
				list1.append(j)
		total=sum(list1)
		if total==i:
			continue
		for k in range(1,(int(total/2)+1)):
			if total%k==0:
				list2.append(k)
		total1=sum(list2)
		if total1==i:
			dict1[i]=total	
	print dict1
	print 'TOTAL OF AMICABLE NO IS==>',sum(dict1.values())+sum(dict1.keys())

if __name__=="__main__":
	prob21()		
