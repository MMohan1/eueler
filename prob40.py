import time
start_time = time.time()
def prob40():
    list1=[]
    a=range(0,1000000)
    for no in a:
        list1.append(str(no))
    a = ''.join(list1)
    i=1
    p=1
    sum1=1
    while i<8:   
        sum1 *= int(a[p])
        p = p*10
        i = i+1
    print sum1
       







if __name__ == "__main__":
    prob40()
    print time.time() - start_time,'seconds'
