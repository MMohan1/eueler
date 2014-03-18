import math

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
	print function(100,1)-1

if __name__ == "__main__":
	main()
