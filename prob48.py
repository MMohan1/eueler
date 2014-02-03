import time
start_time = time.time()
def prob48():
	total = 0
	for i in range(1,1001):
		total += i ** i
	str_total = str(total)
	print str_total[(len(str_total)-10):(len(str_total)+1):1]


if __name__ == "__main__":
	prob48()
	print time.time() - start_time,'seconds'
