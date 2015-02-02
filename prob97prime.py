import import time
start_time = time.time()


def last10Digit():
    return str(28433 * 2 ** 7830457 + 1)[-10:]


if __name__ == '__main__':
    last10Digit()
    print time.time() - start_time, 'Seconds'
