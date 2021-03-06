def prob67():
	table = [[int(n) for n in s.split(' ')] for s in open('triangle.txt').readlines()]
	for row in range(len(table)-1, 0, -1):
		for col in range(0, row):
			table[row-1][col] += max(table[row][col], table[row][col+1])
 
	print "Answer to PE67 = ", table[0][0]
if __name__ == '__main__':
	prob67()
