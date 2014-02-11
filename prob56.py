import time
start_time = time.time()
def prob56():
    list1 = []
    list2 = []
    for i in range(1, 100):
        for j in range(1,100):
            a = i ** j
            list1.append(a)
    for k in list1:
        sum1 = 0
        for m in range(len(str(k))):
            sum1 += int(str(k)[m])
            list2.append(sum1)
    print max(list2)


if __name__ == '__main__':
    prob56()
    print time.time() - start_time,'Seconds'
