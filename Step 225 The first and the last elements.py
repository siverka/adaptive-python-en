def f(ls):
    return [ls[0], ls[-1]]

numbers = [int(x) for x in input().split()]
print(*f(numbers))
