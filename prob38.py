import sys
def paindigit(no):
	no_list=list(no)
	#print no_list
	if '0' in no_list:
		return False
	else:
		for i in no_list:
			if no_list.count(i)>1:
				return False
			elif i==no_list[-1]:
				return True


def prob38():
	for i in range(9432,9245,-1):
		a=str(i*1)+str(i*2)
		if paindigit(a):
			print a
			break

if __name__=='__main__':
	#paindigit(int(sys.argv[1]))
	prob38()
 

