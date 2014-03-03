from __future__ import division
import sys
import time
from collections import OrderedDict
start_time = time.time()
def gcd(a, b):
    if a <= 0 or b<=0:
        return -1
    if a > b:
        a, b = b, a
    while a:
        p = a
        a = b % a
        b = p
    #print p
    if p == 1:
        return True
    else:
        return False


def maximum(od):
    max1 = 0
    key = 0
    for k, v in enumerate(od.items()):
        length = len(v[1])
        high = v[0] / length
        if high > max1:
            max1 = high
            key = v[0]
    print max1
    return key

def prob69():
    od = OrderedDict({})
    for i in range(2310, 2311):
        list1 = []
        for k in range(1, i):
            if gcd(k, i):
                list1.append(k)
        od[i] = list1
    #print od
    print maximum(od)

if __name__ == "__main__":
    prob69()
    print time.time() - start_time,"Seconds"
