def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

def count_negatives(numbers):
    if not numbers:
        return 0
    contador = 0
    for num in numbers:
        if num < 0:
           contador += 1
    return contador
