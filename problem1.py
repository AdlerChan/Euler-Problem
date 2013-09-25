sum = 0

five_multiples = range(0, 1000, 5)
three_multiples = range(0, 1000, 3)

multiples = list(set(three_multiples + five_multiples))

for i in multiples:
    sum = sum + i

print sum
