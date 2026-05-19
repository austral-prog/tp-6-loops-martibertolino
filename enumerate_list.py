def enumerate_list(lst):
    if not lst:
        return []

    resultado = []
    index = 0
    for elemento in lst:
        if elemento != "":
            resultado.append(f"{index}. {elemento}")
            index += 1
    return resultado

def enumerate_backwards(lst):
    resultado = []
    index = 0
    for elemento in lst:
        if elemento != "":
            backwards = ""
            for letras in elemento:
                backwards = letras + backwards
            resultado.append(f"{index}. {backwards}")
            index += 1
    return resultado
