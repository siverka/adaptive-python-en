from functools import reduce
_ = int(input())
numbers = [int(i) for i in input().split()]
numbers.insert(0, 0)
print(reduce(lambda result, number: (113 * (number + result)) % 10000007, numbers))
