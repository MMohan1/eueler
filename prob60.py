from  itertools import permutations

import sys
def is_prime(n):
    flag = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = 0
            break
    if flag:
        return True
    else:
        return False

def prime_list():
    list3 = []
    for i in range(2, 200):
        if is_prime(i):
            list3.append(i)
    list4 = list(permutations(list3, 5))
    print list4
    return list4


def prob60():
    for no in list4:
        list2 = list(permutations(no, 2))
        print list2
        count = 0
        for number in list2:
            num = int(str(number[0]) + str(number[1]))
            if is_prime(num):
                count += 1
            if count == len(list2):
                print list1
                break
        break
       
   

if __name__ == '__main__':
    #is_prime(int(sys.argv[1]))
    #prob60()
    prime_list()
