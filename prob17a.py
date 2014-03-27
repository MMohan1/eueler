def prob17():
	list1=[]
	total_char=0
	dict1={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
	dict2={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
	dict3={0:'',1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty'}
	for i in range(1,100):
		x=str(i)
		if len(x) == 1:
			list1.append(dict1[i])
		elif len(x) == 2 and x[1] == '0':
			list1.append(dict3[int(x[0])])
		elif len(x) == 2 and x[0] == '1':
			list1.append(dict2[i])
		elif len(x) == 2:
			list1.append(dict3[int(x[0])]+dict1[int(x[1])])
	p = sum([len(i) for i in list1])
	print list1,p
	k = 3*((13*99)+p) + 3*((14*99)+p) + 3*((15*99)+p) + len('onethousand') + p + 99
	print k


if __name__ == '__main__':
	prob17()
