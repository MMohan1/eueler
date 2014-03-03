import sys
def factor(n):
    k = reduce(list.__add__,[[i, n/i] for i in range(1, int(n**0.5)+1) if n % i == 0])
    k.remove(max(k))
    #print sum(k)
    return sum(k)
def prob95():
    dict1 = OrderedDict({})
    for i in range(1, 1000000):
        a = i
        list2 = []
        count = 0
        print a
        while a < 1000000:
            a = factor(a)
            count += 1
            if a in list2 or a == 1:
                break
            list2.append(a)
            if a == i:
                print 'i==>',i
                dict1[i] = count
                break
    print dict1
    m = 0
    n = 0
    for k, v in dict1.items():
        if v == m:
            continue
        if v > m:
            m = v
            n = k
    print n,m
if __name__ == '__main__':
    prob95()
    #factor(int(sys.argv[1]))
