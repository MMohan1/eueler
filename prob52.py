from itertools import permutations
def prob51():
    k = 1
    z = 1
    y = 142684
    while z:
        list1 = []
        d = str(y)
        m = list(permutations(d))
        #print m
        list2 = [str(y * i) for i in range(1,7)]
        print list2
        for k in list2:
            l = list(permutations(k))
            list1 += l
        print len(list1)
        for x in  range(len(list1)):
            if list1[x] not in m:
                y += 1
                break
            elif list1[x] == list1[-1]:
                for i in range(0,6):
                    if list1[x][i] in list1[1000]:
                        if i == 6:
                            print k
                            print y
                            z = 0
                            k += 1
                            break
                        else:
                   
                            break

if __name__ == '__main__':
    prob51()
