operations = {'plus': lambda x, y: x + y,
              'minus': lambda x, y: x - y,
              'multiply': lambda x, y: x * y,
              'divide': lambda x, y: x // y}

a, operation, b = input().split()
print(operations[operation](int(a), int(b)))
