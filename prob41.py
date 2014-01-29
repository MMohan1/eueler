import sys
import time
start_time = time.time()
def is_prime(n):
    flag = 1
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            flag = 0
            break
    if flag:
        return True
    else:
        return False


def prob41():
    list1 = []
    for i in xrange(7650000, 7660000):
        if(is_prime(i)):
            list1.append(i)
    #print list1

    list2 = []
    for j in list1:
       
        m = str(j)
        for i in range(len(m)):
            if m.count(m[i])>1:
                break
            if i == len(m) - 1:
                list2.append(j)
    #print list2
    list3 = []
    for k in list2:
        n = str(k)
        for o in range(len(n)):
            if int(n[o]) not in range(1,len(n)+1):
                break
            if o == len(n) - 1:
                list3.append(k)
    print max(list3)
               



if __name__ == '__main__':
    prob41()
    print time.time() - start_time,'seconds'
