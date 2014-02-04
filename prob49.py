import time
import prob41
import itertools
start_time = time.time()
def prob49():
	for i in range(1000,5000):
		list2 = []
		str_no = str(i)
		list1 = list(itertools.permutations(str_no))
		for no in list1:
			real_no = int(''.join(no))
			if prob41.is_prime(real_no):
				list2.append(real_no)
		#print list2
		list3 = []
		list4 = []
		dict1 = {}
		for i in range(0,len(list2)-1):
			for j in range(i+1,len(list2)):
				k = abs(list2[i] - list2[j])
				#print list3
				if k in dict1.keys():
					#print k
					#print list2[i]
					#print list2[j]
					dict1[k].append(list2[j])
					#print list4
				else:
					dict1[k] = [list2[i],list2[j]]
		#print dict1		
		for a, b in dict1.items():
			if len(dict1[a]) > 2  and a == 3330:
				for i in dict1[a]:
					while dict1[a].count(i)!=1:
						dict1[a].remove(i)
				if len(dict1[a]) == 3:
					print dict1[a]
				break
		
			
if __name__ == '__main__':
	prob49()
