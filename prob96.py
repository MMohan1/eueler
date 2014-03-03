from time import time
start_time = time()
from decimal import *
getcontext().prec = 100
def prob80():
    list2 = []
    for i in range(1, 100):
        sqrt = Decimal(i) ** Decimal('0.5')
        list1 = str(sqrt).split('.')
        list1.pop(0)
        m = list(str(list1))
        m.pop(0)
        m.pop(0)
        m.pop(-1)
        m.pop(-1)
        list2.append(sum([int(x) for x in m]))
    print sum(list2)
       


if __name__ == '__main__':
    prob80()
    print time() - start_time,'Seconds'
