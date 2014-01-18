def facto():
	fact=1
	sum1=0
	for i in range(100,0,-1):
		fact*=i
	print fact
	str_no=str(fact)
	for i in range(len(str_no)):
		sum1+=int(str_no[i])
	print sum1

if __name__=='__main__':
	facto()
