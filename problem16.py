def multiples(n):
    a = n / 15
    b = n % 15
    print a, b
    return a, b


def sum(n):
    a, b = multiples(n)
    result = (32768 ** a) * (2 ** b)
    return result

if __name__ == "__main__":
    a = str(sum(1000))
    print a
    print len(a)
    number = 0
    for i in a:
        number += int(i)

    print number
