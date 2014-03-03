from time import time
start_time = time()
def fun1(m, n):
    if m == n:
        return (n*(2*n + 1)*(n + 1))/6
    else:
        return (n*(n+1)*m*(m+1))/4
def prob85():
    a = 0
    for i in range(10, 100):
        if a > 2000000:
            print (i-1),j
            print (i-1)*j
            break
        for j in range(i, 100):
            a = fun1(i, j)
            #print i,j,'==>',a
            if a > 2000000:
                break
   


if __name__ == "__main__":
    prob85()
    print time() - start_time,'Seconds'
