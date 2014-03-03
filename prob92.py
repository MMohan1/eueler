import sys
def no(n):
    str_no = str(n)
    k = [int(i)**2 for i in str_no]
    return sum(k)

def prob92():
    count = 0
    for i in range(1, 10000001):
        k = i
        while k != 1:
            k = no(k)
            if k == 89:
                break
            if k == 1:
                count += 1
    print 10000000 - count

if __name__ == '__main__':
    #no(int(sys.argv[1]))
    prob92()
