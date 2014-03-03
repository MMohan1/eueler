from collections import *
def sum_number(n):
	total = 0
	str_num = str(n)
	for i in str_num:
		total += int(i)
	return total

def prob119():
	dict1 = OrderedDict({})
	i = 11
	while i:
		if len(dict1.keys()) == 15:
			break
		total = sum_number(i)
		for j in range(1, total):
			if total**j > i:
				break
			elif total**j == i:
				dict1.update({i:[total,j]})
				print dict1
				break
		i += 1
	print dict1



if __name__ == "__main__":
	prob119()
		
