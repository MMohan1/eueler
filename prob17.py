def prob17():
	list1=[]
	total_char=0
	dict1={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
	dict2={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eigthteen',19:'nineteen'}
	dict3={0:'',1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eigthty',9:'ninety'}
	#x=raw_input('enter a numbere==>')
	for i in range(1,1001):
		x=str(i)
		if len(x)==3:
			if int(x[1:4])>10 and int(x[1:4])<20:
				list1.append(dict1[int(x[0])]+'hundredand'+dict2[int(x[1:4])])
				print dict1[int(x[0])],'hundred and',dict2[int(x[1:4])]
			else:
				list1.append(dict1[int(x[0])]+'hundredand'+dict3[int(x[1])]+dict1[int(x[2])])
				print dict1[int(x[0])],'hundred and',dict3[int(x[1])],dict1[int(x[2])]
		elif len(x)==2:
			if int(x)>10 and int(x)<20:
				list1.append(dict2[int(x)])
				print dict2[int(x)]				
			else:
				list1.append(dict3[int(x[0])]+dict1[int(x[1])])
				print dict3[int(x[0])],dict1[int(x[1])]
		else:
			if len(x)==4:
				list1.append('onethousand')
				print 'one thousand'
			else:
				list1.append(dict1[int(x)])
				print dict1[int(x)]
	print list1
	for no in list1:
		total_char+=len(no)
	print 'TOTAL CHAR ==>',total_char
