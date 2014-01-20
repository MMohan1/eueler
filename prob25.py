def fibb():
	c=0
	list1=[]
	a,b=1,1
	list1.append(1)
	list1.append(1)
	while(len(str(c))<1000):
		c=a+b
		list1.append(c)
		if len(str(c))==1000:
			print c
			print len(list1)
			break
		a,b=b,c


if __name__=="__main__":
	fibb()
