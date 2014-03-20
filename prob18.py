def prob18():
	table = []
	total = 0
	number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
	num_list = number.split("\n")
	print num_list
	for no in num_list:
		list3 = []
		list2 = no.split(' ')
		for m in list2:
			list3.append(int(m))
		table.append(list3)
	print table
	for row in range(len(table)-1, 0, -1):
		for col in range(0, row):
			table[row-1][col] += max(table[row][col], table[row][col+1])
 
	print "Answer to PE18 = ", table[0][0]
if __name__ == '__main__':
	prob18()
