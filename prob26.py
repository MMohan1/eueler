'''from __future__ import division
from decimal import *
myothercontext = Context(prec=100, rounding=ROUND_HALF_DOWN)
setcontext(myothercontext)
def count_char(num_str):
	dict1 = {}
	for m in num_str:
		dict1[m] = num_str.count(m)
	#print dict1.keys()
	if len(dict1.keys())>9:
		return dict1
	else:
		return 0
def prob26():
	
	dict2 = {}
	for i in range(2,101):
		list1 = []
		p = Decimal(1)/Decimal(i)
		if len(str(p))>20:
			list1.append(p)
			dict2[i] = list1
	#print dict2
	for no in dict2.keys():
		#print str(dict2[no][0])
		if count_char(str(dict2[no][0])):
			print no
			print dict2[no]

def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        print 10**t % d,
        if 1 == 10**t % d:
            return t
    return 0
def main():
	longest = max(recurring_cycle(1, i) for i in range(2,11))
	print [i for i in range(2,1001) if recurring_cycle(1, i) == longest][0]'''

import math
def cycle_length(n):
	i = 1
	if n % 2 == 0:return (cycle_length(n/2))
	if n % 5 == 0:return (cycle_length(n/2))
	while True:
		if (10**i - 1) % n == 0:return i
		else: i += 1
def main():
	m,n = 0,0
	for d in xrange(1,1000):
		c = cycle_length(d)
		if c > m:
			m = c
			n = d
	print n 
 

			
	
		


if __name__ == '__main__':
	main()
