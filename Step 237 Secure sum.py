def sum(a, b):
    is_int = map(lambda x: type(x) is int, [a, b])
    if all(is_int):
        if a > 0 and b > 0:
            return a + b
        else:
            raise ValueError
    else:
        raise TypeError


# print(sum(2, 3))
# print(sum(-2, 3))
# print(sum(2.8, 3))
# print(sum(2, 3.3))
