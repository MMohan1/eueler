import time
start_time = time.time()
import sys
def palindrome(n):
    a = str(n)
    b = str(n)[::-1]
    if a == b:
        return False
    else:
        return True
def reverse(x):
    return int(str(x)[::-1])

def prob55():
    dict1 = {}
    list2 = []
    num_list = range(1, 10001)
    for num1 in num_list:
        total = num1
        count = 0
        if not palindrome(num1):
            rev_num = reverse(num1)
            total = num1 + rev_num
            while palindrome(total):
                count += 1
                num = total
                rev_num = reverse(num)
                total = num + rev_num
                if count >=50:
                    list2.append(num1)
                    break
        else:
            while palindrome(total):
                count += 1
                num = total
                rev_num = reverse(num)
                total = num + rev_num
                if count >=50:
                    list2.append(num1)
                    break
    print list2
    print len(list2)

if __name__ == '__main__':
    prob55()
    print time.time() - start_time,'seconds'
