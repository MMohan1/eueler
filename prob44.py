'''this program running but taking time please provide if ou have a better solution'''
import time
start_time =time.time()
def prob44():
    a=[]
    m = 1
    i = 1000
    while m:
        i += 1
        p = (i*(3*i - 1))/2
        #i += 1'''this program running but taking time please provide if ou have a better solution'''
import time
start_time =time.time()
def prob44():
    a=[]
    m = 1
    i = 1000
    while m:
        i += 1
        p = (i*(3*i - 1))/2
        #i += 1
        a.append(p)
        print a
        for no in a:
            #print no
            if (p - no) in a and p - 2*no in a:
                print p - 2*no
                m = 0
                break


if __name__ == '__main__':
    prob44()
    print time.time() - start_time                 


    
        a.append(p)
        print a
        for no in a:
            #print no
            if (p - no) in a and p - 2*no in a:
                print p - 2*no
                m = 0
                break


if __name__ == '__main__':
    prob44()
    print time.time() - start_time                 
