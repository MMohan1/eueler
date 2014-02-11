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
       

def prob50():
    list3 = []
    for i in range(997650, 997652):
        list2 = []
       
        if is_prime(i):
            for j in range (2, i):
                if is_prime(j):
                    list2.append(j)
        for n1 in range (len(list2)):
           
            sum1 = 0
            list1 = []
            for n in range (n1, len(list2)):
                sum1 += list2[n]
                list1.append(list2[n])
                if sum1 == i:
                    print i, '==>', list1
                    list1.insert(0,i)
                    if len(list1) > len(list3):
                        list3 = list1
                        break
   
    print list3,len(list3)-1


if __name__ == '__main__':
    prob50()
