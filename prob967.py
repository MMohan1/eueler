partitions = {}
def partition(n):
    if n < 0: return 0
    if n == 0: return 1
    if n not in partitions:
        partitions[n] = sum([(-1)**(k+1) * (partition(n - (k * (3 * k - 1) / 2))
            + partition(n - (k * (3 * k + 1) / 2))) for k in range(1, n+1)])
    return partitions[n]

def main():
    a = True
    i = 55374
    while a:
        print i
        print partition(i)
        if partition(i) % 1000000 == 0:
            print i
            a = False
        else:
            i += 1

if __name__ == "__main__": main()
