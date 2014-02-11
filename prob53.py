import time
start_time = time.time()
def factorial(n):
    return reduce(lambda x, y : x * y , range(1, n+1))

def combination(n, r):
    result = factorial(n) / (factorial(r) * factorial(n - r))
    return result

def prob53():
    count = 0
    for i in range(5, 101):
        for k in range(1, i):
            if combination(i, k) > 1000000:
                count += 1
       
           

    print count



if __name__ == '__main__':
    prob53()
    print time.time() - start_time,'seconds'
