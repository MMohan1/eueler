def sunday():
	dict1={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
	dict2={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31,13:1}
	a=1
	total=0
	for i in range(1901,2001):
		if i%4==0:
			dict2[2]=29
		for j in range(1,13):
			k=dict2[j]%7
			a+=k
			a=a%7
			if a==6:
				if j==12:
					print 'in',i+1,'year','1 first day was sunday'
				else:
					print 'in',i,'year',j+1,'first day was sunday'
				total+=1
		dict2[2]=28
	print 'total sunday is==>',total
	
