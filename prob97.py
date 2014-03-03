import time
start_time = time.time()
def prob79():
    number = '319 \
680 \
180 \
690 \
129 \
620 \
762 \
689 \
762 \
318 \
368 \
710 \
720 \
710 \
629 \
168 \
160 \
689 \
716 \
731 \
736 \
729 \
316 \
729 \
729 \
710 \
769 \
290 \
719 \
680 \
318 \
389 \
162 \
289 \
162 \
718 \
729 \
319 \
790 \
680 \
890 \
362 \
319 \
760 \
316 \
729 \
380 \
319 \
728 \
716'
    num_list = number.split(' ')
    list2 = []
    str_number = ''.join(number.split(' '))
    num = [int(i) for i in range(0, 10) if str(i) in str_number]
    list2.extend('319')
    for i in num_list:
        n = list(i)
        for k in n:
            if k not in list2:
                list2.append(k)
        if list2.index(n[0]) > list2.index(n[1]):
            list2.remove(n[0])
            list2.insert(list2.index(n[1]),n[0])
        elif list2.index(n[0]) > list2.index(n[2]):
            list2.remove(n[0])
            list2.insert(list2.index(n[2]),n[0])
        elif list2.index(n[1]) > list2.index(n[2]):
            list2.remove(n[1])
            list2.insert(list2.index(n[2]),n[1])
       
    print ''.join(list2)



           
           

if __name__ == '__main__':
    prob79()
    print time.time() - start_time,'Seconds'
