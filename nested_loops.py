def flatten(matrix):
    lista = []
    for fila in matrix:
        for elemento in fila:
            lista.append(elemento)
    return lista

def row_sums(matrix):
    answer = []
    for fila in matrix:
        answer.append(sum(fila))
    return answer


def col_sums(matrix):
    if len (matrix) == 0:
        return []
    num_colms = len(matrix[0])
    result = []
    for col in range(num_colms):
        total = 0
        for fila in matrix:
            total = total + fila[col]
        result.append(total)
    return result
