def countdown(n):
    list = []
    while n >= 0:
        list.append(n)
        n -= 1
    return list
def double_until(limit):
    result = []
    value = 1
    while value <= limit:
        result.append(value)
        value = value * 2
    return result
