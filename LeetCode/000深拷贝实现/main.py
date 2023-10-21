from collections.abc import Iterable

def my_deepcopy(src):
    tgt = []
    for item in src:
        if isinstance(item, Iterable):
            tgt.append(my_deepcopy(item))
        else:
            tgt.append(item)

    return tgt


a = [[1, 2, 3, 4], 5, 6]
b = my_deepcopy(a)
pass