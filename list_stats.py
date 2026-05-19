def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
def find_max(numbers):

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
def range_of(numbers):
    maximo = find_max(numbers)
    minimo = find_min(numbers)
    return maximo - minimo

def average(numbers):
    if not numbers:
        return 0.0
    suma_total = 0
    for num in numbers:
        suma_total += num
    promedio = suma_total / len(numbers)
    return round(promedio, 1)
def describe(numbers):
    if not numbers:
        return "Empty list"
    minimo = find_min(numbers)
    maximo = find_max(numbers)
    rango = range_of(numbers)
    promedio = average(numbers)
    return f"Min:{minimo} Max:{maximo} Range:{rango} Avg:{promedio}"
