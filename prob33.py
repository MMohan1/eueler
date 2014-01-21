from __future__ import division
def prob33():
	list1=range(11,100)
	list2=range(11,100)
	list3=range(1,10)
	dict1={}
	for no1 in list1:
		list4=[]
		p=str(no1)
		if p[0]==p[1]:
			for i in range(1,10):
				if int(p[0])>i-1:
					continue
				else:
					list4.append(int(p[0]+str(i)))
			dict1[no1]=list4
		else:
			for i in range(1,10):
				a=int(p[0]+str(i))
				b=int(p[1]+str(i))
				if a>no1:
					list4.append(a)
				elif b>no1:
					list4.append(b)
			dict1[no1]=list4
	list7=[]
	for x,y in dict1.items():
		for z in y:
			list6=[]
			if new_division(x,z)==(x/z):
				list6+=[x,z]
				if list6:
					list7.append(list6)
	print list7
	print ((list7[0][0]/list7[0][1])*(list7[1][0]/list7[1][1])*(list7[2][0]/list7[2][1])*(list7[3][0]/list7[3][1]))*10000
		  
				
	#return dict1
def new_division(a,b):
	p=str(a)
	q=str(b)
	if p[0]==q[0]:
		return int(p[1])/int(q[1])
	elif p[0]==p[1]:
		return int(p[1])/int(q[0])
	elif p[1]==q[0]:
		return int(p[0])/int(q[1])
	elif p[1]==q[1]:
		return int(q[0])/int(q[0])
		



if __name__=='__main__':
	prob33()
	

	
			
