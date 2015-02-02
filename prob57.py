import time


def squareRootConvergents():
    numretor1, demenator1 = 3, 2
    numretor2, demenator2 = 7, 5
    out_put = 0
    for i in range(3, 1001):
        numretor = numretor2 * 2 + numretor1
        demenator = demenator2 * 2 + demenator1
        if len(str(numretor)) > len(str(demenator)):
            out_put += 1
        numretor1, demenator1 = numretor2, demenator2
        numretor2, demenator2 = numretor, demenator
    print out_put

if __name__ == "__main__":
    start_time = time.time()
    squareRootConvergents()
    print time.time() - start_time, 'Seconds'
