def prob32():
	list11=[]
	list12=[]
	for i in range(1,10):
		for j in range(1,10):
			if(i==j):
				continue
			else:
				a=i*10+j
				list11.append(a)
	for k in range(1,10):
		for l in range(1,10):
			if l==k:
				continue
			for m in range(1,10):
				if m==l or m==k:
					continue
				else:
					b=k*100+l*10+m
					list12.append(b)

	
	

	#print list11
	#print list12
	
	dict1={}
	for no2  in list12:
		list13=[]
		for no1 in list11:
		 	p=str(no1)
			for d in range(len(p)):
				if p[d] in str(no2):
					break
				elif d==1:
					list13.append(no1)
		dict1[no2]=list13
	#print dict1

	
			
		
					
			
			
		 
	dict3={}
	list10=[]
	for key,value in dict1.items():
		for no in value:
			list20=[]
			list20+=[key,no]
			product=key*no
			list20+=[product]
			#no_str=str(key)+str(value)+str(product)
			list10.append(list20)
	#print list10
	
	
	list15=[]
	for x in list10:
		no_str=''
		for y in x:
			no_str+=str(y)
		list15.append(no_str)
	#print list15


	list30=[]

	for z in list15:
		if len(z)<10:
			for a in range(len(z)):
				if z.count(z[a])>1:
					break
				elif a==(len(z)-1):
					list30.append(z)
	
	#print list30 
	for i in range(3):
		for no in list30:
			if '0' in no:
				#print no
				list30.remove(no)
	

	#print list30
	

	list6=range(2,10)
	list7=[]
	for k in range(1,10):
		for l in range(1,10):
			if l==k:
				continue
			for m in range(1,10):
				if m==l or m==k:
					continue
				for p in range(1,10):
					if p==m or p==l or p==k:
						continue
					else:
						b=p*1000+k*100+l*10+m
						list7.append(b)

	#print list6
	#print list7

	dict111={}
	for no2  in list7:
		list8=[]
		for no1 in list6:
		 	p=str(no1)
			if p in str(no2):
				continue
			else:
				list8.append(no1)
				dict111[no2]=list8
	#print dict111


	 
	
	list100=[]
	for key,value in dict111.items():
		for no in value:
			list200=[]
			no_str1=''
			list200+=[key,no]
			product1=key*no
			list200+=[product1]
			#no_str=str(key)+str(value)+str(product)
			list100.append(list200)
	#print list100


	
	list105=[]
	for x in list100:
		no_str=''
		for y in x:
			no_str+=str(y)
		list105.append(no_str)
	#print list105


	list300=[]

	for z in list105:
		if len(z)<10:
			for a in range(len(z)):
				if z.count(z[a])>1:
					break
				elif a==(len(z)-1):
					list300.append(z)
	#print list300


	for i in range(4):
		for no in list300:
			if '0' in no:
				#print no
				list300.remove(no)
	#print list300

	list30+=list300
	list23=[]
	for i in list30:
		list23.append(i[5:9:1])
	#print list23
	sum1=0
	for i in list23:
		if list23.count(i)>1:
			list23.remove(i)

	#print list23
	sum1=0
	for x in list23:
		sum1+=int(x)
	print sum1
		


	
	


	

	


		




if __name__=='__main__':
	prob32()
