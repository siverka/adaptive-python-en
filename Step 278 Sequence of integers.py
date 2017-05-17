try:
    numbers = [int(x) for x in input().split()]
    numbers = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
    print(*numbers[::-1])
except EOFError:
    pass
