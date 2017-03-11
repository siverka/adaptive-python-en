operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "/": lambda x, y: x / y,
              "*": lambda x, y: x * y,
              "mod": lambda x, y: x % y,
              "pow": lambda x, y: x ** y,
              "div": lambda x, y: x // y}

a = float(input())
b = float(input())
op = input()

try:
    print(operations[op](a, b))
except ZeroDivisionError:
    print("Division by 0!")
