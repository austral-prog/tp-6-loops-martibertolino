def power(base, exp):
    if exp >= 0:
        result = 1
        for i in range (exp):
            result = result * base
        return result


def sum_of_powers(base, max_exp):
    acc = 0
    for i in range (max_exp + 1):
        acc = acc + base ** i
    return acc
