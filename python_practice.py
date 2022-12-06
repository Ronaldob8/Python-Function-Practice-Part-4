# maximum of three numbers
def max_num(a, b, c):
    return max([1, 2, 3])


print(max_num(1, 2, 3))

# Multiply all numbers in a list


def mult_list(list):
    if len(list) == 0:
        return 0
    product = list[0]

    if len(list) > 1:
        for i in list[1:]:
            product = product * i
    return product


print(mult_list([2, 4, 6]))

# reverse string


def rev_string(string):
    return string[::-1]


print(rev_string("hello"))

# numbers fall in given range


def num_within(n, a, b):
    return n in range(a, b)


print(num_within(4, 2, 6))
