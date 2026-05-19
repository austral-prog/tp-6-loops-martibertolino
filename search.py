def index_of_by_index(target, lst, start):
    if start < 0:
        start = 0
    for i in range(start, len(lst)):
        if lst[i] == target:
            return i
    return -1
def index_of(target, lst):
    return index_of_by_index(target, lst, 0)

def index_of_empty(lst):
    return index_of_by_index("", lst, 0)
