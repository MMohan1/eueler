from itertools import *
def total_prime(n):
    nonprime = [j for i in range(2, int(n**0.5)+1) for j in range(i*2, n, i)]
    return [i for i in range(2,n) if i not in nonprime]

def combination(l):
    m = list(permutations(l, 3))
    for no in m:
        x = m.count(no)
        if x > 1:
            for i in range(1, x):
                m.remove(no)
    return m



def prob87():
    count = 0
    for i in range(28, 500):
        prime_list = total_prime(i)
        k = [no for no in prime_list if no**2 < i]
        l = k*3
        l.sort()
        #print l
        list1 = combination(l)
        #print list1
        x = [m for m in list1 if m[0]**2 + m[1]**3 + m[2]**4 == i]
        if len(x):
            count += 1
            print i,'==>',x
    print count

if __name__ == '__main__':
    prob87()
    #combination([1,2,3,1,2,3,1,2,3])
