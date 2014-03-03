from collections import OrderedDict
import time
start_time = time.time()
def power(n, p):
    return n ** p


def prob62():
    sum1 = 0
    OrderdDict = OrderedDict({})
    list1 = []
    for b in range(1, 100):
        a = 1
        list1 = []
        while (len(str(power(a, b)))) <= b:
            if len(str(power(a, b))) == b:
                list1.append(a)
                a += 1
            else:
                a += 1
        if len(list1) > 0:
            OrderdDict[b] = list1
    #print OrderdDict
    for no in OrderdDict.values():
        sum1 += len(no)
    print sum1   
   


if __name__ == "__main__":
    prob62()
    print time.time() - start_time,'Seconds'
