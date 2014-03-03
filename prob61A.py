'''from itertools import permutations
def genratecube():
    list1 = []
    for i in range(300, 410):
        list1.append(i ** 3)
        #print list1
    print list1
    return list1


def prob61():
    list4 = []
    list1 = []
    for i in range(345, 1000):
        list1.append(i ** 3)
    print list1
    for b in list1:
        if len(list4) == 4:
            break
        list4 = []
        a = str(b)
        list2 = list(permutations(a, len(a)))
        for no in list2:
            str1 = ''
            for i in range(len(no)):
                str1 += no[i]
            if int(str1) in list1:
                list4.append(int(str1))
            for k in list4:
                while list4.count(k)!=1:
                    list4.remove(k)
            if len(list4) == 4:
                print list4
                break



if __name__ == "__main__":
    prob61()
    #genratecube()'''


from collections import defaultdict
def cube(x): return x**3

def main():
    cubes = defaultdict(list)
    for i in range(10000):
        c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)
    print min([min(v) for k, v in cubes.items() if len(v) == 5])

if __name__ == "__main__":
    main()
