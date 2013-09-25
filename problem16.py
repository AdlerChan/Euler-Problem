def multiples(n):
    a = n / 15
    b = n % 15
    return a, b


def sum1(n):
    a, b = multiples(n)
    result = (32768 ** a) * (2 ** b)
    return result

if __name__ == "__main__":
    print sum([int(i) for i in str(sum1(1000))])
    print sum(map(lambda x: int(x), str(2 ** 1000)))
    print sum([int(i) for i in str(2 ** 1000)])
