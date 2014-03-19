'''import math

def function(num=5,minimal=1):
	temp = 1
	if num <= 1:
		return 1
	else:
		for i in range(1, int(math.floor(num/2))+1):
			if i >= minimal:
				temp += function(num-i, i)
	return temp

def main():
	print function(100,1)-1'''



def prob76():
	target = 10
	ns = range(1,10)
	ways = [1] +[0]*target
	print ways
	#print ns
	for n in ns:
		for i in range(n,target+1):
			#print ways
			ways[i] += ways[i-n]
			#import pdb;pdb.set_trace()
	print ways	
	print ways[target]


if __name__ == '__main__':
	prob76()

if __name__ == "__main__":
	main()
