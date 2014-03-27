def prob13():
	table = [int(s) for s in open('digit150.txt').readlines()]
	print str(sum(table))[0:10]


if __name__ == '__main__':
	prob13()
