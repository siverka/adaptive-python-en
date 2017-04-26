def f(ls):
    return(list(set(ls)))

lst = [int(x) for x in input().split()]
print(*f(lst))
