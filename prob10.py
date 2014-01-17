def triange():
    a=0
    list1=[]
    dict1={}
    for i in range(1,20000000):
        a=a+i
        print a
        list1.append(a)
    print list1
    for j in list1:
        list2=[]
        for k in range(1,j+1):
            print j
            if j%k==0:
                list2.append(k)
        if(len(list2)>500):
            dict1[j]=list2
            break
    if dict1:       
        print dict1
    else:
        print 'not found'        
